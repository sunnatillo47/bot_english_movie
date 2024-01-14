import sqlite3

class Voitesbase:
    def __init__(self, path_to_db="voites.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_voites(self):
        sql = """
        CREATE TABLE Voites (
            movie_id_ref int REFERENCES Movies(id),
            user_id bigint
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_voites(self, movie_id_ref, user_id):

        sql = """
        INSERT INTO Voites(movie_id_ref, user_id) VALUES(?, ?)
        """
        self.execute(sql, parameters=(movie_id_ref, user_id), commit=True)

    def select_all_voites(self, movie_id_ref):
        sql = """
        SELECT user_id FROM Voites where movie_id_ref=?
        """
        return self.execute(sql,parameters=(movie_id_ref,), fetchall=True)

    def select_user(self, **kwargs):
        sql = "SELECT * FROM Voites WHERE"
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)



def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")