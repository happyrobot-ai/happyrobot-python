from enum import Enum
from typing import Optional, Literal
from pydantic import BaseModel
import json
from typing import List, Dict, Any

from happyrobot.src.utils.message_utils import combine_messages


class MessageRole(str, Enum):
    System = "system"
    User = "user"
    Assistant = "assistant"
    Tool = "tool"


class Function(BaseModel):
    name: str
    arguments: str
    

class ToolCall(BaseModel):
    type: Literal["function"] = "function"
    id: str
    function: Function
    


class Message(BaseModel):
    id: str
    role: MessageRole
    content: str
    tool_calls: Optional[list[ToolCall]] = None
    tool_call_id: Optional[str] = None
    name: Optional[str] = None
    


class Messages(BaseModel):
    messages: list[Message]
    
    def _process_tool_call(self, tool_call: ToolCall):
        # Helper function to process each tool call, including nested 'function' key
        processed_call = {}
        for key, value in tool_call.model_dump().items():
            if key == "function":
                # Process the 'function' key's value, which is expected to be a dict
                value = {k: v for k, v in value.items() if not (k == "arguments" and v.strip() == "{}")}
            elif key == "id":
                continue
            processed_call[key] = value
        return processed_call
    
    def to_dict(self, drop_id: bool = True):
        messages = [
            {
                **({"id": message.id} if not drop_id else {}),
                "role": message.role.value,
                **({"name": message.name} if message.name else {}),
                "content": message.content.strip() if message.content else None,
                **({"tool_calls": [self._process_tool_call(tc) for tc in message.tool_calls]} if message.tool_calls else {}),
            }
            for message in self.messages if message.content.strip() != ""
        ]
        
        # Remove system messages
        messages = [message for message in messages if message["role"] != "system"]
        # Concatenate messages just in case
        messages = combine_messages(messages)
        return messages
    
    @staticmethod
    def serialize(messages: List[Dict[str, Any]]):
        def is_json_string(s):
            # Helper function to check if a string is JSON
            try:
                json_object = json.loads(s)
                return isinstance(json_object, dict)  # Check if the loaded object is a dictionary
            except json.JSONDecodeError:
                return False

        def serialize_item(item):
            # Recursively serialize each item, checking for JSON strings
            if isinstance(item, dict):
                return {key: serialize_item(value) for key, value in item.items()}
            elif isinstance(item, list):
                return [serialize_item(element) for element in item]
            elif isinstance(item, str) and is_json_string(item):
                return json.loads(item)  # Parse the JSON string into a dict
            else:
                return item  # Return the item as is if it's not a dict, list, or JSON string

        return json.dumps([serialize_item(message) for message in messages])
        
