from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.properties import StringProperty
from kivy.uix.widget import Widget


class ScannerApp(App):



    def switch_letter(argument):
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
            'à':'0'
        }
        return dictionnaire.get(argument, "Invalid letter")


    def on_text(instance, value):
        return value

    def callback(self,instance):
        resultat = ''
        compteur2 = 0;
        compteur = 0;
        ID = self.recherche.text
        ID2 = ''
        for x in ID :
            x2 = x
            x2 = self.switch_letter()
            if(x2 != "Invalid letter"):
                ID2=ID2+x2
            else:
                ID2="Erreur"

        self.label2.text = ID2

        fichier = open("Classe.csv", mode = 'r')
        for l in fichier.readlines():
            if (l.split(";")[0] == ID2):
                compteur2=1
                if(compteur == 0):
                    resultat = "\nEtudiant : " + l.split(";")[1] + " " + l.split(";")[2]+ " présent";
                    compteur = 1
                else:
                    resultat = resultat + "\nEtudiant : " + l.split(";")[1] + " " + l.split(";")[2]+ " présent";
        if (compteur2 == 0):
            print("Badgage effectuée : Badge non reconnu")
            print("\n")
            resultat = resultat + "\nBadge Inconnu"
        else:
            print("Badgage effectuée : Badge reconnu")
            print("\n")

        fichier.close()
        self.label2.text = resultat



    def build(self):
        horizontalBox   = BoxLayout(orientation='horizontal', spacing = 5)
        horizontalBox.add_widget(Label(text=' ID du \nbadge :',size_hint=(0.3,1)))
        self.recherche = TextInput(multiline=False)
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
