import random
import hashlib
import datetime

class User:
    def __init__(self, name, myid, mytype):
        self.name = name
        self.id = myid
        self.type = mytype
    def __eq__(self, other) -> bool:
        return True if self.id == other.id else False
    def __repr__(self) -> str:
        return self.name
        

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

def hashme(arg) -> str:
    return hashlib.sha256(arg.encode()).hexdigest()

def are_all_empty(*args) -> bool:
    for arg in args:
        if arg!="":
            return False
    return True

def are_empty(*args) -> bool:
    for arg in args:
        if arg=="":
            return True
    return False

def are_all_in(*args, iterable) -> bool:
    for arg in args:
        if arg not in iterable:
            return False
    return True

    

def pylist_tohtml(arg:list) -> str:
    result = list()
    openlist = "<li>"
    closelist = "</li>"
    for item in arg:
        result.append(openlist)
        result.append(item)
        result.append(closelist)
    return "".join(result)

# def sqlmessages_tohtml(arg, me) -> str:
#     result = list()
#     for e in arg:
#         author = e[0]
#         content = e[1]
#         me2 = ".me" if e[0] == me else ""
#         result.append(f'<span class="message{me2}">')
#         result.append(f'<p><b>{author}</b></p>')
#         result.append(f'<p class="message-content{me2}">{content}</p>')
#         result.append('</span>')
#     return "".join(result)











def myrand():
    return random.randint(0,10)
