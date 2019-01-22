import web
        
urls = (
    '/', 'application.controllers.personas.index.Index',
    '/insert', 'application.controllers.personas.insert.Insert',
    '/update/(.*)', 'application.controllers.personas.update.Update',
    '/delete/(.*)', 'application.controllers.personas.delete.Delete',
    '/view/(.*)', 'application.controllers.personas.view.View',
)

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
