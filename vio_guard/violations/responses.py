from pydantic import BaseModel 
from datetime import datetime
from pydantic import Field

class User(BaseModel):
    id: int
    username: str
    password: str

class ViolationSummary(BaseModel):
    total_violations= 9,
    active_cases= 5,
    student_involved = 3,
    resolved = 5,
     
class Summary(BaseModel):
    summary: list[ViolationSummary]
    generated_by: str  
    generated_at: datetime = Field(default_factory=datetime.utcnow)

#guard
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