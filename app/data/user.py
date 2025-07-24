
class User:
    owned_game_ids = [int]
    steam_id: str
    def __init__(self, steam_id: str | int):
        self.steam_id = str(steam_id)

    def get_steam_id(self) -> str:
        return self.steam_id