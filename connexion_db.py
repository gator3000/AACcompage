import mysql.connector
import sys
import dbconf as config

class Connexion:
    def __init__(self, host=config.db_host, user=config.user_db, mdp=config.password, db=config.database):
        self.host = host
        self.user = user
        self.password = mdp
        self.database = db
        try:
            self.connexion = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.connexion.cursor()
            config.init(self)
        except Exception as e:
            print(e)
            self.testing = True
        else:
            self.testing = False
    def close(self):
        if self.connexion:
            self.connexion.close()
    def __repr__(self):
        return f"Connexion to {self.database}@{self.host} under {self.user}"
    
    #* SQL Knowed Commands
    def CREATE(self, typeof:str, name:str, champ:tuple, primarykey:tuple = None):
        if not self.testing:
            try:
                cmd = f"""CREATE {typeof.upper()} {name} {"".join([e if e != "'" else "" for e in str(tableFields)])}""" + f""" PIMARY KEY {"".join([e if e != "'" else "" for e in str(primarykey)])}""" if primarykey is not None else "" + ";"
                self.cursor.execute(cmd)
            except Exception as e:
                self.connexion.rollback()
                print(e)
                return f"<{typeof.capitalize()}CreationError>"
            finally:
                self.connexion.commit()
        else:
            print("This function is not available in testing mode")

    def SELECT(self, what:str, fromarg:str, where:str=None, join:str=None, orderby:str=None):
        if not self.testing:
            try:
                cmd = f"""SELECT {what} FROM {fromarg}""" + (f""" WHERE {where}""" if where is not None else str()) + (f""" JOIN {join}""" if join is not None else str()) + (f""" ORDER BY {orderby}""" if orderby is not None else str()) + ";"
                print(cmd)
                self.cursor.execute(cmd)
            except Exception as e:
                print(e)
                return "<SelectionError>"
            finally:
                return self.cursor.fetchall()
        else:
            print("This function is not available in testing mode")

    def INSERT(self, table:str, tableFields:tuple, values:str):
        if not self.testing:
            try:
                cmd = f"""INSERT INTO {table} {"".join([e if e != "'" else "" for e in str(tableFields)])} VALUES {values};"""
                self.cursor.execute(cmd)
            except Exception as e:
                self.connexion.rollback()
                print(e)
                return "<InsertionError>"
            finally:
                self.connexion.commit()
        else:
            print("This function is not available in testing mode")

    def DELETE(self, table:str, where:str):
        if not self.testing:
            try:
                cmd = f"""DELETE {table} WHERE {where};"""
                self.cursor.execute(cmd)
            except Exception as e:
                self.connexion.rollback()
                print(e)
                return "<DeletionError>"
            finally:
                self.connexion.commit()
        else:
            print("This function is not available in testing mode")
    
    def UPDATE(self, table:str, what:str, where:str):
        if not self.testing:
            try:
                cmd = f"""UPDATE {table} SET {what} WHERE {where};"""
                self.cursor.execute(cmd)
            except Exception as e:
                self.connexion.rollback()
                print(e)
                return "<UpdatingError>"
            finally:
                self.connexion.commit()
        else:
            print("This function is not available in testing mode")


