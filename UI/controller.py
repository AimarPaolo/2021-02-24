import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.choice = None

    def handle_grafo(self, e):
        self._view.txt_result.controls.clear()
        if self.choice is None:
            self._view.create_alert("Selezionare un match!")
            return
        self._model.buildGraph(self.choice)
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato!"))
        nNodes, nEdges = self._model.getCaratteristiche()
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nNodes} nodi"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo creato ha {nEdges} archi"))
        self._view.update_page()


    def handle_migliore(self, e):
        self._view.txt_result.controls.clear()
        migliore = self._model.getBestGiocatore()
        idMap = self._model.IdMap
        self._view.txt_result.controls.append(ft.Text(f"{migliore[0]} - {idMap[migliore[0]].Name}, delta efficienza={migliore[1]}"))
        self._view.update_page()

    def fillDD(self):
        for i in self._model.getMatch():
            self._view.dd_match.options.append(ft.dropdown.Option(data=i, text=f"[{i[0]}] {i[1]} vs. {i[2]}", on_click=self.readData))

    def readData(self, e):
        if e.control.data is None:
            self.choice = None
        else:
            self.choice = e.control.data
