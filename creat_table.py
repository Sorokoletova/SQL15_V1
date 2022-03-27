import sqlite3
with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query_breed = """
            CREATE TABLE IF NOT EXISTS breed (
                id integer PRIMARY KEY AUTOINCREMENT,
                breed varchar(60) UNIQUE NOT NULL 
          )
        """
    query_color1 = """
            CREATE TABLE IF NOT EXISTS color1  (
                id integer PRIMARY KEY AUTOINCREMENT,
                color1 varchar(60) UNIQUE NOT NULL 
          )
        """
    query_color2 = """
                CREATE TABLE IF NOT EXISTS color2  (
                    id integer PRIMARY KEY AUTOINCREMENT,
                    color2 varchar(60) UNIQUE NOT NULL 
              )
            """

    query_subtype = """
            CREATE TABLE IF NOT EXISTS subtype (
                id integer PRIMARY KEY AUTOINCREMENT,
                outcome_subtype varchar(60) UNIQUE NOT NULL 
          )
       """
    query_condition = """
            CREATE TABLE IF NOT EXISTS outcome (
                id integer PRIMARY KEY AUTOINCREMENT,
                outcome_type varchar(100) UNIQUE NOT NULL 
           )
        """
    query_myanimals = """
            CREATE TABLE IF NOT EXISTS my_animals (
                index_animal integer PRIMARY KEY AUTOINCREMENT,
                animal_type varchar(40),  
                animal_id varchar(20) NOT NULL, 
                name_animal varchar(100),
                age_upon_outcome varchar(40),
                date_of_birth data ,
                outcome_month integer(2),
                outcome_year integer(4),
                breed varchar(100),
                color1 varchar(40),
                color2 varchar(40),
                outcome_subtype varchar(100),
                outcome_type varchar(100),
                idbreed integer, 
                idcolor1 integer, 
                idcolor2 integer, 
                idsubtype integer, 
                idoutcome integer, 
                FOREIGN KEY (idbreed) REFERENCES breed (id) ON DELETE CASCADE,
                FOREIGN KEY (idcolor1) REFERENCES colors1 (id) ON DELETE CASCADE,
                FOREIGN KEY (idcolor2) REFERENCES colors2 (id) ON DELETE CASCADE,
                FOREIGN KEY (idsubtype) REFERENCES subtype (id) ON DELETE CASCADE,
                FOREIGN KEY (idoutcome) REFERENCES outcome (id) ON DELETE CASCADE
           )      
         """

    cursor.execute(query_breed)
    cursor.execute(query_color1)
    cursor.execute(query_color2)
    cursor.execute(query_subtype)
    cursor.execute(query_condition)
    cursor.execute(query_myanimals)
