# Import all the models, so that Base has them before being
# imported by Alembic
from api.db.base_class import Base  # noqa
from api.models.users import User  # noqa
from api.models.titles import Title  # noqa
