# schema

import datetime
from typing import Optional
# using pydantic BaseModel for schema
from pydantic import BaseModel, field_validator

class Create(BaseModel):
    content : str
    price : int

class Comment(BaseModel):
    content : str
    price : int

class Update(BaseModel):
    content: Optional[str] = None
    price: Optional[int] = None

    # class Update(BaseModel):
    # content: str | None = None
    # price: int | None = None  # 'price' 필드가 정의되어 있음