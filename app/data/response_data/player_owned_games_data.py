"""
Structure:
      {
        "appid": 3716600,
        "playtime_forever": 0,
        "playtime_windows_forever": 0,
        "playtime_mac_forever": 0,
        "playtime_linux_forever": 0,
        "playtime_deck_forever": 0,
        "rtime_last_played": 0,
        "playtime_disconnected": 0
      }
""" # TODO: Remove this file
from app.data.model.game_model import Game


class PlayerOwnedGames:
    def __init__(self, app_id, playtime_forever):
        self.appid = app_id
        self.playtime_forever = playtime_forever

    # Var declarations
    games = [Game]
