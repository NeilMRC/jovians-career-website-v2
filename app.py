# This is the first file of the project 17/02/2023
# Modified to V2 on 21/02/2023
from flask import Flask, render_template,jsonify

app = Flask(__name__)
Company="Camel"
JOBS=[
  {
    'id':1,
    'title':'Data Analyst',
    'location': 'Bangaluru, India',
    'salary': 'Rs: 10,00,000'
  },
  {
    'id':2,
    'title':'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs: 15,00,000'
  },
  {
    'id':3,
    'title':'Frontend Engineer',
    'location': 'Remote',
    #'salary': 'Rs: 12,00,000'
  },
  {
    'id':4,
    'title':'Backend Engineer',
    'location': 'Remote',
    'salary': '$150,000.00'
  },
  
]



@app.route("/")
def hello_world():
  return render_template("home.html",
                        jobs=JOBS, company_name=Company)
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

