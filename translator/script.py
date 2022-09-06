import time
from ponstrans import translate


qbulka = True
list = []
while qbulka:
    duma = input("Vuvedi duma: ")
    list.append(duma)
    ready = input("Gotovo y/n?: ")
    if ready == "y":
        qbulka = False
x = 0
list2 = []
for i in range(len(list)):
    translations = translate(word=list[x], source_language="de", target_language="bg")
    x += 1
    list2.append(translations[0]["target"])
list3 = dict(zip(list,list2))
print(list3)
time.sleep(60)