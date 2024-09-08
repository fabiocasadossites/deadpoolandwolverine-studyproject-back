from http import HTTPStatus

from fastapi import APIRouter

from deadpoolandwolverine_backend.schemas import Message

router = APIRouter(prefix='', tags=['example'])


@router.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}
