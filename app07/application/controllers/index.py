import web

render = web.template.render('application/views/', base='master')

class Index:
    def __init__(self):
        pass

    def GET(self):       
        return render.index()

    def POST(self):
        formulario = web.input()
        print formulario.exampleInputEmail1
        print formulario.exampleInputPassword1
        return formulario.exampleInputEmail1 + ":" + formulario.exampleInputPassword1
        


