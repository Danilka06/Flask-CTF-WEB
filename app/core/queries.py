from sqlalchemy.orm.session import Session

from app.core.models import User
from app.core import db_session

global_session = None


def use_db(func):
    """
    Helps to replace this
    db = create_session()
    query = get(data, db)

    to this
    query = get(data)

    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        global global_session

        if global_session is None:
            global_session = db_session.create_session()
        return func(*args, **kwargs, db=global_session)

    return wrapper


# ==== DB ====
@use_db
def delete(model, db: Session) -> None:
    db.delete(model)


@use_db
def add(model, db: Session) -> None:
    db.add(model)


@use_db
def add_and_commit(model, db: Session) -> None:
    db.add(model)
    db.commit()


@use_db
def flush(db: Session):
    db.flush()


@use_db
def commit(db: Session) -> None:
    db.commit()


@use_db
def get_user_by_login(login: str, db: Session):
    return db.query(User).filter(User.login == login).first()


@use_db
def get_user_by_id(id: int, db: Session) -> User | None:
    return db.query(User).filter(User.id == id).first()


@use_db
def get_password_by_login(login: str, db: Session) -> User | None:
    return db.query(User).filter(User.login == login).first()

