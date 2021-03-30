import sqlite3
from model import Users

# conn = sqlite3.connect('cinema.db')

# c = conn.cursor()

# c.execute("""CREATE TABLE User(
#             id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
#             nom           TEXT NOT NULL ,
#             prenom        TEXT NOT NULL ,
#             poste         TEXT NOT NULL ,
#             username      TEXT NOT NULL ,
#             password      TEXT NOT NULL ,
#             date_debut    NUMERIC NOT NULL ,
#             date_fin      NUMERIC NOT NULL ,
#             admin         INTEGER NOT NULL
#         )""")

def add_user(conn, c, user):
    with conn:
        c.execute("INSERT INTO User (nom,prenom,poste,username,password,date_debut,date_fin,admin) VALUES (:nom, :prenom, :poste, :username, :password, :date_debut, :date_fin, :admin)", {'nom': user.nom, 'prenom': user.prenom, 'poste': user.poste, 'username': user.username, 'password': user.password, 'date_debut': user.date_debut, 'date_fin': user.date_fin, 'admin': user.admin})


def read_users(c):
    c.execute("SELECT * FROM User")
    return c.fetchall()

def read_one(c, prenom):
    c.execute("SELECT * FROM User WHERE prenom=:prenom", {'prenom': prenom})
    return c.fetchall()

def auth(c, username, password):
    c.execute("SELECT * FROM User WHERE username=:username AND password=:password", {'username': username, 'password': password})
    return c.fetchall()


def update_user(conn, c, user, id):
    with conn:
        c.execute("""UPDATE User SET nom = :nom, prenom = :prenom, poste = :poste, username = :username, password = :password, date_debut = :date_debut, date_fin = :date_fin, admin = :admin
                    WHERE id = :id""",
                  {'nom': user.nom, 'prenom': user.prenom, 'poste': user.poste, 'username': user.username, 'password': user.password, 'date_debut': user.date_debut, 'date_fin': user.date_fin, 'admin': user.admin, 'id': id})


def delete_user(conn, c, id):
    with conn:
        c.execute("DELETE from User WHERE id = :id",
                  {'id': id})

# conn.close()


