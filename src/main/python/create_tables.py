from database import HealthDatabase

create_water_sql = """ CREATE TABLE IF NOT EXISTS water_entries (
                                    id integer PRIMARY KEY,
                                    fluid_oz INTEGER NOT NULL,
                                    timestamp INTEGER NOT NULL
                                ); """


def create_water_table():
    db = HealthDatabase()
    db.create_table(create_water_sql)

create_water_table()