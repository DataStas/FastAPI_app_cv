from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from fastapi import Depends

from ..database import get_async_session
from ..operations.models import input_const_params, input_variable_params


async def get_variable_params(exp_tag: str,
                              id: int, 
                              session: AsyncSession = Depends(get_async_session)):
    exp_condition = input_variable_params.c.experiment_tag == exp_tag
    id_condition = input_variable_params.c.id == id
    query = select(input_variable_params).where(exp_condition and id_condition)
    result = await session.execute(query)
    var_data = [dict(r._mapping) for r in result]
    query = select(input_const_params).where(exp_condition and id_condition)
    result = await session.execute(query)
    const_data = [dict(r._mapping) for r in result],
    
    return {'status': 'success',
            'data': var_data+const_data,
            'details': None}