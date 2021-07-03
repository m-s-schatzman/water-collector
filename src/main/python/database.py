import sqlite3
import pathlib

from sqlite3 import Error

class HealthDatabase:

    def __init__(self):
        path = str(pathlib.Path().resolve())
        self.db_file = path + "/db/healthstats.db"
        self.conn = self.create_connection()

    def create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            return sqlite3.connect(self.db_file)
        except Error as e:
            raise e

    def close_connection(self):
        if self.conn:
            self.conn.close()
        else:
            raise Exception("Database connection not open. Cannot close.")


    def create_water_entry(self, water):
        """
        Create a new project into the projects table
        :param conn:
        :param project:
        :return: project id
        """
        sql = """INSERT INTO water_entries(fluid_oz,timestamp)
                VALUES({},{})""".format(water.glass_size_oz, water.unix_timestamp)
                
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        print(f"Water entry created.")
        return cur.lastrowid

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement
        :param conn: Connection object
        :param create_table_sql: a CREATE TABLE statement
        :return:
        """
        try:
            c = self.conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)
        
    def select_all_water_entries(self):
        """
        Query all rows in the water_entries table
        :param conn: the Connection object
        :return:
        """
        cur = self.conn.cursor()
        cur.execute("SELECT * FROM water_entries")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def query(self, query):
        cur = self.conn.cursor()
        cur.execute(query)
        
        return cur.fetchall()