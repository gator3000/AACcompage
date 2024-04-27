import cherrypy as cherrypy
from mako.template import Template
from mako.lookup import TemplateLookup
import tools
import datetime
import time
from connexion_db import Connexion



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
        if "show-teachers" in kwargs:
            current_id = kwargs["show-teachers"]
            id_list = [int(x[0]) for x in self.connexion.SELECT("id", "drivingschools")]
            # print(id_list)
            # print(current_id)
            # print(current_id in id_list)
            #if current_id in id_list:
            school = self.connexion.SELECT("id, name, adress, email, number", "drivingschools", f"id = {current_id}")[0]
            name = school[1]
            mydteachers = self.connexion.SELECT("firstname, lastname, email", "drivingteachers", f"drivingschool = {current_id}")
            text = tools.format_ds_page(school, mydteachers)
            return mytemplate.render(myPageName=name, drivingschools=text)
        pylistofds = self.connexion.SELECT("name, adress, email, number, id", "drivingschools")
        listofds = tools.pylistofdstohtml(pylistofds)
        return mytemplate.render(myPageName="Auto-Écoles", drivingschools=listofds)

    @cherrypy.expose
    def adding_driving_school(self, **kwargs):
        mytemplate = self.lookup.get_template("adding-driving-school.html")
        return mytemplate.render(myPageName="Ajouter Votre Entreprise", myerror="")

    @cherrypy.expose
    def adding_new_driving_school(self, **kwargs):
        # INSERT INTO drivingschools (name, adress, email, number, password) VALUES ("CAR'rément Permis",  "47 Rue Victor Hugo à Villefranche", "carrementpermis@gmail.com", "0481480203", "835d6dc88b708bc646d6db82c853ef4182fabbd4a8de59c213f2b5ab3ae7d9be");
        if tools.are_all_in("name", "adress", "email", "number", "password", "retyped-password", iterable=kwargs):
            if not tools.are_empty(kwargs["name"], kwargs["adress"], kwargs["email"], kwargs["number"], kwargs["password"], kwargs["retyped-password"]):
                if len(kwargs["number"]) == 10 and kwargs["number"][0] == "0" and " " not in kwargs["number"]:
                    if len(kwargs["name"]) < 256:
                        if len(kwargs["adress"]) < 256:
                            if kwargs["password"] == kwargs["retyped-password"]:
                                self.connexion.INSERT("drivingschools", ("name", "adress", "email", "number", "password"), f""" ("{kwargs['name']}", "{kwargs['adress']}", "{kwargs['email']}", "{kwargs['number']}", "{tools.hashme(kwargs['password'])}" )""")
                                raise cherrypy.HTTPRedirect("/driving_schools")
                            else:myerror = "Le mot de passe n'est pas le même que celui reécris."
                        else:myerror = "L'adresse de votre Auto-École ne doit pas faire plus de 256 charactères. Essayez de le racourcir."
                    else:myerror = "Le nom de votre entreprise ne doit pas faire plus de 256 charactères."
                else:myerror = "Le numéro saisis n'est pas du bon format (10 chiffres commançant par '0' sans espaces, par exemple : 0123456789)."
            else:myerror = "Remplisez bien tous les champs marqués d'une étoile (tous)."
        else:myerror = ""
        mytemplate = self.lookup.get_template("adding-driving-school.html")
        return mytemplate.render(myPageName="Ajouter Votre Entreprise", myerror=myerror)


    @cherrypy.expose
    def see_driving_school(self, **kwargs):
        mytemplate = self.lookup.get_template("see-driving-school.html")
        return mytemplate.render(myPageName=name, mycontent=content)

if __name__ == "__main__":
    # port 16384
    tools.write_log("SERVER", "starting")
    cherrypy.config.update({'error_page.404': E404, 'error_page.500': E500})
    WEBSITE = Website()
    cherrypy.quickstart(WEBSITE, config="conf.ini")
    tools.write_log("SERVER", "closed")
    WEBSITE.connexion.close()
    tools.write_log("DATABASE", "disconected")