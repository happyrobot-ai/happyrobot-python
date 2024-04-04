from typing import Optional
from pydantic import BaseModel, Field
from typing import Optional


class CallMetadata(BaseModel):
    call_sid: Optional[str] = None
    ffrom: str = Field(alias="from")
    to: str


class Call(BaseModel):
    id: str
    organization_id: str
    metadata: CallMetadata
    created: str
    