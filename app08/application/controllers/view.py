import web
import application.models.model_datos as model_datos

render = web.template.render('application/views/', base='master')

class View:
    def __init__(self):
        pass

    def GET(self, email):  
        datos = model_datos.select_email(email)
        return render.view(datos)
