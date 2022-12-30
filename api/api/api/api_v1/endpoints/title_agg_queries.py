from typing import Any, List
from sqlalchemy.orm import Session

from fastapi import APIRouter, Request, Depends

from api import crud, models, schemas
from api.controllers import SQLQueryController
from api.api import deps
from api.core.config import settings

router = APIRouter()

title_count_by_category_sql = (
    "select count(*), category as key, 'category' as key_type "
    "from titles "
    "group by category; "
)

title_movie_avg_runtime_sql = (
    "SELECT ROUND(AVG(TO_NUMBER(duration, '9999 min'))::NUMERIC, 2) as count, 'Movie' as key, 'average_duration' as key_type "
    "FROM titles "
    "WHERE category = 'Movie' "
    "GROUP BY category; "
)


@router.get("/title-count-by-category", response_model=List[schemas.SQLCountQuery])
def title_count_by_category(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """title-count-by-category endpoint"""
    return SQLQueryController.read_many(db, title_count_by_category_sql)


@router.get("/title-movie-avg-runtime", response_model=List[schemas.SQLCountQuery])
def title_movie_avg_runtime(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
):
    """title-movie-avg-runtime endpoint"""
    return SQLQueryController.read_many(db, title_movie_avg_runtime_sql)
