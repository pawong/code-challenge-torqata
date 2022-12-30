FROM python:3.8-slim

COPY ./ /api/

WORKDIR /api/
RUN echo "${GIT_COMMIT}" >> REVISION

RUN pip install poetry
RUN poetry install

#CMD ["poetry", "run", "uvicorn", "api.main:api", "--host", "0.0.0.0", "--port", "8080"]
CMD HOME=/root poetry run uvicorn api.main:api --host 0.0.0.0 --port 8080
