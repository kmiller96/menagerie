import fastapi

from sqlmodel import SQLModel, Field, Session, select, create_engine

from starlette_admin import BaseAdmin
from starlette_admin.contrib.sqla import Admin, ModelView

##############
## Database ##
##############

engine = create_engine("sqlite:///test.db", echo=True)


###########
## Admin ##
###########


def add_admin(app: fastapi.FastAPI):
    """Registers the admin panel to the FastAPI application."""
    admin: BaseAdmin = Admin(engine)

    admin.add_view(ModelView(User))

    admin.mount_to(app)


############
## Models ##
############


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)

    name: str
    age: int


#################
## Application ##
#################


app = fastapi.FastAPI()

add_admin(app)


@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.get("/users")
def list_users():
    with Session(engine) as session:
        return session.exec(select(User)).all()


@app.get("/users/{user_id}")
def get_user(user_id: int):
    with Session(engine) as session:
        user = session.get(User, user_id)
        return user
