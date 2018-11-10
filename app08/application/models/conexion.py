import web

db_host = 'localhost'
db_name = 'base_demo'
db_user = 'kuorra'
db_pw = 'kuorra.2018'
db_port = 3308

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw,
    port = db_port
    )


def get_all_datos():
    try:
        return db.select('datos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None
