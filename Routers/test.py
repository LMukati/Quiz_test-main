from fastapi import APIRouter

router = APIRouter()

@router.get('/')

def test_api():
    return {'message':'welcome'}
