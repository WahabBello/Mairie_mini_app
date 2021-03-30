import sqlite3
import tkinter 
import tkinter.messagebox as box

from model import Evenements, Users
from user_controller import add_user, read_one, read_users, delete_user, update_user, auth
from event_controller import add_event, read_one, read_events, delete_event, update_event


# =========================
# BD connection
conn = sqlite3.connect('mairie.db')
c = conn.cursor()

# Des variables globales et reutilisables
code_couleur = "#76c6d0"
code_couleur2 = "#62a2aa"
code_couleur3 = "#995757"
font_valeur = ('Times New Roman',11,'normal') 
font_valeur2 = ('Times New Roman',12,'bold') 
event_id = None
user_id = None
user_actif = [("","","","","","","",0)]

# Les fonction du Gestion
# =========================

# <----CRUD EVENT

def event_selected(event):
    global event_id
    event_id = event[0]
    value_film.set(event[1]) 
    value_auteur.set(event[2]) 
    value_anim.set(event[3]) 
    value_debat.set(event[4])

def add_function():
    for key, value in dict_users.items():
        if value == value_debat.get():
            responsable = key
    
    if not responsable:
        box.showerror("Erreur", "Choissisez un responble")

    print(responsable)
    event = Evenements(value_film.get(), value_auteur.get(), value_anim.get(), responsable)
    add_event(conn, c, event)
    print("Fonction d'ajout")
    affiche_table(frame3)
    

def read_function():
    all_events = read_events(c)
    return all_events
    
def edit_function():
    for key, value in dict_users.items():
        if value == value_debat.get():
            responsable = key    
    if not value_film.get() and not responsable: 
        event = Evenements(value_film.get(), value_auteur.get(), value_anim.get(), responsable)
        update_event(conn, c, event, event_id)
        affiche_table(frame3)
    else:
        box.showerror("Erreur", "Selectionner un element puis modifier les champs souhaités")  
    # print("Fonction de modification")
        
def delete_function(id):
    # print(user_actif[0][-1])
    if user_actif[0][-1] == 1:
        delete_event(conn, c, id)
        affiche_table(frame3)
    else:
        box.showerror("Erreur", "Connectez vous en tant que admin")

def reset_function():
    value_film.set("")
    value_auteur.set("")
    value_anim.set("")
    value_debat.set("")
    print("Fonction Reinitialiser")
    affiche_table(frame3)

# ---->CRUD EVENT

# <----CRUD User


def event_selected_user(user):
        global user_id
        user_id = user[0]

        value_name.set(user[1])
        value_Firstname.set(user[2])
        value_poste.set(user[3])
        value_username.set(user[4])
        value_password.set(user[5])
        value_date_debut.set(user[6])
        value_date_fin.set(user[7])
        value_role.set(user[8])

def add_function_user():
        # pass
    if user_actif[0][-1] == 1:
        user = Users(value_name.get(), value_Firstname.get(), value_poste.get(), value_username.get(
        ), value_password.get(), value_date_debut.get(), value_date_fin.get(), value_role.get())
        add_user(conn, c, user)
        print("Fonction d'ajout")
        affiche_table_users(frame3_1)
    else:
        box.showerror("Erreur", "Connectez vous en tant que admin")


def read_function_user():
    # pass
    if user_actif[0][-1] == 1:
        all_users = read_users(c)
        return all_users
    else:
        box.showerror("Erreur", "Connectez vous en tant que admin")    
    # all_users = read_users(c)
    # return all_users

def edit_function_user():
    if user_actif[0][-1] == 1:
        user = Users(value_name.get(), value_Firstname.get(), value_poste.get(), value_username.get(
        ), value_password.get(), value_date_debut.get(), value_date_fin.get(), value_role.get())
        update_user(conn, c, user, user_id)
        affiche_table_users(frame3_1)
        print("Fonction de modification")
    else:
        box.showerror("Erreur", "Connectez vous en tant que admin")  

def delete_function_user(id):
    if user_actif[0][-1] == 1:
        delete_event(conn, c, id)
        affiche_table_users(frame3_1)
    else:
        box.showerror("Erreur", "Connectez vous en tant que admin")

def reset_function_user():
        value_name.set("")
        value_Firstname.set("")
        value_poste.set("")
        value_username.set("")
        value_password.set("")
        value_date_debut.set("")
        value_date_fin.set("")
        value_role.set(0)
        print("Fonction Reinitialiser")
        affiche_table_users(frame3_1)
# ---->CRUD User

