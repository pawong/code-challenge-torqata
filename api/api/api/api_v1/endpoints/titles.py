import logging
from typing import Any, List, Optional
from ....schemas.title import Title

from fastapi import APIRouter, Body, Depends, HTTPException, Request
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from api import crud, models, schemas
from api.api import deps
from api.core.config import settings


router = APIRouter()


@router.get("/", response_model=List[schemas.Title])
def read_titles(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    order_by: str = "",
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve titles.
    """
    titles = crud.title.get_multi(db, skip=skip, limit=limit, order_by=order_by)
    return titles


@router.post("/", response_model=schemas.Title)
def create_title(
    *,
    db: Session = Depends(deps.get_db),
    title_in: schemas.TitleCreate,
    current_user: models.User = Depends(
        deps.get_current_active_superuser
    ),  # Authorize?
    request: Request,
) -> Any:
    """
    Create new title.
    """
    if not title_in:
        raise HTTPException(
            status_code=404,
            detail="Unable to process program data",
        )

    title = crud.title.create(db, obj_in=title_in)
    return title


@router.get("/{title_id}", response_model=schemas.Title)
def read_title_by_id(
    title_id: int,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: Session = Depends(deps.get_db),
) -> Any:
    """
    Get a specific title by id.
    """
    title = crud.title.get(db, id=title_id)
    return title


@router.put("/{title_id}", response_model=schemas.Title)
def update_title(
    *,
    db: Session = Depends(deps.get_db),
    title_id: int,
    title_in: schemas.TitleUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
    request: Request,
) -> Any:
    """
    Update a title.
    """
    title = crud.title.get(db, id=title_id)
    if not title:
        raise HTTPException(
            status_code=404,
            detail="The title with this id does not exist in the system",
        )
    title = crud.title.update(db, db_obj=title, obj_in=title_in)
    return title


@router.get("/search/", response_model=List[schemas.Title])
def search_titles(
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_superuser),
    skip: int = 0,
    limit: int = 100,
    order_by: str = "",
    query: str = "",
) -> Any:
    """
    Retrieve titles that match the query string.
    """
    titles = crud.title.search_titles(
        db, skip=skip, limit=limit, order_by=order_by, query=query
    )
    return titles
