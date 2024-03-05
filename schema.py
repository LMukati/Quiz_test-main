from pydantic import BaseModel,Field,EmailStr
from typing import List

class QuestionResponseSchema(BaseModel):
    question_id : int=Field(...)
    option_id : int=Field(...)

class UserSchema(BaseModel):
    first_name : str=Field(...,max_length=15)
    last_name : str=Field(...,max_length=15)
    email : EmailStr=Field(...)


class UserResponseSchema(BaseModel):
    user_details :UserSchema
    response :List[QuestionResponseSchema]
    