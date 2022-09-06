import random
from bs4 import BeautifulSoup
import requests
import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

url = "https://www.delicious.com.au/recipes/rhubarb-orange-cordial-recipe/6hr0kcwu"
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")
find = doc.find_all("h4")



list_2 = []
list_3 = []
list_4 = []



def url_find(url):
    x = url
    resultat = requests.get(x)
    doc2 = BeautifulSoup(resultat.text, "html.parser")
    find3 = doc2.find_all("h4")
    try:
        for i in range(0, 100):
            final = (find3[0].parent.find_all("li")[i].string)
            list_2.append(final)
    except:
        "IndexError: list index out of range"



def url_find2(url):
    x = url
    resultat = requests.get(x)
    doc2 = BeautifulSoup(resultat.text, "html.parser")
    find3 = doc2.find_all("h4")
    try:
        for i in range(0, 100):
            final = (find3[0].parent.find_all("li")[i].string)
            list_3.append(final)
    except:
        "IndexError: list index out of range"


def url_find3(url):
    x = url
    resultat = requests.get(x)
    doc2 = BeautifulSoup(resultat.text, "html.parser")
    find3 = doc2.find_all("h4")
    try:
        for i in range(0, 100):
            final = (find3[0].parent.find_all("li")[i].string)
            list_4.append(final)
    except:
        "IndexError: list index out of range"

def recepie(url):
    x = url
    result = requests.get(x)
    file = BeautifulSoup(result.text,"html.parser")
    findfind = file.find_all("article")
    a =str(findfind[random.choice((0,9))].find_all("a")[0]).replace(str(findfind[1].find_all("a")[0].find("picture")),"")
    b =((a.split()[1].replace("href=","").replace(">",""))[1:-1])
    recepie.c = "https://www.delicious.com.au/" + b
    recepie.d = b[8:-8]
def recepie2(url):
    x = url
    result = requests.get(x)
    file = BeautifulSoup(result.text,"html.parser")
    findfind = file.find_all("article")
    a =str(findfind[random.choice((0,9))].find_all("a")[0]).replace(str(findfind[1].find_all("a")[0].find("picture")),"")
    b =((a.split()[1].replace("href=","").replace(">",""))[1:-1])
    recepie2.c = "https://www.delicious.com.au/" + b
    recepie2.d = b[8:-8]
def recepie3(url):
    x = url
    result = requests.get(x)
    file = BeautifulSoup(result.text,"html.parser")
    findfind = file.find_all("article")
    a =str(findfind[random.choice((0,9))].find_all("a")[0]).replace(str(findfind[1].find_all("a")[0].find("picture")),"")
    b =((a.split()[1].replace("href=","").replace(">",""))[1:-1])
    recepie3.c = "https://www.delicious.com.au/" + b
    recepie3.d = b[8:-8]


class MyGrid(GridLayout):
    list_plodove = []
    hrani = input("what food: ")
    hrani2 = input("what food: ")
    hrani3 = input("what food: ")
    list_plodove.append(hrani)
    list_plodove.append(hrani2)
    list_plodove.append(hrani3)
    main_link = "https://www.delicious.com.au/search?ct=recipes&q={0}".format(hrani)
    main_link2 = "https://www.delicious.com.au/search?ct=recipes&q={0}".format(hrani2)
    main_link3 = "https://www.delicious.com.au/search?ct=recipes&q={0}".format(hrani3)
    recepie(main_link)
    recepie2(main_link2)
    recepie3(main_link3)
    url_find(recepie.c)
    url_find2(recepie2.c)
    url_find3(recepie3.c)
    a = 0

    list_rezepti = [str(list_2).replace(r"\n", ""), str(list_3).replace(r"\n", ""), str(list_4).replace(r"\n", "")]

    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.text = TextInput()
        self.add_widget(self.text)
        for i in self.list_plodove:
            button = Button(text=i)
            self.add_widget(button)
            button.bind(on_press=self.press)

    def press(self, instance):
        self.a += 1
        if instance.text in self.list_plodove:
            self.text.text = str(
                list(zip(self.list_plodove, self.list_rezepti))[self.list_plodove.index(instance.text)][1])
            if self.a < 2:
                self.add_widget(Label(text=recepie.d))
                self.add_widget(Label(text=recepie2.d))
                self.add_widget(Label(text=recepie3.d))

class MyApp(App):
    def build(self):
        return MyGrid()


MyApp().run()
