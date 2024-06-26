from logging import getLogger

import httpx

from exception.exception import UnauthorizedException, RestClientException

logger = getLogger(__name__)


async def get_request(base_url: str, endpoint: str = None, headers: dict = None, params: dict = None):
    """
    Make an asynchronous GET request to the specified endpoint.

    Args:
        base_url (str): The base URL of the API.
        endpoint (str, optional): The specific endpoint to append to the base URL. Defaults to None.
        headers (dict, optional): Headers to include in the request. Defaults to None.
        params (dict, optional): Query parameters to include in the request. Defaults to None.

    Returns:
        dict: The JSON response from the API.

    Raises:
        UnauthorizedException: If the response status code is 401.
        RestClientException: If the response status code is not 200.
    """
    async with httpx.AsyncClient() as client:
        url = f"{base_url}{endpoint if endpoint else ''}"
        logger.debug(f"Request URL: {url}{' params: ' + str(params) if params else ''}")
        response = await client.get(url, headers=headers, params=params)
        if response.status_code == 401:
            raise UnauthorizedException(message=response.text, status=response.status_code)
        if response.status_code != 200:
            raise RestClientException(message=response.text, status=response.status_code)
        return response.json()


async def post_request(base_url: str, endpoint: str = None, headers: dict = None, data: dict | list = None):
    """
    Make an asynchronous POST request to the specified endpoint.

    Args:
        base_url (str): The base URL of the API.
        endpoint (str, optional): The specific endpoint to append to the base URL. Defaults to None.
        headers (dict, optional): Headers to include in the request. Defaults to None.
        data (dict | list, optional): The JSON payload to include in the request body. Defaults to None.

    Returns:
        dict: The JSON response from the API.

    Raises:
        UnauthorizedException: If the response status code is 401.
        RestClientException: If the response status code is not 200.
    """
    async with httpx.AsyncClient() as client:
        url = f"{base_url}{endpoint if endpoint else ''}"
        logger.debug(f"Request URL: {url} data: {data}")
        response = await client.post(url, headers=headers, json=data)
        if response.status_code == 401:
            raise UnauthorizedException(message=response.text, status=response.status_code)
        if response.status_code != 200:
            raise RestClientException(message=response.text, status=response.status_code)
        return response.json()

