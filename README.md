# flask_DBFactory

Simple import method, to inline SQLAlchemy DB/model creation, for fast ORM prototyping setups.

**About**

DBFactory is a simple Flask instance class which makes it possible to bind declarations of SQLAlchemy model/database relations as they are needed in a model file.

`factory_floor.py` presents an SQLAlchemy model playground, exemplifying the core project's aim: tooling of use for development.

Since SQLite reduces database creation to a single line, DBFactory leverages this fact to make light work of model binding, using Flask-SQLAlchemy's interpretation of SQLAlchemy in terms of `SQLALCHEMY_DATABASE_URI` and `SQLALCHEMY_BINDS` interaction with SQLAlchemy through bound table metadata.
 
Inlining is done with the SQLAlchemy directive `__bind_key__`. In the example the directive is set to `DB.get('name')` on related table classes, forming a model set. 

As shown, the directive also makes it possible to link tables through a common parent class, to be inherited by all tables in a model, or overridden.

#### Use
Like Flask_SQLAlchemy, simply import DBFactory and instantiate it after instantiating your Flask app.

##### Import:

`from flask_dbfactory import DBFactory`

##### Create instance:
Below your declared flask instance, usually `app`:

`dbfactory = DBFactory(app)`

This will create a 'main' database, which you can use or ignore.

##### Inline declaration:

`DB = dbfactory.new_db('my_model_db_name')`

##### Use:

Run `factory_floor.py` in your REPL, then you can inspect your models, and, finally, `db.create_all()` to create all.

### Possible Features:

- Selectively create the database for any one of the declared binds.


