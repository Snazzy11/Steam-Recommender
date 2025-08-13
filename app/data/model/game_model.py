"""
Data for a single game
"""
from dataclasses import dataclass #, field

@dataclass(frozen=True, init=True)
class Game: # TODO: How can I make fields optional, or else able to be excluded if they dont exist in the pulled game?
    """
    Data model for a single game
    """
    appid: str
    name: str
    rtime_last_played: int

    playtime: int
    playtime_mac: int
    playtime_linux: int
    playtime_deck: int
    playtime_windows: int
    playtime_disconnected: int

    img_icon_url: str
