from enum import Enum
from typing import Optional, Literal
from pydantic import BaseModel


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

