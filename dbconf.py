# User Configuration

user_db = "accompagnerbot"
password = "pakls!08ù"


# Database Configuration

db_host = "localhost"
database = "accompagne"


# Initialization
def init(connexion):
    connexion.cursor.execute("""
    CREATE TABLE drivingschools (
        id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name varchar(50),
        email varchar(50),
        password varchar(256),
        adress varchar(256),
    )
    ;
    """)
    connexion.cursor.execute("""
    CREATE TABLE drivingteachers (
        id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        firstname varchar(20),
        lastname varchar(30),
        email varchar(50),
        password varchar(256)
        drivingschool int,
        FOREIGN KEY(drivingschool) REFERENCES drivingschools (id)
    )
    ;
    """)
    connexion.cursor.execute("""
    CREATE TABLE drivingpupils (
        id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        firstname varchar(20),
        lastname varchar(30),
        email varchar(50),
        password varchar(256)
        drivingschool int,
        FOREIGN KEY(drivingschool) REFERENCES drivingschools (id)
    )
    ;
    """)
    connexion.cursor.execute("""
    CREATE TABLE route (
        id int PRIMARY KEY NOT NULL AUTO_INCREMENT,
        pupil int,
        FOREIGN KEY(pupil) REFERENCES pupil (id)
        title varchar(30),
        lenght float(5),
        departure varchar(100),
        arrival varchar(100),
        time varchar(5),
        night bool,
        city bool,
        road bool,
        highway bool,
        u-turn int,
        r-parallel int,
        l-parallel int,
        r-battle int,
        f-battle int,
        r-diagonalpark int,
        l-diagonalpark int
    )
    ;
    """)
