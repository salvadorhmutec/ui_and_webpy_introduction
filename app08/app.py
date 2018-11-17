import web
        
urls = (
    '/', 'application.controllers.index.Index',
    '/insert', 'application.controllers.insert.Insert',
    '/update/(.*)', 'application.controllers.update.Update',
    '/delete/(.*)', 'application.controllers.delete.Delete',
    '/view/(.*)', 'application.controllers.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
