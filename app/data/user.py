"""
Holds User class
"""

from app.data.model.game_model import Game


class User:
    """
    A Steam User
    """
    owned_games = [Game]
    steam_id: str

    def __init__(self, steam_id: str, owned_games: list[Game] = None):
        self.steam_id = steam_id
        self.owned_games = owned_games or []

    def get_steam_id(self) -> str:
        """
        Get user's steam id        :return:
        """
        return self.steam_id

    def set_owned_games(self, games: list[Game]) -> None:
        """
        Set list of owned games, of type Game
        :param games: List of Game objects
        :return:
        """
        # TODO: Test that the list is correct, although MyPy should catch this
        self.owned_games = games
