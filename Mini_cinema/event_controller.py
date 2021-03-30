import sqlite3
from model import Evenements

# conn = sqlite3.connect('mairie.db')

# c = conn.cursor()

# c.execute("""CREATE TABLE Evenement(
#             id_event            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
#             type_event    TEXT NOT NULL ,
#             nom_event     TEXT NOT NULL ,
#             date_event    NUMERIC NOT NULL ,
#             id_User       INTEGER NOT NULL

#             ,CONSTRAINT Evenement_User_FK FOREIGN KEY (id_User) REFERENCES User(id_event)
#             )""")

def add_event(conn, c, event):
    with conn:
        c.execute("INSERT INTO Evenement (type_event,nom_event,date_event,id_User) VALUES (:type_event, :nom_event, :date_event, :id_User)", {'type_event': event.type_event, 'nom_event': event.nom_event, 'date_event': event.date_event, 'id_User': event.id_User})


def read_events(c):
    c.execute("SELECT id_event, type_event, nom_event, date_event, nom FROM Evenement INNER JOIN User ON User.id = Evenement.id_User")
    return c.fetchall()

# def read_events(c):
#     c.execute("SELECT * FROM Evenement")
#     return c.fetchall()

def read_one(c, event):
    c.execute("SELECT * FROM Evenement WHERE type_event=:type_event", {'type_event': event})
    return c.fetchall()


def update_event(conn, c, event, id_event):
    with conn:
        c.execute("""UPDATE Evenement SET type_event = :type_event, nom_event = :nom_event, date_event = :date_event, id_User = :id_User
                    WHERE id_event = :id_event""",
                  {'type_event': event.type_event, 'nom_event': event.nom_event, 'date_event': event.date_event, 'id_User': event.id_User, 'id_event': id_event})


def delete_event(conn, c, id_event):
    with conn:
        c.execute("DELETE from Evenement WHERE id_event = :id_event",
                  {'id_event': id_event})

# conn.close()