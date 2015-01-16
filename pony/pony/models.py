# -*- coding: utf-8 -*-

from sqlalchemy import String, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from pony.db import BaseModel


class Kind(BaseModel):
    __tablename__ = 'kinds'
    name = Column(String(255))


class Group(BaseModel):
    __tablename__ = 'groups'
    name = Column(String(255))


class Pony(BaseModel):
    __tablename__ = 'ponies'
    name = Column(String(255))
    kind_id = Column(Integer, ForeignKey('kinds.id'))
    kind = relationship('Kind', backref='ponies')
    colour = Column(String(255))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', backref='ponies')

