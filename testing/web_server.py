import cherrypy
import random
class AdLib:
    @cherrypy.expose
    def index(self):
        cherrypy.response.headers['Content-Type'] = 'text/html'
        career_list = ["barista", "astronaut", "doctor", "nurse",
         "musician", "teacher", "application developer"]
        career = random.choice(career_list)
        result = "<h1>Random Career Generator</h1>"
        result += f"<p>When I graduate, I want to be a(n) {career}!</p>"
        return result
cherrypy.quickstart(AdLib())