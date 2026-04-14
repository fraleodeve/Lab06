import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()

        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # self._page.theme_mode = ft.ThemeMode.DARK

        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self._ddAnno = None
        self._ddBrand = None
        self._ddRivenditore = None
        self._btnTopVendite = None
        self._btnAnalizzaVendite = None
        self.txt_result = None

    def load_interface(self):
        # title
        self._title = ft.Text("Analizza vendite", color="blue", size=24)
        self._page.controls.append(self._title)

        # riga 1
        self._ddAnno = ft.Dropdown(label="Anno",
                                   options = [ft.dropdown.Option("Nessun filtro")],
                                   width=200)
        self._controller.fillddAnno()

        self._ddBrand = ft.Dropdown(label="Brand",
                                    options = [ft.dropdown.Option("Nessun filtro")],
                                    width=200)
        self._controller.fillddBrand()

        self._ddRivenditore = ft.Dropdown(label="Rivenditore",
                                          options = [ft.dropdown.Option("Nessun filtro")],
                                          width=450)
        self._controller.fillddRivenditore()

        row1 = ft.Row([self._ddAnno, self._ddBrand, self._ddRivenditore],
                      alignment=ft.MainAxisAlignment.CENTER)

        # riga 2
        self._btnTopVendite = ft.ElevatedButton(text="Top vendite",
                                                   on_click=self._controller.handleTopVendite,
                                                   width=200)

        self._btnAnalizzaVendite = ft.ElevatedButton(text="Analizza vendite",
                                                on_click=self._controller.handleAnalizzaVendite,
                                                width=200)

        row2 = ft.Row([self._btnTopVendite, self._btnAnalizzaVendite],
                      alignment=ft.MainAxisAlignment.CENTER)

        self._page.add(row1, ft.Container(height=10), row2, ft.Container(height=10))

        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result)
        self._page.update()

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
