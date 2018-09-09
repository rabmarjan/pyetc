from injector import inject, Injector, provider, Module, Key, singleton
import sqlite3


class RequestHandler:
    @inject
    def __init__(self, db: sqlite3.Connection):
        self._db = db

    def get(self):
        cursor = self._db.cursor()
        cursor.execute('SELECT key, value FROM data ORDER by key')
        return cursor.fetchall()


Configuration = Key("configuration")


def configuration_for_testing(binder):
    configuration = {"db_connection_string": ":memory:"}
    binder.bind(Configuration, to=configuration, scope=singleton)


class DatabaseModule(Module):
    @singleton
    @provider
    def provide_sqlite_connection(self, configuration: Configuration) -> sqlite3.Connection:
        conn = sqlite3.connect(configuration["db_connection_string"])
        cursor = conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS data (key PRIMARY KEY, value)')
        cursor.execute('INSERT OR REPLACE INTO data VALUES ("Marjan", "Python")')
        return conn


injector = Injector([configuration_for_testing, DatabaseModule()])
handler = injector.get(RequestHandler)
print(tuple(map(str, handler.get()[0])))

# We can also verify that our Configuration and SQLite connections are indeed singletons within the Injector:

print(injector.get(Configuration) is injector.get(Configuration))
print(injector.get(sqlite3.Connection) is injector.get(sqlite3.Connection))

first_name: str = "Marjan"
print(f"Hi, {first_name}!")
