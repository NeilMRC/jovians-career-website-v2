# This is the first file of the project 17/02/2023
from flask import Flask

app = Flask(__name__)
print("from the app.")
@app.route("/")
def hello_world():
  return "<p>Hello stinky world!</p>"


if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)