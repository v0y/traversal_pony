# -*- coding: utf-8 -*-

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm.exc import NoResultFound

from pony.db import Base, DBSession


class Kind(Base):
    __tablename__ = 'kinds'
    name = Column(String(255))

    def __getitem__(self, key):
        try:
            return DBSession.query(Pony).filter_by(
                name=key, kind=self).one()
        except NoResultFound:
            raise KeyError(key)


class Group(Base):
    __tablename__ = 'groups'
    name = Column(String(255))

    def __getitem__(self, key):
        try:
            return DBSession.query(Pony).filter_by(
                name=key, group=self).one()
        except NoResultFound:
            raise KeyError(key)


class Pony(Base):
    __tablename__ = 'ponies'
    name = Column(String(255))
    kind_id = Column(Integer, ForeignKey('kinds.id'))
    kind = relationship('Kind', backref='ponies')
    colour = Column(String(255))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', backref='ponies')

