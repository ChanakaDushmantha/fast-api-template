class NoDataFoundException(Exception):
    def __init__(self, message: str):
        self.message = message


class RestClientException(Exception):
    def __init__(self, message: str, status: int):
        self.status = status
        self.message = message


class UnauthorizedException(Exception):
    def __init__(self, message: str, status: int):
        self.status = status
        self.message = message
