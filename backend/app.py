from flask import Flask, jsonify
from werkzeug.exceptions import default_exceptions
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

people = [{"name": "Hunter", "age": 21}, {"name": "Rishi", "age": 22}]

@app.route("/person")
def get_person():
    import random
    print random.randint(0,1)
    person = people[random.randint(0,1)]
    return jsonify(person)

if __name__ == '__main__':
        app.run(debug=True)
