from sqlalchemy import create_engine, text
import os

db_connection_string=os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_connection_string,
                      connect_args={
                        "ssl":{
                          "ssl_ca":"/etc/ssl/cert.pem"
                        }
                      }
                      )
def get_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    result_all = result.all()
    jobs=[]
    for row in result_all:
      jobs.append(row._asdict())
    return jobs

def load_job_from_db(id):
  with engine.connect() as conn:
    t=text('select * from jobs where jobs.id={}'.format(id))
    result = conn.execute(t)
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  result_all=result.all()
  first_result=result_all[0]
  first_result_dict=result_all[0]._asdict()
 

result_dicts=[]
for row in result_all:
  result_dicts.append(row._asdict())
print(result_dicts)