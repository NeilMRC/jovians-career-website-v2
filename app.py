# This is the first file of the project 17/02/2023
# Modified to V2 on 21/02/2023
from flask import Flask, render_template,jsonify,request
from database import get_jobs_from_db, load_job_from_db, add_application_to_db

app = Flask(__name__)
Company="Camel"



@app.route("/")
def hello_world():
  jobs = get_jobs_from_db()
  return render_template("home.html",
                        jobs=jobs, company_name=Company)
@app.route("/api/jobs")
def list_jobs():
  jobs=get_jobs_from_db()
  return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
  job = load_job_from_db(id)
  if not job:
    return "Not found",404
  return render_template("jobpage.html",job=job, company_name=Company)

@app.route("/job/<id>/apply", methods=['post'])
def apply_to_job(id):
  data=request.form
  job = load_job_from_db(id)
  add_application_to_db(id,data)
  return render_template('application_submitted.html', application=data, company_name=Company, job=job)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)

