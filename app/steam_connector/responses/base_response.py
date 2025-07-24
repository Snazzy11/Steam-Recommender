"""
Holds basic response class
"""
from abc import ABC, abstractmethod
import json
from types import SimpleNamespace

class BaseResponse(ABC):
    """
    Abstract response class for queries to API
    """
    def __init__(self, json_data_string='', error=None) -> None:
        """
        Initialize the base response values
        :param json_data_string: Exact string of JSON data returned from the API
        :param error: Error response from API, if it exists
        """
        self.raw_json = json_data_string or ''
        self.error = error
        self.success = error is None and json_data_string != ''
        self.data = None
        self.pretty_json = ''
        if self.success:
            try:
                self.data = json.loads(json_data_string, object_hook=lambda d: SimpleNamespace(**d))
                self.pretty_json = json.dumps(json.loads(json_data_string), indent=2)
            except json.JSONDecodeError as e:
                self.success = False
                self.error = f"JSON decode error: {e}"
                self.data = None

    def __str__(self):
        return self.pretty_json if self.success else f"<Error: {self.error}>"

"""
self
    data
        response
            game_count: int
            games: {
                000: ...
                001: {
                    appid: int
                    etc.
                }
            }
"""