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


def select_datos():
    try:
        return db.select('datos')
    except Exception as e:
        print "Model select_datos Error {}".format(e.args)
        print "Model select_datos Message {}".format(e.message)
        return None

def select_email(email):
    try:
        return db.select('datos',where='email=$email', vars=locals())[0]
    except Exception as e:
        print "Model select_datos Error {}".format(e.args)
        print "Model select_datos Message {}".format(e.message)
        return None

def insert_datos(email, password):
    try:
        return db.insert('datos', email=email,password=password)
    except Exception as e:
        print "Model insert_datos Error {}".format(e.args)
        print "Model insert_datos Message {}".format(e.message)
        return None

def delete_datos(email):
    try:
        return db.delete('datos', where='email=$email',vars=locals())
    except Exception as e:
        print "Model insert_datos Error {}".format(e.args)
        print "Model insert_datos Message {}".format(e.message)
        return None

def update_datos(email, password):
    try:
        return db.update('datos', 
            email=email,
            password=password, 
            where='email=$email',
            vars=locals())
    except Exception as e:
        print "Model insert_datos Error {}".format(e.args)
        print "Model insert_datos Message {}".format(e.message)
        return None
