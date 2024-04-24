import cherrypy as cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
import tools
import datetime
import time
from connexion_db import Connexion
# import json



def E404(**kwargs):
    return "<img src='./static/assets/404.jpg' alt='Error 404 Page Not Found' style='min-height: 100%;width: 100%;height: auto;position: fixed;top: 0;left: 0;'/>"
def E500(**kwargs):
    return "<img src='./static/assets/500.jpg' alt='Error 500 Internal Server Error' style='min-height: 100%;width: 100%;height: auto;position: fixed;top: 0;left: 0;'/>"

class Website(object):
    def __init__(self):
        self.ANNONYMOUS = tools.User("Annonymous", -5, "user")
        self.lookup = TemplateLookup(directories=['static/templates'], input_encoding='utf-8', module_directory='static/tmp/mako_modules')
        try:
            print(tools.log_now("DATABASE starting connexion"))
            self.connexion=Connexion()
        except Exception as e:
            print(e)
            tools.write_log("DATABASE", "connexion failed")
            raise ConnectionError(tools.log_now("DATABASE connexion ERROR"))
        finally:
            print(tools.log_now("DATABASE connected"))
            tools.write_log("DATABASE", "200 connexion made")
            print(tools.log_now("DATABASE initialized"))




    @cherrypy.expose
    def index(self, **kwargs):
        mytemplate = self.lookup.get_template("index.html")
        return mytemplate.render(myPageName="Acceuil")
    
    @cherrypy.expose
    def driving_schools(self, **kwargs):
        mytemplate = self.lookup.get_template("driving-schools.html")
        pylistofds = self.connexion.SELECT("*", "drivingschools")
        listofds = tools.pylistofdstohtml(pylistofds)
        return mytemplate.render(myPageName="Auto-Écoles", drivingschools=listofds)


if __name__ == "__main__":
    # port 16384
    tools.write_log("SERVER", "starting")
    cherrypy.config.update({'error_page.404': E404, 'error_page.500': E500})
    WEBSITE = Website()
    cherrypy.quickstart(WEBSITE, config="conf.ini")
    tools.write_log("SERVER", "closed")
    WEBSITE.connexion.close()
    tools.write_log("DATABASE", "disconected")