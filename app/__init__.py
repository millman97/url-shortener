from flask import Flask
from flask_cors import CORS

# init app
app = Flask(__name__)
CORS(app)

from app import routes, database, controllers, models 

if __name__ == "__main__":
    app.run(debug=True)
