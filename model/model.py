from database.DAO import DAO

class Model:
    def __init__(self):
        pass

    def getAnni(self):
        return DAO.getAnni()

    def getVendite(self):
        return DAO.getVendite()

    def getProdotti(self):
        return DAO.getProdotti()

    def getRivenditori(self):
        return DAO.getRivenditori()

    def getTopVendite(self, anno, brand, rivenditori):
        lista = []
        for el in DAO.getVendite():
            if anno != "Nessun filtro":
                if el["Anno"] == anno:
                    if brand != "Nessun filtro":
                        if el["Brand"] == brand:
                            if rivenditori != "Nessun filtro":
                                if el["Rivenditori"] == rivenditori:
                                    lista.append(el)
            else:
                if brand != "Nessun filtro":
                    if el["Brand"] == brand:
                        if rivenditori != "Nessun filtro":
                            if el["Rivenditori"] == rivenditori:
                                lista.append(el)
                else:
                    if rivenditori != "Nessun filtro":
                        if el["Rivenditori"] == rivenditori:
                            lista.append(el)
                    else:
                        lista.append(el)
        return lista
