import web
        
urls = (
    '/', 'application.controllers.index.Indexs',
    '/acercade', 'application.controllers.acercade.Acercade',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
