from dataclasses import dataclass

@dataclass
class Giocatore:
    PlayerID: int
    Name: str
    MatchID: int
    TeamID: int
    passaggi: int
    assist: int
    tempoGiocato: int


    def __hash__(self):
        return hash(self.PlayerID)
