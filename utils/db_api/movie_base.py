
import sqlite3

class MovieDB:
    def __init__(self, path_to_db="movie.db"):
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

    def create_table_Movies(self):
        sql = """
        CREATE TABLE Movies (
            id int NOT NULL,
            movie_id varchar(255) NOT NULL,
            movie_caption varchar(1000),
            like int,
            dislike int,
            PRIMARY KEY (id)
            );
"""
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_movie(self,id: int,movie_id: str, movie_caption: str = None, like: int = 0, dislike: int = 0):

        
        sql = """
        INSERT INTO Movies(id,movie_id, movie_caption, like, dislike) VALUES(?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, movie_id, movie_caption, like, dislike), commit=True)

    def select_all_movies(self):
        sql = """
        SELECT * FROM Movies
        """
        return self.execute(sql, fetchall=True)

    def select_movie(self, **kwargs):
        sql = "SELECT * FROM Movies WHERE "
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)
    
    def select_id(self):
        sql = "SELECT id FROM Movies;"

        return self.execute(sql, fetchall=True)

    def count_movies(self):
        return self.execute("SELECT COUNT(*) FROM Movies;", fetchone=True)
    

    def update_top(self, like, id):

        sql = f"""
        UPDATE Movies SET like=? WHERE id=?
        """
        return self.execute(sql, parameters=(like, id), commit=True)

    def last_movie(self):
        return self.execute("SELECT * FROM Movies ORDER BY id DESC LIMIT 1;", fetchone=True)
    
    def get_movie_info(self, id):
        sql = f"""
            SELECT * FROM Movies WHERE id=?
        """
        return self.execute(sql, parameters=(id,), fetchone=True)
    
    def del_movie(self, id):
        sql = f"""
            DELETE FROM Movies WHERE id = ?
        """
        return self.execute(sql, parameters=(id,), commit=True)
    
    def update_like(self, like, id):

        sql = f"""
        UPDATE Movies SET like=? WHERE id=?
        """
        return self.execute(sql, parameters=(like, id), commit=True)
    
    def top_movies(self):

        sql = f"""
            SELECT movie_caption, like FROM Movies ORDER BY like DESC LIMIT 5;
        """

        return self.execute(sql, fetchall=True)



def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")