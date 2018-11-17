import web
        
urls = (
    '/', 'application.controllers.index.Index',
    '/insert', 'application.controllers.insert.Insert'
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
