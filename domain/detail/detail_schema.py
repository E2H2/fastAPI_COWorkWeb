# schema
# schema는 request, response의 입출력을 제한할거야!

# for using server.default time
import datetime

# using pydantic BaseModel for schema
from pydantic import BaseModel, field_validator

from domain.comment.comment_schema import Comment

class Create(BaseModel):
    member_id : int
    title : str
    content : str
    start_price : int
    completed_status_yn : str
    image_id : int
    image_url : str
    area : str

class Detail(BaseModel):
    title : str
    content : str
    nickname : str
    create_date : datetime.datetime
    area : str
    image_url : str
    comment  : list[Comment] = []

class Update(BaseModel):
    content : str
    image_url : str