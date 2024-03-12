from enum import Enum
from typing import Optional, Union, List
from pydantic import BaseModel

from happyrobot_python.models.call import Call
from happyrobot_python.models.message import Message


class StartContent(BaseModel):
    recording: Optional[str] = None


class EndContent(BaseModel):
    messages: list[Message]
    tools: Optional[dict] = None



class EventType(str, Enum):
    Start = "start"
    Message = "message"
    End = "end"


class Event(BaseModel):
    type: EventType
    call: Call
    content: dict

    class Config:
        use_enum_values = True