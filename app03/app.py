import web
        
urls = (
    '/', 'index'
)

render = web.template.render('templates/', base='master')

class index: 
    def GET(self):       
        return render.index()

if __name__ == "__main__":
    web.config.debug = False
    app = web.application(urls, globals())
    app.run()
