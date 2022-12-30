from typing import Any
from sqlalchemy.orm import Session

from fastapi import Request


class SQLQueryController:

    @staticmethod
    def read_many(db: Session, sql: str):
        results = db.execute(sql)
        return [dict(r) for r in results]

    @staticmethod
    def read(db: Session, sql: str):
        results = db.execute(sql)
        return dict(results.fetchone())
