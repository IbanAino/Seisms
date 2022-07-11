##
# class Controller
#
# Cette classe est la classe Controller de l'architecture logicielle Modèle - Vue - controlleur.
# Elle se charge de faire transiter les commandes et les données entre le Modèle et la Vue.
##
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    
    def load_Sismic_Data(self, day, month, year):
        sismic_Data = self.model.load_sismic_Data_From_Webb(day = day, month = month, year = year)
        return sismic_Data

    def display_Sismic_Data(self, csv_file_Path):
        self.view.display_Sismic_Data(csv_file_Path)

    def load_Station_Config(self):
        """
        Cette fonction envoie à l'interface graphique les données lues dans le fichier config de l'application.
        Cette fonction n'est appelée qu'après l'instanciation de toutes le classes, car le fichier de config n'est lu qu'une fois le programme lancé.
        """
        self.model.load_config_file()

        lat = self.model.station_Latitude
        lon = self.model.station_Longitude
        self.view.set_Station_Coordonates(station_Latitude = lat, station_Longitude = lon)

        self.view.frame_Down.set_Station_Name(self.model.station_Name)
