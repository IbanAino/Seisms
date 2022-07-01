#from tkinter import Tk, W, E, messagebox
from tkinter import ttk
import tkinter as tk
from datetime import datetime
import re
import math
from math import sin, cos, sqrt, atan2, radians


##
# class View
#
# Cette classe est la classe Vue de l'architecture logicielle Modèle - Vue - controlleur.
#
# Elle définie toute la partie interface graphique de l'application.

##

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        parent.geometry("820x900")
        parent.configure(bg = 'Light Grey')

        self.sismic_Data = []
        self.station_Latitude = '0'
        self.station_Longitude = '0'

        self.frame_Up = Frame_Up(self.button_clicked)
        self.frame_Up.place(x = 20, y = 20)

        self.frame_Down = Frame_Down(station_Latitude = self.station_Latitude, station_Longitude = self.station_Longitude)
        self.frame_Down.place(x = 20, y = 80)

        # set the controller
        self.controller = None

    def set_Controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def button_clicked(self):
        """
        Handle button click event
        :return:
        """
        day = self.frame_Up.date_Day_Entry.get()
        month = self.frame_Up.date_Month_Entry.get()
        year = self.frame_Up.date_Year_Entry.get()

        self.set_cursor_busy()

        self.sismic_Data = self.controller.load_Sismic_Data(day = day, month = month, year = year)
        self.frame_Down.display_Sismic_Data(self.sismic_Data)

        self.reset_cursor()

    def display_Sismic_Data(self, sismic_Data):
        self.frame_Down.display_Sismic_Data(sismic_Data)

    def set_cursor_busy(self):
        self.frame_Up.config(cursor='watch')
        self.frame_Up.update_idletasks()
        self.frame_Down.config(cursor='watch')
        self.frame_Down.update_idletasks()

    def reset_cursor(self):
        self.frame_Up.config(cursor='')
        self.frame_Down.config(cursor='')


##
# class Frame_Up
#
# Cette classe représente la partie supérieure de l'interface graphique
# Cette classe contien un formulaire pour enter la date des données sismiques à télécharger, ainsi que le bouton pour lancer le téléchargement.
# Les entrées utilisateur sont vérifiées.
##
class Frame_Up(tk.Frame):
    def __init__(self, button_clicked):
        super(Frame_Up, self).__init__()
        self.configure(bg = 'Light Grey')

        self.date_Day = datetime.today().strftime('%d')
        self.date_Month = datetime.today().strftime('%m')
        self.date_Year = datetime.today().strftime('%Y')

        print(self.date_Day + ' ' + self.date_Month + ' ' + self.date_Year)

        # Validation commands
        self.validate_Command_Day = self.register(self.on_Validate_Day)
        self.validate_Command_Month = self.register(self.on_Validate_Month)
        self.validate_Command_Year = self.register(self.on_Validate_Year)

        tk.Label(self, text='Date ', background = 'Light Grey').grid(row = 1, column = 1)
        tk.Label(self, text='/', background = 'Light Grey').grid(row = 1, column = 3)
        tk.Label(self, text='/', background = 'Light Grey').grid(row = 1, column = 5)
        tk.Label(self, background = 'Light Grey', width = 5).grid(row = 1, column = 7)
        tk.Label(self, background = 'Light Grey', width = 5).grid(row = 1, column = 9)

        self.date_Day = tk.StringVar(value = self.date_Day)
        self.date_Month = tk.StringVar(value = self.date_Month )
        self.date_Year = tk.StringVar(value = self.date_Year )

        self.date_Day_Entry = tk.Entry(self, validate="focusout", textvariable = self.date_Day, bg = 'white', fg = 'black', width = 2)
        self.date_Month_Entry = tk.Entry(self, validate="focusout", textvariable = self.date_Month, bg = 'white', fg = 'black', width = 2)
        self.date_Year_Entry = tk.Entry(self, validate="focusout", textvariable = self.date_Year, bg = 'white', fg = 'black', width = 4)
        self.date_Day_Entry.grid(row = 1, column = 2)
        self.date_Month_Entry.grid(row = 1, column = 4)
        self.date_Year_Entry.grid(row = 1, column = 6)
        self.date_Day_Entry.configure(validatecommand = (self.validate_Command_Day, "%W", "%P"))
        self.date_Month_Entry.configure(validatecommand = (self.validate_Command_Month, "%W", "%P"))
        self.date_Year_Entry.configure(validatecommand = (self.validate_Command_Year, "%W", "%P"))

        self.save_button = tk.Button(self, text=' Charger les données sismiques ', command = button_clicked, width = 30)
        self.save_button.grid(row=1, column=8)


    def on_Validate_Day(self, entry_name, new_value):
        """
        Cette fonction vérifie que la valuer du jour entrée par l'utilisateur est bien formatée.
        Cette valeur doit être comprise entre 1 et 31
        Si c'est la cas, l'entrée se colore en vert. Sinon elle se colore en rouge.
        """
        entry = self.nametowidget(entry_name)
        #entry.configure(background="#98FB98")

        try:
            new_value = float(new_value)

            if (1 <= new_value and new_value <= 31):
                #entry.configure(background="#98FB98")
                entry.configure(background="white")

            else:
                entry.configure(background="#FFBCC1")

        except ValueError:
            entry.configure(background="#FFBCC1")
            return True

        return True

    def on_Validate_Month(self, entry_name, new_value):
        """
        Cette fonction vérifie que la valuer du mois entrée par l'utilisateur est bien formatée.
        Cette valeur doit être comprise entre 1 et 12
        Si c'est la cas, l'entrée se colore en vert. Sinon elle se colore en rouge.
        """
        entry = self.nametowidget(entry_name)
        #entry.configure(background="#98FB98")

        try:
            new_value = float(new_value)

            if (1 <= new_value and new_value <= 12):
                #entry.configure(background="#98FB98")
                entry.configure(background="white")


            else:
                entry.configure(background="#FFBCC1")

        except ValueError:load_sismic_Data
        return True

    def on_Validate_Year(self, entry_name, new_value):
        """
        Cette fonction vérifie que la valuer de l'année entrée par l'utilisateur est bien formatée.
        Cette valeur doit être comprise entre 1000 et 9999
        Si c'est la cas, l'entrée se colore en vert. Sinon elle se colore en rouge.
        """
        entry = self.nametowidget(entry_name)
        #entry.configure(background="#98FB98")

        try:
            new_value = float(new_value)

            if (1000 <= new_value and new_value <= 9999):
                #entry.configure(background="#98FB98")
                entry.configure(background="white")

            else:
                entry.configure(background="#FFBCC1")

        except ValueError:
            entry.configure(background="#FFBCC1")
            return True

        return True


