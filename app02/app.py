import web
        
urls = (
    '/', 'Index',
    '/acercade', 'Acercade',
)

render = web.template.render('templates/')

class Index: 
    def GET(self):
        datos =['Salvador','salvadorhm@gmail.com']     
        return render.index(datos)

class Acercade: 
    def GET(self):
        nombre = "Salvador"
        email = "salvadorhm@email.com"       
        return render.acercade(nombre, email)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
