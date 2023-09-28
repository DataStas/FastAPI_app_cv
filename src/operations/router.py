from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from .models import input_const_params, input_variable_params
from .schemas import ConstParamsCreate, VariableParamsCreate

router = APIRouter(
    prefix="/rw_operations",
    tags=["R/W data to database"]
)


@router.get("/const")
async def get_const_params(exp_tag: str,
                           session: AsyncSession = Depends(get_async_session)):
    query = select(input_const_params).where(input_const_params.c.experiment_tag == exp_tag)
    result = await session.execute(query)
    return [dict(r._mapping) for r in result]

@router.post("/const")
async def add_const_params(new_operation: ConstParamsCreate,
                           session: AsyncSession = Depends(get_async_session)):
    stmt = insert(input_const_params).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}

@router.get("/variable")
async def get_variable_params(exp_tag: str, 
                              session: AsyncSession = Depends(get_async_session)):
    query = select(input_variable_params).where(input_variable_params.c.experiment_tag == exp_tag)
    result = await session.execute(query)
    print(result)
    return [dict(r._mapping) for r in result]

@router.post("/variable")
async def add_variable_params(new_operation: VariableParamsCreate,
                              session: AsyncSession = Depends(get_async_session)):
    stmt = insert(input_variable_params).values(**new_operation.model_dump())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}