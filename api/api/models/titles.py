from sqlalchemy.dialects import postgresql
from sqlalchemy import Column, Integer, Text, DateTime

from api.db.base_class import Base


class Title(Base):
    __tablename__ = "titles"

    id = Column(Integer, primary_key=True, index=True)

    show_id = Column(Text)
    category = Column(Text)
    title = Column(Text)
    director = Column(Text)
    cast_members = Column(Text)
    country = Column(Text)
    date_added = Column(DateTime)
    release_year = Column(Integer)
    rating = Column(Text)
    duration = Column(Text)
    listed_in = Column(Text)
    description = Column(Text)
