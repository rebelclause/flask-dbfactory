from datetime import datetime
from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

from sqlalchemy import Column, Integer, String
# for composite key creation ForeignKeyConstraint must be used instead of, or in addition to, ForeignKey
from sqlalchemy import ForeignKey, ForeignKeyConstraint
from sqlalchemy.types import Boolean, DateTime
from sqlalchemy.orm import relationship

from dataclasses import dataclass, InitVar, field
from typing import Any, List, ClassVar

import pprint
from flask_dbfactory import DBFactory

pp = pprint.PrettyPrinter(indent=4)

def create_app():

    # create the Flask instance
    app = Flask(__name__.split('.')[0])

    # instantiate DB_Factory, creating default db 'main', or string argument name
    # mydb = DBFactory(app)
    mydb = DBFactory(app, "bogus_or_bonus")

    app.config.__setitem__('SQLALCHEMY_TRACK_MODIFICATIONS', False)

    # instantiate SQLAlchemy
    db = SQLAlchemy(app)

    return mydb, db, app

mydb, db, app = create_app()

# anydb = DBFactory(app, 'whoa_not_ok')

# no bind key used here by design
@dataclass
class U_Mixin(db.Model): # (object) if not __abstract__ = True
    wabisabi: ClassVar
    id: int

    __abstract__ = True # use if inheriting from db.Model
    __bind_key__ = ""

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)

DB = DBFactory.dblist[0]
# DB = mydb.new_db("one_to_many")
# print("DB looks like: ", DB)

@dataclass
class User(U_Mixin, UserMixin, db.Model):
    # id: int
    username: int

    __bind_key__ = DB.get('name')
    # id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, nullable=False)
    # ::backref arg:: a collection of the referencing table
    somany = relationship('Many', backref='manycollecton')

@dataclass
class Many(U_Mixin, db.Model):
    # id: int
    many: int
    user_id: int

    __bind_key__ = DB.get('name')
    # id = Column(Integer, primary_key=True, nullable=False)
    many = Column(Integer, nullable=False)
    # ::foreignkey arg:: table name<dot>column name
    user_id = Column(Integer, ForeignKey('user.id'))


DB = mydb.new_db("many_to_many_incorrect")

@dataclass
class Parent(U_Mixin):
    parentname: str
    child_id: int

    __bind_key__ = DB.get('name')
    parentname = Column(String)
    child_id = Column(Integer, ForeignKey('child.id'))
    children = relationship('Parent', backref='children')

@dataclass
class Child(U_Mixin):
    childname: str
    parent_id: int

    __bind_key__ = DB.get('name')
    childname = Column(String)
    parent_id = Column(Integer, ForeignKey('parent.id'))
    parents = relationship('Child', backref='parents')


DB = mydb.new_db("joins")

class Bind():
    __bind_key__ = DB.get('name')

@dataclass
class Users(Bind, U_Mixin, db.Model):
    pass

@dataclass
class Posts(Bind, U_Mixin, db.Model):
    pass

@dataclass
class Likes(Bind, U_Mixin, db.Model):
    pass

@dataclass
class Comments(Bind, U_Mixin, db.Model):
    pass


if __name__ == "__main__":
    print(f"List of all DB binds in DBFactory.dblist:")
    pp.pprint(list(DBFactory.dblist))
    # db.create_all()
