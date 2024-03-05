from fastapi import APIRouter
from Module.Users import Users
from schema import UserResponseSchema
router = APIRouter()

@router.post('/users')
async def start_quiz(request:UserResponseSchema):
    return Users().create_user(request)