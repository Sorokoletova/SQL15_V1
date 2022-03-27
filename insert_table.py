import sqlite3
with sqlite3.connect("animal.db") as connection:
    cursor = connection.cursor()
    query_breed = """
               INSERT INTO breed (breed)
               SELECT DISTINCT breed
               FROM animals
               WHERE breed!=''
        """
    query_color1 = """
               INSERT INTO color1 (color1)
               SELECT DISTINCT TRIM(color1)
               FROM animals
               WHERE color1!=''
        """
    query_color2 = """
                   INSERT INTO color2 (color2)
                   SELECT DISTINCT TRIM(color2)
                   FROM animals
                   WHERE color2!=''
            """
    query_subtype = """
                       INSERT INTO subtype (outcome_subtype)
                       SELECT DISTINCT outcome_subtype
                       FROM animals
                       WHERE outcome_subtype!=''
                """
    query_condition = """
                        INSERT INTO outcome (outcome_type)
                        SELECT DISTINCT outcome_type
                        FROM animals
                        WHERE outcome_type!=''
                   """
    query_myanimals = """
                        INSERT INTO my_animals (index_animal, animal_type, animal_id, name_animal, age_upon_outcome, 
                        date_of_birth, outcome_month, outcome_year,breed, color1, color2, outcome_subtype, outcome_type)
                        SELECT "index", animal_type, animal_id, name, age_upon_outcome, date_of_birth, outcome_month, outcome_year, breed, color1, color2, outcome_subtype, outcome_type
                        FROM animals                      
                    """
    cursor.execute(query_breed)
    cursor.execute(query_color1)
    cursor.execute(query_color2)
    cursor.execute(query_subtype)
    cursor.execute(query_condition)
    cursor.execute(query_myanimals)


with sqlite3.connect("animal.db") as connection:
     connection.row_factory = sqlite3.Row
     query = connection.execute("""
            SELECT *
            FROM outcome""").fetchall()
     for q in query:
        value = dict(q)
        connection.execute(f"""
        UPDATE my_animals
        SET idoutcome = {value["id"]}
        WHERE outcome_type = '{value["outcome_type"]}'
        """)
     query1 = connection.execute("""
        SELECT *
        FROM color1""").fetchall()
     for q in query1:
         value = dict(q)
         connection.execute(f"""
             UPDATE my_animals
             SET idcolor1 = {value["id"]}
             WHERE color1 = '{value["color1"]}'
             """)
     query2 = connection.execute("""
                      SELECT *
                      FROM color2""").fetchall()
     for q in query2:
         value = dict(q)
         connection.execute(f"""
                  UPDATE my_animals
                  SET idcolor2 = {value["id"]}
                  WHERE color2 = '{value["color2"]}'
                  """)
     query3 = connection.execute("""
                    SELECT *
                    FROM breed""").fetchall()
     for q in query3:
         value = dict(q)
         connection.execute(f"""
                       UPDATE my_animals
                       SET idbreed = {value["id"]}
                       WHERE breed = '{value["breed"]}'
                       """)
     query4 = connection.execute("""
                        SELECT *
                        FROM subtype""").fetchall()
     for q in query4:
         value = dict(q)
         connection.execute(f"""
                        UPDATE my_animals
                        SET idsubtype = {value["id"]}
                        WHERE outcome_subtype = '{value["outcome_subtype"]}'
                        """)

     query_dell = """
                    ALTER TABLE my_animals
                    DROP COLUMN breed                    
                    """
     query_dell1 = """
                    ALTER TABLE my_animals
                    DROP COLUMN color1                  
                        """
     query_dell2 = """
                    ALTER TABLE my_animals
                    DROP COLUMN color2 
                         """
     query_dell3 = """
                    ALTER TABLE my_animals
                    DROP COLUMN outcome_subtype 
                             """
     query_dell4 = """
                    ALTER TABLE my_animals
                    DROP COLUMN outcome_type 
                                 """

     cursor.execute(query_dell)
     cursor.execute(query_dell1)
     cursor.execute(query_dell2)
     cursor.execute(query_dell3)
     cursor.execute(query_dell4)