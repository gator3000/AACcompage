# User Configuration

user_db = "aaccompagnerbot"
password = "mke5+$z"


# Database Configuration

db_host = "localhost"
database = "AACcompagne"


# Initialization
def init(connexion):
    try:
        connexion.cursor.execute("""
        CREATE TABLE drivingschools (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            description VARCHAR(1000),
            email VARCHAR(50) NOT NULL,
            adress VARCHAR(256) NOT NULL,
            number VARCHAR(10) NOT NULL,
            password VARCHAR(256) NOT NULL
        );
        """)
    except:
        pass
    try:
        connexion.cursor.execute("""
        CREATE TABLE drivingteachers (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(30) NOT NULL,
            email VARCHAR(50) NOT NULL,
            password VARCHAR(256) NOT NULL,
            drivingschool INT NOT NULL,
            FOREIGN KEY(drivingschool) REFERENCES drivingschools (id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """)
    except:
        pass
    try:
        connexion.cursor.execute("""
        CREATE TABLE drivingpupils (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            firstname VARCHAR(20) NOT NULL,
            lastname VARCHAR(30) NOT NULL,
            comment VARCHAR(200),
            email VARCHAR(50) NOT NULL,
            password VARCHAR(256) NOT NULL,
            drivingschool INT NOT NULL,
            FOREIGN KEY(drivingschool) REFERENCES drivingschools (id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """)
    except:
        pass
    try:
        connexion.cursor.execute("""
        CREATE TABLE routes (
            id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
            pupil INT NOT NULL,
            FOREIGN KEY(pupil) REFERENCES drivingpupils (id) ON DELETE CASCADE ON UPDATE CASCADE,
            title VARCHAR(30) NOT NULL,
            date VARCHAR(8) NOT NULL,
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
    except:
        pass