# ---->Connexion User
def authentification():
    # global username_data
    # global password_data
    username = username_data.get()
    password = password_data.get()
    global user_actif
    user_actif = auth(c, username, password)
    # if(username == "admin" and password =="Admin02"):
    if(username == "" and password ==""):
        box.showinfo("Attention", "Veuillez remplir les champs")
    elif(user_actif):
        print("Connexion réuissie")
        affiche_fenetre()
    else:
        box.showerror("Erreur", "Mettez vos vrais identifiants")
        print("Connexion échouée")
# <----Connexion User

#---->Fonction affichages
def affiche_table(widget):
    # code for creating table
    all_events = read_events(c)
    total_rows = len(all_events)
    total_columns = len(all_events[0])
    for i in range(total_rows):
        for j in range(total_columns):
            label_type = tkinter.Label(widget, padx=5, font=font_valeur2, text="Id") 
            label_type.grid(row=0, column=0)   

            label_type = tkinter.Label(widget, padx=5, font=font_valeur2, text="Type") 
            label_type.grid(row=0, column=1)   

            label_nom = tkinter.Label(widget, padx=5, font=font_valeur2, text="Nom") 
            label_nom.grid(row=0, column=2) 

            label_titre = tkinter.Label(widget, padx=5, font=font_valeur2, text="Date") 
            label_titre.grid(row=0, column=3) 

            label_responsable = tkinter.Label(widget, padx=5, font=font_valeur2, text="Responsable") 
            label_responsable.grid(row=0, column=4) 

            m = tkinter.Button(widget, text="Selectionner", command=lambda i=i: event_selected(all_events[i]))
            m.grid(row=i+1, column=total_columns)
            # d = tkinter.Button(widget, text="Delete", command=lambda i=i: delete_function(all_events[i][0]))
            # d.grid(row=i+1, column=total_columns+1)
            e = tkinter.Label(widget, bd=2, padx=5, pady=5, font=font_valeur, wraplength= 200, text=all_events[i][j])
            e.grid(row=i+1, column=j)

def affiche_table_users(widget):
    # code for creating table
    all_users = read_users(c)
    total_rows = len(all_users)
    total_columns = len(all_users[0])
    for i in range(total_rows):
        for j in range(total_columns):
            label_type = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Id")
            label_type.grid(row=0, column=0)

            label_type = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Nom")
            label_type.grid(row=0, column=1)

            label_nom = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Prenom")
            label_nom.grid(row=0, column=2)

            label_titre = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Poste")
            label_titre.grid(row=0, column=3)

            label_responsable = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Username")
            label_responsable.grid(row=0, column=4)

            label_responsable = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Password")
            label_responsable.grid(row=0, column=5)

            label_responsable = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Date de début")
            label_responsable.grid(row=0, column=6)

            label_responsable = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Date de fin")
            label_responsable.grid(row=0, column=7)

            label_responsable = tkinter.Label(
                widget, padx=5, font=font_valeur2, text="Admin")
            label_responsable.grid(row=0, column=8)
            if user_actif[0][-1]:
                m = tkinter.Button(widget, text="Selectionner",
                                    command=lambda i=i: event_selected_user(all_users[i]))
                m.grid(row=i+1, column=total_columns)
                # d = tkinter.Button(
                #     widget, text="Delete", command=lambda i=i: delete_function_user(all_users[i][0]))
                # d.grid(row=i+1, column=total_columns+1)

                if j == 5:
                    e = tkinter.Label(widget, bd=2, padx=5, pady=5,
                                        font=font_valeur, wraplength=200, text="*******")
                elif j == 8:
                    value = 'Oui' if all_users[i][j] == 1 else 'Non'
                    e = tkinter.Label(widget, bd=2, padx=5, pady=5,
                                        font=font_valeur, wraplength=200, text=value)
                else:
                    e = tkinter.Label(widget, bd=2, padx=5, pady=5,
                                        font=font_valeur, wraplength=200, text=all_users[i][j])
                e.grid(row=i+1, column=j)

def affiche_fenetre():
    
    frame_panel.pack()
    affiche_events()
    fenetre_auth.pack_forget()
    # label.pack(fill="both", expand="yes")

def affiche_events():
    affiche_table(frame3)
    label2.pack_forget()
    label.pack(fill="both", expand="yes")    

def affiche_users():
    affiche_table_users(frame3_1)
    label.pack_forget() 
    label2.pack(fill="both", expand="yes")    
# <------Fonction affichages


# ================================

# Partie graphique avec Tkinter
# ==================================


widget = tkinter.Tk()
widget.title('Mairie')
# widget["bg"]= code_couleur

#-------------> Fenetre d'authentification
fenetre_auth = tkinter.Label(widget, bg=code_couleur)
fenetre_auth.pack(pady = 10, padx = 10)

