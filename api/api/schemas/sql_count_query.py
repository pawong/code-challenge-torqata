from unicodedata import numeric
from pydantic import BaseModel


class SQLCountQuery(BaseModel):
    count: float
    key: str
    key_type: str
