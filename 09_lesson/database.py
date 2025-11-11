from sqlalchemy import create_engine, text


class Database:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string)

    def execute_query(self, query, params=None):
        with self.engine.begin() as connection:
            result = connection.execute(text(query), params or {})
            if query.strip().upper().startswith('SELECT'):
                return result.fetchall()
