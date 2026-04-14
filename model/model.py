from database.DAO import DAO

class Model:
    def __init__(self):
        self.listaVendite = list()
        self.listaProdotti = list()
        self.listaRivenditori = list()

        self.creazioneListe()

    def creazioneListe(self):
        self.listaVendite = DAO.getVendite()
        self.listaProdotti = DAO.getProdotti()
        self.listaRivenditori = DAO.getRivenditori()

    def getAnni(self):
        return DAO.getAnni()

    def getVendite(self):
        return DAO.getVendite()

    def getProdotti(self):
        return DAO.getProdotti()

    def getRivenditori(self):
        return DAO.getRivenditori()


    def getTopVendite(self, anno, brand, rivenditore):
        lista_agg = self.corpo_base(anno, brand, rivenditore)
        lista_agg.sort(key=lambda x: x[3], reverse=True)

        if len(lista_agg) > 5:
            lista_finale = lista_agg[:5]
        else:
            lista_finale = lista_agg

        return lista_finale

    def AnalisiVendite(self, anno, brand, rivenditore):
        lista = self.corpo_base(anno, brand, rivenditore)

        ricavi_totali = 0
        for el in lista:
            ricavi_totali += el[3]

        numero_vendite = len(lista)

        numero_rivenditori = 0
        listaR = list()
        for el in lista:
            if el[1] not in listaR:
                numero_rivenditori += 1
                listaR.append(el[1])

        numero_prodotti = 0
        listaP = list()
        for ele in lista:
            if ele[0] not in listaP:
                numero_prodotti += 1
                listaP.append(ele[0])

        return ricavi_totali, numero_vendite, numero_rivenditori, numero_prodotti

    def corpo_base(self, anno, brand, rivenditore):
        lista = []
        codiceP = []
        codiceR = []

        for b in self.listaProdotti:
            if b.Product_brand == brand:
                codiceP.append(int(b.Product_number))

        for c in self.listaRivenditori:
            if c.Retailer_name == rivenditore:
                codiceR.append(int(c.Retailer_code))

        # print(anno, codiceP, codiceR, brand, rivenditore)

        for el in DAO.getVendite():
            if anno != "Nessun filtro":
                if int(el.Date.year) == int(anno):
                    if brand != "Nessun filtro":
                        if int(el.Product_number) in codiceP:
                            if rivenditore != "Nessun filtro":
                                if int(el.Retailer_code) in codiceR:
                                    # print("CIAOOOOOOOOOOOOOOOOOOOOO")
                                    lista.append(el)
                            else:
                                lista.append(el)
                    else:
                        if rivenditore != "Nessun filtro":
                            if int(el.Retailer_code) in codiceR:
                                lista.append(el)
                        else:
                            lista.append(el)

            else:
                if brand != "Nessun filtro":
                    if int(el.Product_number) in codiceP:
                        if rivenditore != "Nessun filtro":
                            if int(el.Retailer_code) in codiceR:
                                lista.append(el)
                        else:
                            lista.append(el)
                else:
                    if rivenditore != "Nessun filtro":
                        if int(el.Retailer_code) in codiceR:
                            lista.append(el)
                    else:
                        lista.append(el)

        lista_agg = list()
        for element in lista:
            lista_singola = []
            lista_singola.append(element.Product_number)
            lista_singola.append(element.Retailer_code)
            lista_singola.append(element.Date)
            lista_singola.append(element.Quantity * element.Unit_sale_price)
            lista_agg.append(lista_singola)

        return lista_agg

