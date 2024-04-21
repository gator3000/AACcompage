# User Configuration

user_db = "accompagnerbot"
password = "pakls!08ù"


# Database Configuration

db_host = "localhost"
database = "accompagne"


# Initialization
def init(connexion):
    connexion.cursor.execute("""
    CREATE TABLE drivingpupils
    ;
    """)
    connexion.cursor.execute("""
    CREATE TABLE drivingschools
    ;
    """)
