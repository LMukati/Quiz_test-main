from fastapi import APIRouter
from Module.question import Questions
router = APIRouter()

@router.get('/questions')
async def fetch_all_questions():
    return Questions().fetch_all_questions()