frame1 = tkinter.Frame(fenetre_auth, bg=code_couleur, width=350, height=150)
frame1.pack(pady = 10, padx = 10)

username = tkinter.Label(frame1, text=" Username ")
username.grid (row = 2,column = 1, sticky = "E", padx = 10, pady = 5)

password = tkinter.Label(frame1, text=" Password ")
password.grid (row = 3, column = 1, sticky = "E", padx = 10, pady = 5)

username_data = tkinter.Entry(frame1)
username_data.grid (row = 2, column = 2, padx=5, pady=5)

password_data = tkinter.Entry(frame1)
password_data.grid (row = 3, column = 2, padx=5, pady=5)
password_data.config(show="*")

Valider = tkinter.Button (fenetre_auth, text=' Connexion ', command=authentification, justify='center')
Valider.pack(pady = 10)
#<------------ Fenetre d'authentificattion


#---------------------> Onglets du l'application
frame_panel = tkinter.Frame(widget)
frame_panel.pack_forget()

event_panel = tkinter.Button(frame_panel, bg=code_couleur2, relief="groove", text="Gestion d'evenements", command=affiche_events)
event_panel.pack(side= "left", padx=5)

user_panel = tkinter.Button(frame_panel, bg=code_couleur3, relief="groove", text="Gestion des utilisateurs", command=affiche_users)
user_panel.pack()
#<--------------------- Onglets du l'application

#---------->Fenetre Evenements
label = tkinter.Label(widget, bg=code_couleur)
label.pack_forget()

# Frame des buttons de gestion
frame1 = tkinter.Frame(label, bg=code_couleur)
frame1.pack()

# Les buttons
add_button = tkinter.Button(frame1, text="Ajouter", command = add_function, width=10)
add_button.pack(side= "left", padx=5, pady=5)

# read_button = tkinter.Button(frame1, text="Afficher", command = read_function, width=10)
# read_button.pack(side= "left", padx=5, pady=5)

edit_button = tkinter.Button(frame1, text="Modifier", command = edit_function, width=10)
edit_button.pack(side= "left", padx=5, pady=5)

delete_button = tkinter.Button(frame1, text="Supprimer", command =lambda: delete_function(event_id), width=10)
delete_button.pack(side= "left", padx=5, pady=5)

reset_button = tkinter.Button(frame1, text="Reinitialiser", command = reset_function, width=10)
reset_button.pack(side= "left", padx=5, pady=5)

# Frame2 des input
frame2 = tkinter.Frame(label, bg=code_couleur)
frame2.pack(padx=10, pady=10)

#Les inputs et les labels
titre_film = tkinter.Label(frame2, text="Type de l'evenement", bg=code_couleur, padx=10) 
titre_film.grid(row= 1, column=1)
type_events=['Film', 'Debat', 'Animation', 'Contexte']
value_film = tkinter.StringVar() 
value_film.set(type_events[0])
entree_film = tkinter.OptionMenu(frame2, value_film,*type_events)
entree_film.grid(row= 2, column=4, padx=10)
entree_film.grid(row= 1, column=2, padx=10)

titre_auteur = tkinter.Label(frame2, text="Nom de l'evenement", bg=code_couleur, padx=10) 
titre_auteur.grid(row= 1, column=3)
value_auteur = tkinter.StringVar() 
entree_auteur = tkinter.Entry(frame2, textvariable=value_auteur, width=30)
entree_auteur.grid(row= 1, column=4, padx=10)

titre_anim = tkinter.Label(frame2, text="Date (AAAA-MM-JJ)", bg=code_couleur, padx=10) 
titre_anim.grid(row= 2, column=1)
value_anim = tkinter.StringVar() 
entree_anim = tkinter.Entry(frame2, textvariable=value_anim, width=30)
entree_anim.grid(row= 2, column=2, padx=10)

titre_debat = tkinter.Label(frame2, text="Responsable", bg=code_couleur, padx=10) 
titre_debat.grid(row= 2, column=3)

value_debat = tkinter.StringVar() 
all_users= read_users(c)

dict_users=dict()
  
for id,nom,prenom,poste,ususername,password,date_debut,date_fin,admin in all_users:
    dict_users.setdefault(id, nom)

option_menu = tkinter.OptionMenu(frame2, value_debat,*dict_users.values())
option_menu.grid(row= 2, column=4, padx=10)
# --
#Affichage texte
frame3 = tkinter.Frame(label)
frame3.pack(padx=10, pady=5, fill="both", expand="yes")


affiche_table(frame3)
# <----------Fenetre Evenements

