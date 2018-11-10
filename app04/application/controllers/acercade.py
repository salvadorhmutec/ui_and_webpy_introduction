import web

render = web.template.render('application/views/', base='master')

class Acercade:
    def __init__(self):
        pass

    def GET(self):       
        nombre = "Salvador"
        email = "salvadorhm@gmail.com"    
        return render.acercade(nombre, email)
