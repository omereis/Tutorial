from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://bumps:bumps_dba@NCNR-R9nano.campus.nist.gov:3306/bumps_db')
metadata = MetaData ()

connection = engine.connect()

res = connection.execute('select max(job_id) from t_bumps_jobs;')
for row in res:
    id = row.values()[0]
    print ('{}'.format(row))

sql = 'insert into t_bumps_jobs(job_id) values ({});'.format(id + 1)
res = connection.execute(sql)
print ('New id: {}'.format(id))

connection.close()
