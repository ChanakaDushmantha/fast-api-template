from logging import getLogger
from typing import List

import httpx

from exception.exception import UnauthorizedException, RestClientException

logger = getLogger(__name__)


async def get_request(base_url: str, endpoint: str = None, headers: dict = None, params: dict = None):
    async with httpx.AsyncClient() as client:
        url = f"{base_url}{endpoint if endpoint else ''}"
        logger.debug(f"Request URL: {url}{' params: ' + str(params) if params else ''}")
        response = await client.get(url, headers=headers, params=params)
        if response.status_code == 401:
            raise UnauthorizedException(message=response.text, status=response.status_code)
        if response.status_code != 200:
            raise RestClientException(message=response.text, status=response.status_code)
        return response.json()


async def post_request(base_url: str, endpoint: str = None, headers: dict = None, data: dict | List = None):
    async with httpx.AsyncClient() as client:
        url = f"{base_url}{endpoint if endpoint else ''}"
        logger.debug(f"Request URL: {url} data: {data}")
        response = await client.post(url, headers=headers, json=data)
        if response.status_code == 401:
            raise UnauthorizedException(message=response.text, status=response.status_code)
        if response.status_code != 200:
            raise RestClientException(message=response.text, status=response.status_code)
        return response.json()
