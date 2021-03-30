
class Users:
    def __init__(self, nom, prenom, poste, username, password, date_debut, date_fin, admin = 0):
        self.nom = nom
        self.prenom = prenom
        self.poste = poste
        self.username = username
        self.password = password
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.admin = admin

class Evenements:
    def __init__(self, type_event, nom_event, date_event, id_User):
        self.type_event = type_event
        self.nom_event = nom_event
        self.date_event = date_event
        self.id_User = id_User
