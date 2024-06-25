import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.DiGraph()
        self.nodi = []
        self.bestDizio = {}
        self.IdMap = {}

    def buildGraph(self, matchId):
        self._grafo.clear()
        self.nodi = DAO.getAllNodi(matchId[0])
        for f in self.nodi:
            self.IdMap[f.PlayerID] = f
        self._grafo.add_nodes_from(self.nodi)
        self.addEdges()

    def addEdges(self):
        self._grafo.clear_edges()
        for n1 in self._grafo.nodes:
            for n2 in self._grafo.nodes:
                if n1.TeamID != n2.TeamID:
                    if self._grafo.has_edge(n1, n2) is False:
                        efficienza1 = (n1.passaggi + n1.assist)/n1.tempoGiocato
                        efficienza2 = (n2.passaggi + n2.assist)/n2.tempoGiocato
                        peso = abs(efficienza2-efficienza1)
                        if efficienza1 > efficienza2:
                            self._grafo.add_edge(n1, n2, weight=peso)
                        else:
                            self._grafo.add_edge(n2, n1, weight=peso)
        self.createBestDizionario()

    def createBestDizionario(self):
        self.bestDizio = {}
        for n in self._grafo.nodes:
            self.bestDizio[n.PlayerID] = 0
            for uscenti in self._grafo.out_edges(n):
                self.bestDizio[n.PlayerID] += self._grafo[uscenti[0]][uscenti[1]]['weight']
            for entranti in self._grafo.in_edges(n):
                self.bestDizio[n.PlayerID] -= self._grafo[entranti[0]][entranti[1]]['weight']

    def getBestGiocatore(self):
        listamigliore = list(sorted(self.bestDizio.items(), key=lambda item: item[1], reverse=True))
        print(listamigliore)
        return listamigliore[0]

    def getMatch(self):
        return DAO.getAllMatches()

    def getCaratteristiche(self):
        return len(self._grafo.nodes), len(self._grafo.edges)
