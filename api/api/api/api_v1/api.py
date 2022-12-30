from fastapi import APIRouter

from api.api.api_v1.endpoints import (
    login,
    users,
    titles,
    ping,
    eight_ball,
    title_agg_queries,
)


api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(titles.router, prefix="/titles", tags=["titles"])
api_router.include_router(ping.router, prefix="/ping", tags=["ping"])
api_router.include_router(eight_ball.router, prefix="/8ball", tags=["eight-ball"])
api_router.include_router(title_agg_queries.router, prefix="/aggs", tags=["aggs"])
