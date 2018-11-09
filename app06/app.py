import web
        
urls = (
    '/', 'application.controllers.index.Index'
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
