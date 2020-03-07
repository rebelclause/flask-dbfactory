"""

"""

from flask import current_app, _app_ctx_stack

class DBFactory():
    dblist = []
    extant = False

    def __init__(self, app, *args):

        try:
            if DBFactory.extant == True:
                raise TypeError
        except TypeError as e:
            print("Only one instance of DBFactory is allowed.", {e})
            # exit

        if len(args) >=1:
            for _ in args:
                dbname = _
        else:
            dbname = 'main'
        self.app = app # used, kept for expansion
        if app is not None:
            self.init_app(app, dbname)

    def init_app(self, app, dbname):
        DBFactory.extant = True

        if DBFactory.dblist.__len__() <= 0:
            app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{dbname}.sqlite"

        idx = DBFactory.dblist.__len__()
        DBFactory.dblist.append({'name': dbname, 'uri': f"sqlite:///{dbname}.sqlite", 'idx': f"{idx}"})

        try:
            app.config['SQLALCHEMY_BINDS'] = {
                DBFactory.dblist[0]['name']: app.config.get('SQLALCHEMY_DATABASE_URI'), # invite key error
            }
        except KeyError as e:
            print(f"Error: {e}")

        init_uri = self.new_db(dbname)

    def new_db(self, dbname):
        idx = DBFactory.dblist.__len__()
        DBFactory.dblist.append({'name': dbname, 'uri': f"sqlite:///{dbname}.sqlite", 'idx': f"{idx}"})
        self.app.config['SQLALCHEMY_BINDS'][dbname] = DBFactory.dblist[idx]['uri']
        print("DBFactory.dblist entry:" + "{" + "\"name\":" + "\"" + dbname + "\"" + "," + "\"uri\":" + "\"" + f"sqlite:///{dbname}.sqlite" + "\", " + "\"idx\":" + f"{idx}" + "}")
        return {"name": dbname, "uri": f"sqlite:///{dbname}.sqlite", "idx": f"{idx}"}


if __name__ == "__main__":
    pass

# https://flask.palletsprojects.com/en/1.1.x/extensiondev/?highlight=extensions%20dev

"""
        appdata = 'postgresql+{}://{}:{}@{}:{}/{}'.format(
            users['driver'],
            users.get('user'),
            users.get('pwd'),
            users.get('host'),
            users.get('port'),
            users.get('db'))            
            )

        connection = mysql.connector.connect(

         appdata = 'mysql://{}:{}@{}:{}/{}'.format(
            host = host_name,
            user = user_name,
            passwd = user_password,
            port = 3436,
            # need to query the db and then launch into create if the db does not exist
            database = db_name
            
        # What SQLAlchemy gives: 
        # pydoc3 -p 4200    
        # http://localhost:4200/sqlalchemy.html#Index
        # http://localhost:4200/sqlalchemy.html#MetaData
        
        create(self, bind=None)
            Issue a ``CREATE`` statement for this
            :class:`.Index`, using the given :class:`.Connectable`
            for connectivity.
             
            .. seealso::
             
                :meth:`.MetaData.create_all`.

"""
