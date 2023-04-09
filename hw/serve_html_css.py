import cherrypy
import random
import os

"""class HTML:
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = 'text/html'

        career_list = ['programmer', 'dentist', 'politician', 'dictator',
                       'teacher', 'musician', 'application developer',
                       'doctor', 'nurse', 'physician', 'cancer patient',
                       'orphan']
        career = random.choice(career_list)

        result = "<h1>Random Career Generator</h1>"

        result += f"<p>When I grow up I want to be a(n) {career}!</p>"

        return result"""
# cherrypy.quickstart(HTML())

import os
import cherrypy
import random

# Serve static files out of the web subdirectory
PATH = os.path.abspath(os.path.dirname(__file__)) + "/web"


class WebServer(object):
    @cherrypy.expose
    def index(self):
        # Set the media type
        cherrypy.response.headers['Content-Type'] = 'text/html'
        random_number = random.randrange(1, 101)
        result = "<html>"
        result += "<head>"
        result += "<link rel='stylesheet' type='text/css' href='style.css'>"
        result += "</head>"
        result += "<body>"
        result += "<h1>My Page</h1>"
        result += f"<p>My random number: {random_number}</p>"
        result += "</body>"
        result += "</html>"

        return result


config = {
        '/': {
                'tools.staticdir.on': True,
                'tools.staticdir.dir': PATH,
            },
    }

cherrypy.quickstart(WebServer(), config=config)