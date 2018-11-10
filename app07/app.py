import web
        
urls = (
    '/', 'application.controllers.index.Index',
    '/datos/(.+)', 'application.controllers.datos.Datos'
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