##
# class Frame_Down
#
# Cette classe représente la partie inférieure de l'interface graphique
# elle se compose d'un tableau affichant les données sismques
# Cette classe récupère les données du formulaire de la classe Frame_Up et se charge de télécharger les données pour les afficher.
# 
##
class Frame_Down(tk.Frame):
    def __init__(self, station_Latitude, station_Longitude):
        super(Frame_Down, self).__init__()

        self.configure(bg = 'Light Grey')

        self.station_Latitude = station_Latitude
        self.station_Longitude = station_Longitude

        self.tree=ttk.Treeview(self, column=("c1", "c2", "c3", "c4", "c5"), show='headings', height=38)
        self.tree.column("# 1",anchor='center', stretch='no', width=110)
        self.tree.heading("# 1", text="Date")
        self.tree.column("# 2", anchor='center', stretch='no', width=110)
        self.tree.heading("# 2", text="Heure")
        self.tree.column("# 3", anchor='center', stretch='no', width=80)
        self.tree.heading("# 3", text="Magn.")
        self.tree.column("# 4", anchor='center', stretch='no', width=300)
        self.tree.heading("# 4", text="Lieu")
        self.tree.column("# 5", anchor='center', stretch='no', width=180)
        self.tree.heading("# 5", text=("Distance to station"))
        self.tree.grid(row=1, column=0, columnspan=5)

    def set_Station_Name(self, station_Name):
        self.tree.heading("# 5", text=("Distance to " + station_Name))

    def display_Sismic_Data(self, sismic_Data):

        # Clear Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, row in enumerate(sismic_Data):
            if len(row) > 20:
                latitude = row[1]
                longitude = row[2]
                distance_from_station_to_seism = 0
                distance_from_station_to_seism = self.distance_to_Station(longitude = longitude, latitude = latitude)

                self.tree.insert('', 'end',text="1",values=(row[0][0:10],row[0][11:19],row[4],row[13],str(distance_from_station_to_seism)[0:8]))

    def distance_to_Station(self, longitude, latitude):
        """
        Cette fonction calcule la distance entre deux paires de coordonnées géographiques.
        """
        lon1 = float(self.station_Longitude)
        lat1 = float(self.station_Latitude)
        lon2 = float(longitude)
        lat2 = float(latitude)

        radius = 6371  # km

        dlat = math.radians(lat2 - lat1)
        dlon = math.radians(lon2 - lon1)
        a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
            math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
            math.sin(dlon / 2) * math.sin(dlon / 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        d = radius * c

        #print(d)
        return(d)