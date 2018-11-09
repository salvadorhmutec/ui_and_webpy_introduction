import web
        
urls = (
    '/', 'index',
    '/acercade', 'acercade',
)

render = web.template.render('templates/')


class index: 
    def GET(self):       
        return render.index()

class acercade: 
    def GET(self):       
        return render.acercade()

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
