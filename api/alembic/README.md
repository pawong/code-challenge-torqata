# Generic single-database configuration.

## Auto generate change

From the API directory,
```
% poetry run alembic revision --autogenerate -m "Add your comment here."
```

## Run updates

```
%  poetry run alembic upgrade head
```
