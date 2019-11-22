import uuid

class Player(object):

    def __init__(self, firstname, lastname, wins=0, losses=0, playerid=None):

        if playerid == None:
            self.playerid = unicode(uuid.uuid4())
        else:
            self.playerid = unicode(playerid)

        self.firstname = unicode(firstname).lower()
        self.lastname = unicode(lastname).lower()
        self.wins = int(wins)
        self.losses = int(losses)

        try:
            self.ratio = round((float(wins) / (wins + losses)) * 100, 2)
        except:
            self.ratio = float()

    def get_player(self):
        return {
            "playerid": self.playerid,
            "firstname": self.firstname,
            "lastname": self.lastname,
            "wins": self.wins,
            "losses": self.losses,
            "ratio": self.ratio
        }

    def recalculate_ratio(self):
        try:
            self.ratio = round((float(wins) / (wins + losses)) * 100, 2)
        except:
            self.ratio = float()