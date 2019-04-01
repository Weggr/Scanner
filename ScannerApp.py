from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
import datetime


class ScannerApp(App):

    resultat = ''
    compteur = 0
    compteurRésultat = 0

    def switch_letter(self,argument):
        dictionnaire = {
            '&':'1',
            'é':'2',
            '"':'3',
            "'":'4',
            '(':'5',
            '-':'6',
            'è':'7',
            '_':'8',
            'ç':'9',
            'à':'0',
            'q':'a',
            'w':'z',
            'a':'q',
            'z':'w',
            'Q':'A',
            'W':'Z',
            'A':'Q',
            'Z':'W',
            'm':';',
            'M':':',
            ',':'m',
            '?':'M'
        }
        return dictionnaire.get(argument, "Invalid letter")


    def on_text(self, value):
        return value
    def refocus_ti(self,*args):
        self.recherche.focus = True

    def callback(self, text):
        compteur2 = 0
        ID = self.recherche.text
        self.recherche.text = ''
        Clock.schedule_once(self.refocus_ti)
        ID2 = ''
        #import pdb; pdb.set_trace()
        for x in ID :
            x2 = x
            x2 = self.switch_letter(x)
            if(x2 != "Invalid letter"):
                ID2=ID2+x2
            else:
                ID2="Erreur"

        self.label2.text = ID2

        fichier1 = open("Classe.csv", mode = 'r')
        fichier2 = open("Presences.csv", mode = 'a')
        for l in fichier1.readlines():
            if (l.split(";")[0] == ID2):
                compteur2=1
                if(self.compteur == 0):
                    self.resultat = "\nEtudiant : " + l.split(";")[1] + " " + l.split(";")[2]+ " présent à " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'));
                    self.compteur = 1
                else:
                    self.resultat = self.resultat + "\nEtudiant : " + l.split(";")[1] + " " + l.split(";")[2]+ " présent à "+ str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'));
                fichier2.write(ID2 +";"+ l.split(";")[1] +";"+ l.split(";")[2] +";"+ str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))+"\n")
        if (compteur2 == 0):
            print("Badgage effectuée : Badge non reconnu")
            print("\n")
            self.resultat = self.resultat + "\nBadge Inconnu à " + str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'));
        else:
            print("Badgage effectuée : Badge reconnu")
            print("\n")

        fichier1.close()
        fichier2.close()
        self.label2.text = self.resultat



    def build(self):
        horizontalBox   = BoxLayout(orientation='horizontal', spacing = 5)
        horizontalBox.add_widget(Label(text=' ID du \nbadge :',size_hint=(0.3,1)))
        self.recherche = TextInput(multiline=False, password =True)
        self.recherche.focus = True
        self.recherche.bind(on_text_validate=self.callback)
        horizontalBox.add_widget(self.recherche)

        superBox = BoxLayout(orientation='vertical')
        superBox.add_widget(horizontalBox)
        label1 = Label(text='Information sur les étudiants :', size_hint=(1,.3))
        self.label2 = Label(text="Commencez à badger", size_hint=(1,2.5))
        superBox.add_widget(label1)
        superBox.add_widget(self.label2)

        return superBox


if __name__ == '__main__':
    ScannerApp().run()
