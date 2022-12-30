# MAS FastAPI server

## Run locally

```
% poetry run uvicorn api.main:api --reload
```

## Start Shell on Server

```
$ docker exec -it api /bin/bash
```

## Sometimes directory is rebuilding so this

```
$ poetry run python -m compileall .
```
