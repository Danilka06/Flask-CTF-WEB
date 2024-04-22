import sqlalchemy as sa
import sqlalchemy.ext.declarative as dec
import sqlalchemy.orm as orm


SqlAlchemyBase = dec.declarative_base()

__factory = None  # db session


def global_init(db_url: str):
    global __factory

    if __factory:
        return

    if not db_url or not db_url.strip():
        raise Exception("incorrect path")

    engine = sa.create_engine(db_url)

    from app.core import models

    __factory = orm.sessionmaker(bind=engine)
    SqlAlchemyBase.metadata.create_all(engine)


def create_session():
    global __factory

    return __factory()
