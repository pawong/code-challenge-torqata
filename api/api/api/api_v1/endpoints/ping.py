import socket
import datetime
import json

from typing import Any

from fastapi import APIRouter, HTTPException, Request


router = APIRouter()


@router.get("")
def ping(request: Request):
    """ping endpoint"""
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return {
        "status": "success",
        "ping": "pong",
        "server_time": datetime.datetime.now(),
        "root_path": request.scope.get("root_path"),
        "host_name": host_name,
        "host_ip": host_ip,
        "header": request.headers,
    }
