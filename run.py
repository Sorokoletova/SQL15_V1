import sqlite3
from flask import Flask
import json


def view_animals(itemid):
    with sqlite3.connect("animal.db") as connection:
        connection.row_factory = sqlite3.Row
        query = connection.execute(f"""
            SELECT my_animals.index_animal, my_animals.animal_type,my_animals.animal_id,my_animals.name_animal,
             my_animals.age_upon_outcome, my_animals.outcome_month, my_animals.outcome_year, 
             breed.breed,color1.color1,color2.color2, subtype.outcome_subtype,outcome.outcome_type
            FROM my_animals
            LEFT JOIN breed ON my_animals.idbreed = breed.id
            LEFT JOIN color1 ON my_animals.idcolor1 = color1.id
            LEFT JOIN color2 ON my_animals.idcolor2 = color2.id
            LEFT JOIN subtype ON my_animals.idsubtype = subtype.id
            LEFT JOIN outcome ON my_animals.idoutcome = outcome.id
            WHERE index_animal = '{itemid}'
        """).fetchall()
    for q in query:
        result = dict(q)
    return json.dumps(result, indent=4)


app = Flask(__name__)


@app.route('/<itemid>')
def page_animal(itemid):
    animal = view_animals(itemid)
    return animal


app.run()
