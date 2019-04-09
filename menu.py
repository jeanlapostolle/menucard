filemenu = open("./ressource/menu/menu.csv", "r")

entrees = []
plats = []
desserts = []
boissons = []
accompagnements = []

dic = {"plats": plats, "accompagnements": accompagnements,
       "entrees": entrees, "desserts": desserts, "boissons": boissons}
for line in filemenu.readlines():
    type, nom, prix = line.split(',')
    prix = prix[:-1]
    sel = dic[type]
    sel.append(nom)
