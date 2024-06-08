from pydantic import BaseModel

class Todo(BaseModel):
    id: int
    savetime: str
    name: str
    item: str