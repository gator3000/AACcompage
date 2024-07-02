import mysql.connector
import sys

class tools:
    def __init__(self):
        pass

    def write_log(domain = "TESTING", content = "", file = "timeline.log") -> None:
        print(log_now(domain.upper() + " " + content.capitalize(), mountharg="int"), file=open(file, "a"))

    def log_now(log:str=None, mountharg:str="str") -> str:
        date = str(datetime.date.today()).split("-")
        months = ["Unk", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        day = date[2]
        month = months[int(date[1])] if mountharg == "str" else date[1]
        year = date[0]
        date = "/".join([day,month,year])
        hour = str(datetime.datetime.now())[11:19]
        return f"[{date}:{hour}] " + ( log if log is not None else "" )


class Connexion:
    def __init__(self, host, user, mdp, db, init):
        self.host = host
        self.user = user
        self.password = mdp
        self.database = db
        self.init = init
        try:
            self.connexion = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
            self.cursor = self.connexion.cursor()
            self.init(self)
            tools.write_log("CONNECTING", f"to database {self.database} as {self.user}@{self.host}", file="db.log")
        except Exception as e:
            tools.write_log("FAILED TO CONNECT", f"to database {self.database} as {self.user}@{self.host} due to {e}", file="db.log")
            self.testing = True
        else:
            tools.write_log("CONNECTED", f"to database without errors!", file="db.log")
            self.testing = False
    def close(self):
        if self.connexion:
            try:
                self.connexion.close()
            except Exception as e:
                tools.write_log("CLOSING CONNECTION FAILED", f"with database {self.database} as {self.user}@{self.host}", file="db.log")
            else:
                tools.write_log("CONNECTION CLOSED", f"with database without errors!", file="db.log")
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
                tools.write_log("OPERATING", f"Creation worked without errors !", file="db.log")
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
                tools.write_log("OPERATING", f"Selection worked without errors !", file="db.log")
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
                tools.write_log("OPERATING", f"Insertion worked without errors !", file="db.log")
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
                tools.write_log("OPERATING", f"Deletion worked without errors !", file="db.log")
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
                tools.write_log("OPERATING", f"Updating field worked without errors !", file="db.log")
        else:
            print("This function is not available in testing mode")


