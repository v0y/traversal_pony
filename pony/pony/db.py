from sqlalchemy import Integer, Column
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from sqlalchemy.ext.declarative import declarative_base
from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))


def get_session():
    session = scoped_session(sessionmaker(extension=None))
    session.configure(bind=DBSession.get_bind())
    return session


class BaseModel(object):
    id = Column(Integer, primary_key=True)

    @classmethod
    def by_id(cls, id_):
        return DBSession.query(cls).filter_by(id=id_).first()


Base = declarative_base(cls=BaseModel)
