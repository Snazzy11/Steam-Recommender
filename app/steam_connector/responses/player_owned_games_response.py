"""
Holds the response class for the get_owned_games method
"""
from app.steam_connector.responses.base_response import BaseResponse

# TODO: Allow/Disallow the 'include_appinfo' bool which will retrive additional data about each game
# TODO: Create an array of miniature 'game' objects

class PlayerGetOwnedGamesResponse(BaseResponse):
    def __init__(self, json_response: str, error=None) -> None:
        super().__init__(json_response, error)
        self.set_vars()

# TODO this data should acutally be for each item, and should not exist here
    # Var declarations
    appid: str
    playtime_forever: int # Play times are in minutes
    playtime_windows: int
    playtime_linux: int
    playtime_mac: int
    playtime_deck: int # This one does NOT always exist
    rtime_last_played: int # What is rtime? Relative time?
    playtime_disconnected: int

    # Only do if base response was successful
    def set_vars(self) -> None:
        print('Print test: ', self.data)
        appid = getattr(self.data.)
