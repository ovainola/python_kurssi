import cherrypy

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return "".join(open("index.html", "r"))

if __name__ == '__main__':
   cherrypy.quickstart(HelloWorld())