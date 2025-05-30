from pydantic import BaseModel
from typing import Optional, Dict
from datetime import datetime
class Event(BaseModel):
    event_id: str
    device_id: str
    timestamp: datetime
    event_type: str
    payload: Dict
class EventUpdate(BaseModel):
    event_type: Optional[str]
    payload: Optional[Dict]
