import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class Delete:
    def __init__(self):
        pass

    def GET(self, email): 
        datos = model_datos.select_email(email) 
        return render.delete(datos)
    
    def POST(self, email):
        formulario = web.input()
        email = formulario['email']
        model_datos.delete_datos(email)
        raise web.seeother('/')
