import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._ddAnni = None
        self._ddBrand = None
        self._ddRivenditori = None

    def handleTopVendite(self, e):
        self._view.txt_result.controls.clear()
        if self._view._ddAnno.value == None or self._view._ddBrand.value == None or self._view._ddRivenditore.value == None:
            messaggio = "Attenzione! Campo non inserito"
            self._view.create_alert(messaggio)
        else:
            lista = self._model.getTopVendite(self._view._ddAnno.value, self._view._ddBrand.value, self._view._ddRivenditore.value)
            if len(lista) == 0:
                self._view.txt_result.controls.append(ft.Text(f"Non ci sono risultati per questa ricerca!", color="red"))
                self._view.update_page()
                return

            self._view.txt_result.controls.append(ft.Text(f"Vendite:"))
            for c in lista:
                self._view.txt_result.controls.append(ft.Text(f"Data: {c[2]}; "
                                                              f"Ricavo: {c[3]}; "
                                                              f"Rivenditore: {c[1]}; "
                                                              f"Prodotto: {c[0]}; "))
            self._view.update_page()


    def handleAnalizzaVendite(self, e):
        self._view.txt_result.controls.clear()
        if self._view._ddAnno.value == None or self._view._ddBrand.value == None or self._view._ddRivenditore.value == None:
            messaggio = "Attenzione! Campo non inserito"
            self._view.create_alert(messaggio)
        else:
            ricavi_totali, numero_vendite, numero_rivenditori, numero_prodotti = self._model.AnalisiVendite(self._view._ddAnno.value, self._view._ddBrand.value, self._view._ddRivenditore.value)
            self._view.txt_result.controls.append(ft.Text(f"Statistiche vendite:"))
            self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {ricavi_totali}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {numero_vendite}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero rivenditori: {numero_rivenditori}"))
            self._view.txt_result.controls.append(ft.Text(f"Numero prodotti: {numero_prodotti}"))
            self._view.update_page()

    def fillddAnno(self):
        for el in self._model.getAnni():
            self._view._ddAnno.options.append(ft.dropdown.Option(el))

    def fillddBrand(self):
        lista = []
        for el in self._model.getProdotti():
            if el.Product_brand not in lista:
                self._view._ddBrand.options.append(ft.dropdown.Option(
                    key = el.Product_brand,
                    data = el,
                    on_click = self._choiceDDBrand
                ))
                lista.append(el.Product_brand)

    def _choiceDDBrand(self, e):
        self._ddBrand = e.control.data
        print(self._ddBrand)

    def fillddRivenditore(self):
        lista = []
        for el in self._model.getRivenditori():
            if el.Retailer_name not in lista:
                self._view._ddRivenditore.options.append(ft.dropdown.Option(
                    key=el.Retailer_name,
                    data=el,
                    on_click=self._choiceDDRivenditore
                ))
                lista.append(el.Retailer_name)

    def _choiceDDRivenditore(self, e):
        self._ddRivenditori = e.control.data
        print(self._ddRivenditori)


