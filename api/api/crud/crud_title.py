from typing import Any, Dict, Optional, Union, List
from datetime import datetime

from sqlalchemy.orm import Session

from api.crud.base import CRUDBase
from api.models.titles import Title
from api.schemas.title import TitleCreate, TitleUpdate


class CRUDTitle(CRUDBase[Title, TitleCreate, TitleUpdate]):
    def create(self, db: Session, *, obj_in: TitleCreate) -> Title:
        db_obj = Title(
            show_id=obj_in.show_id,
            category=obj_in.category,
            title=obj_in.title,
            director=obj_in.director,
            cast_members=obj_in.cast_members,
            country=obj_in.country,
            date_added=obj_in.date_added,
            release_year=obj_in.release_year,
            rating=obj_in.rating,
            duration=obj_in.duration,
            listed_in=obj_in.listed_in,
            description=obj_in.description,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def update(
        self, db: Session, *, db_obj: Title, obj_in: Union[TitleUpdate, Dict[str, Any]]
    ) -> Title:
        if isinstance(obj_in, dict):
            title_data = obj_in
        else:
            title_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=title_data)

    def search_titles(
        self,
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
        order_by: str = "",
        query: str = "",
    ) -> List[Title]:
        return (
            db.query(self.model)
            .filter(self.model.title.contains(query))
            # .order_by(order_by)
            .offset(skip)
            .limit(limit)
            .all()
        )


title = CRUDTitle(Title)
