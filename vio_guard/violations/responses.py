from pydantic import BaseModel 
from datetime import datetime
from pydantic import Field

class User(BaseModel):
    id: int
    username: str
    password: str

class ViolationSummary(BaseModel):
    total_violations= 10,
    active_violations= 5,
    student_violations = 3,
    resolved_violations = 2,
    referred_to_council = 3

class datetime(BaseModel):
    year: int
    month: int
    day: int
    hour:int
    minute: int
    second: int
    auto_now: bool = False
     
class Summary(BaseModel):
    summary: list[ViolationSummary]
    generated_by: str  
    generated_at: datetime = Field(default_factory=datetime.utcnow)
 
class Violation(BaseModel):
    id: int
    violation_type: str
    student_id: int
    description: str
    reported_by: int
    created_at: datetime
    updated_at: datetime | None = None
    status: str = 'Pending'
    approved_by: int | None = None