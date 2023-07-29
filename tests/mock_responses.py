"""Simple mock responses definitions."""
from unittest import mock
from aiohttp import ClientResponse

class MockResponseDict(dict):
    """Class for mock request response."""

    def __init__(self, json_data, status_code, headers={}, raw_data=None):
        """Initialize mock get response."""
        self.json_data = json_data
        self.status = status_code
        self.raw_data = raw_data
        self.reason = "foobar"
        self.headers = headers
        self.read = mock.AsyncMock(return_value=self.raw_data)
 
class MockResponseClient(ClientResponse):
    """Class for mock request response."""

    def __init__(self, json_data, status_code, headers={}, raw_data=None):
        """Initialize mock get response."""
        self.json_data = json_data
        self.status = status_code
        self.raw_data = raw_data
        self.reason = "foobar"
        self.read = mock.AsyncMock(return_value=self.raw_data)
 
    async def json(self):
        """Return json data from get_request."""
        return self.json_data
