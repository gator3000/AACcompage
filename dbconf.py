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
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(256) NOT NULL,
        adress VARCHAR(256) NOT NULL
    );
    """)
    connexion.cursor.execute("""
    CREATE TABLE drivingteachers (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(30) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(256) NOT NULL,
        drivingschool INT NOT NULL,
        FOREIGN KEY(drivingschool) REFERENCES drivingschools (id)
    );
    """)
    connexion.cursor.execute("""
    CREATE TABLE drivingpupils (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        firstname VARCHAR(20) NOT NULL,
        lastname VARCHAR(30) NOT NULL,
        email VARCHAR(50) NOT NULL,
        password VARCHAR(256) NOT NULL,
        drivingschool INT NOT NULL,
        FOREIGN KEY(drivingschool) REFERENCES drivingschools (id)
    );
    """)
    connexion.cursor.execute("""
    CREATE TABLE route (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        pupil INT NOT NULL,
        FOREIGN KEY(pupil) REFERENCES drivingpupils (id),
        title VARCHAR(30) NOT NULL,
        lenght float(5) NOT NULL,
        departure VARCHAR(100),
        arrival VARCHAR(100),
        time VARCHAR(5),
        night bool NOT NULL,
        city bool NOT NULL,
        road bool NOT NULL,
        highway bool NOT NULL,
        u_turn INT NOT NULL,
        r_parallel INT NOT NULL,
        l_parallel INT NOT NULL,
        r_battle INT NOT NULL,
        f_battle INT NOT NULL,
        r_diagonalpark INT NOT NULL,
        l_diagonalpark INT NOT NULL
    );
    """)