# <----------Fenetre Users
label2 = tkinter.Label(widget, bg=code_couleur3)
label2.pack_forget()

# Frame des buttons de gestion
frame1 = tkinter.Frame(label2, bg=code_couleur3)
frame1.pack()

# Les buttons

add_button1 = tkinter.Button(frame1, text="Ajouter",
                            command=add_function_user, width=10)
add_button1.pack(side="left", padx=5, pady=5)

# read_button = tkinter.Button(frame1, text="Afficher", command = read_function, width=10)
# read_button.pack(side= "left", padx=5, pady=5)

edit_button1 = tkinter.Button(
    frame1, text="Modifier", command=edit_function_user, width=10)
edit_button1.pack(side="left", padx=5, pady=5)

delete_button1 = tkinter.Button(frame1, text="Supprimer", command =lambda: delete_function_user(event_id), width=10)
delete_button1.pack(side= "left", padx=5, pady=5)

reset_button1 = tkinter.Button(
    frame1, text="Reinitialiser", command=reset_function_user, width=10)
reset_button1.pack(side="left", padx=5, pady=5)

# Frame2 des input
frame2_1 = tkinter.Frame(label2, bg=code_couleur3)
frame2_1.pack(padx=10, pady=10)

# Les inputs et les labels
user_name = tkinter.Label(frame2_1, text="Nom", bg=code_couleur3, padx=10)
user_name.grid(row=1, column=1)
value_name = tkinter.StringVar()
entree_name = tkinter.Entry(frame2_1, textvariable=value_name, width=30)
entree_name.grid(row=1, column=2, padx=10)


user_Firstname = tkinter.Label(frame2_1, text="Prenom", bg=code_couleur3, padx=10)
user_Firstname.grid(row=1, column=3)
value_Firstname = tkinter.StringVar()
entree_Firstname = tkinter.Entry(
    frame2_1, textvariable=value_Firstname, width=30)
entree_Firstname.grid(row=1, column=4, padx=10)

user_poste = tkinter.Label(frame2_1, text="Poste", bg=code_couleur3, padx=10)
user_poste.grid(row=2, column=1)
value_poste = tkinter.StringVar()
entree_poste = tkinter.Entry(frame2_1, textvariable=value_poste, width=30)
entree_poste.grid(row=2, column=2, padx=10)

user_username = tkinter.Label(
    frame2_1, text="Username", bg=code_couleur3, padx=10)
user_username.grid(row=2, column=3)
value_username = tkinter.StringVar()
entree_username = tkinter.Entry(frame2_1, textvariable=value_username, width=30)
entree_username.grid(row=2, column=4, padx=10)

user_password = tkinter.Label(
    frame2_1, text="Password", bg=code_couleur3, padx=10)
user_password.grid(row=3, column=1)
value_password = tkinter.StringVar()
entree_password = tkinter.Entry(frame2_1, textvariable=value_password, width=30)
entree_password.grid(row=3, column=2, padx=10)

user_date_debut = tkinter.Label(
    frame2_1, text="Date de début", bg=code_couleur3, padx=10)
user_date_debut.grid(row=3, column=3)
value_date_debut = tkinter.StringVar()
entree_date_debut = tkinter.Entry(
    frame2_1, textvariable=value_date_debut, width=30)
entree_date_debut.grid(row=3, column=4, padx=10)

user_date_fin = tkinter.Label(
    frame2_1, text="Date de fin", bg=code_couleur3, padx=10)
user_date_fin.grid(row=4, column=1)
value_date_fin = tkinter.StringVar()
entree_date_fin = tkinter.Entry(frame2_1, textvariable=value_date_fin, width=30)
entree_date_fin.grid(row=4, column=2, padx=10)

user_role = tkinter.Label(
    frame2_1, text="Cochez pour devenir admin", bg=code_couleur3, padx=10)
user_role.grid(row=4, column=3)


value_role = tkinter.StringVar()
value_role.set(0)
# entree_role = tkinter.Entry(frame2_1, textvariable=value_role, width=30)
entree_role = tkinter.Radiobutton(
    frame2_1, text="Non", variable=value_role, value=0)
entree_role2 = tkinter.Radiobutton(
    frame2_1, text="Oui", variable=value_role, value=1)
entree_role2.grid(row=4, column=5, padx=10)
entree_role.grid(row=4, column=4, padx=10)

frame3_1 = tkinter.Frame(label2)
frame3_1.pack(padx=10, pady=5, fill="both", expand="yes")


affiche_table_users(frame3_1)
# <----------Fenetre Users

widget.mainloop()
# ==================================

conn.close()
# =========================