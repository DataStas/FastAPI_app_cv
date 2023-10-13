from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import APIRouter, Depends

from ..database import get_async_session
from ..operations.models import input_const_params, input_variable_params
from ..auth.base_config import current_user


router = APIRouter(
    prefix="/models",
    tags=["model"]
)

@router.get("/variable_params")
async def get_variable_params(exp_tag: str,
                              id: int, 
                              session: AsyncSession = Depends(get_async_session),
                              user=Depends(current_user)):
    id_cond = (input_variable_params.c.id == id)
    exp_cond = (input_variable_params.c.experiment_tag == exp_tag)
    query = select(input_variable_params).where((input_variable_params.c.id == id)&
                                                (input_variable_params.c.experiment_tag == exp_tag))
    result = await session.execute(query)
    var_data = [dict(r._mapping) for r in result]
    id_cond = (input_const_params.c.id == id)
    exp_cond = (input_const_params.c.experiment_tag == exp_tag)
    query = select(input_const_params).where((input_const_params.c.id == id)&
                                             (input_const_params.c.experiment_tag == exp_tag))
    result = await session.execute(query)
    const_data = [dict(r._mapping) for r in result],
    var_data += const_data
    
    return {'status': 'success',
            'data': var_data,
            'details': None}