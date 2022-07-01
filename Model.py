import configparser
import re
import os
from os.path import exists
import requests

import csv

##
# class Model
#
# Cette classe est la classe Model de l'architecture logicielle Modèle - Vue - controlleur.
# Elle contient deux fonction principaes :
# - fonction save_Data, qui enregistre la mesabs dans un fichier texte.
# - fonction read_Mesabs, qui ouvre une mesabs déjà enregistrée à partir d'un fochier texte pour pouvoir l'éditer.
##
class Model:
    def __init__(self):
        # set the controller
        self.controller = None

        self.station_Latitude = '0'
        self.station_Longitude = '0'
        self.station_Name = 'no name'

        self.proxies = {}

    def set_Controller(self, controller):
        """
        Set the controller
        :param controller:
        :return:
        """
        self.controller = controller

    def load_sismic_Data_From_Webb(self, day, month, year):
        """
        Cette fonction récupère les données sismiques de la base de données internationnale.
        Cette base est accessible via le site www.earthquake.usgs.gov.
        Le site propose un formulaire qui télécharge les données sismiques sous la forme d'un fichier csv.
        Cette fonction envoie la requête url et lit la réponse au format csv pour l'extraire dans une liste.
        """
        csv_url = "https://earthquake.usgs.gov/fdsnws/event/1/query.csv?starttime=" + year + "-" + month + "-" + day + " 00:00:00&endtime=" + year + "-" + month + "-" + day + " 23:59:59&minmagnitude=4.5&orderby=time"
        #proxies = {'http': 'http://192.168.61.7:3129', 'https': 'http://192.168.61.7:3129'}

        print(csv_url)

        req = requests.get(url=csv_url, proxies=self.proxies)
        url_content = req.content

        seisms_Raw = url_content.decode('utf-8')
        seisms_List = re.split('[\n]', seisms_Raw)

        for i, row in enumerate(seisms_List):
            # Split by comma (,) but ignoring commas into quotes (ex: "99 km SW of Corinto, Nicaragua")
            seisms_List[i] = re.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)", row)

            # Delete quotes
            for y, cell in enumerate(seisms_List[i]):
                seisms_List[i][y] = cell.replace('"','')

        # Remove the file's first and last lines
        seisms_List.pop(0)
        del seisms_List[-1]

        return seisms_List

    def load_config_file(self):
        """
        Un fichier de configuration contient les informations de la station qui ne sont pas vouées à changer:
          - lieu d'implantation de la station
          - longitude
          - lattitude
        """
        self.config = configparser.ConfigParser()
        self.config.read('config.txt')

        if (self.config.has_option('Station_Configuration', 'Site') and
            self.config.has_option('Station_Configuration', 'Station_latitude') and
            self.config.has_option('Station_Configuration', 'Station_longitude')):
            pass
            
        else:
            print('Erreur dans la fichier de configuration config.txt\n\nVeuillez l\'éditer.')
            return True

        self.station_Configuration  = self.config['Station_Configuration']

        self.station_Latitude = self.station_Configuration['Station_latitude']
        self.station_Longitude = self.station_Configuration['Station_longitude']
        self.station_Name = self.station_Configuration['Site']

        proxies_List_Raw = self.config.get('Proxies_list','proxies')
        proxies_List = re.split('[\n]', proxies_List_Raw)

        for i, row in enumerate(proxies_List):
            proxies_List[i] = re.split('[,]', row)

        # Convert proxies list into proxies dictionnary
        for proxy in proxies_List:
            self.proxies[proxy[0]] = proxy[1]
        


