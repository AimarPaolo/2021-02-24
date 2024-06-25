from database.DB_connect import DBConnect
from model.player import Giocatore


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllMatches():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select m.MatchID as id, t.Name as s1, t2.Name as s2
from matches m, teams t, teams t2 
where t.TeamID = m.TeamHomeID and t2.TeamID = m.TeamAwayID
order by m.MatchID """
        cursor.execute(query)
        for row in cursor:
            result.append((row["id"], row["s1"], row["s2"]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getAllNodi(matchId):
        conn = DBConnect.get_connection()
        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select a.PlayerID, p.Name, a.MatchID , a.TeamID, sum(a.TotalSuccessfulPassesAll) as passaggi, sum(a.Assists) as assist, sum(a.TimePlayed) as tempoGiocato
from actions a, players p 
where a.MatchID = %s and p.PlayerID = a.PlayerID
group by a.PlayerID 
"""
        cursor.execute(query, (matchId, ))
        for row in cursor:
            result.append(Giocatore(**row))
            # Prodotto(**row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def nome3():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """"""

        cursor.execute(query, )

        for row in cursor:
            result.append()

        cursor.close()
        conn.close()
        return result