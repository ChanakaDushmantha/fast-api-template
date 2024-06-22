from logging import getLogger

from fastapi import FastAPI, Request
from sqlalchemy.exc import IntegrityError
from starlette.responses import JSONResponse
from starlette.status import HTTP_400_BAD_REQUEST

from exception.exception import NoDataFoundException, RestClientException, UnauthorizedException

logger = getLogger(__name__)


def add_exception_handler(app: FastAPI):
    @app.exception_handler(Exception)
    async def handle_generic_exception(request: Request, exc: Exception):
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={'success': False,
                                     'message': str(exc)})

    @app.exception_handler(NoDataFoundException)
    async def handle_no_data_found_exception(request: Request, exc: NoDataFoundException):
        logger.error(exc)
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={'success': False,
                                     'message': exc.message})

    @app.exception_handler(IntegrityError)
    async def handle_integrity_error(request: Request, exc: IntegrityError):
        logger.exception(exc)
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={'success': False,
                                     'message': str(exc)})

    @app.exception_handler(RestClientException)
    async def handle_no_data_found_exception(request: Request, exc: RestClientException):
        logger.error(exc.message)
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={'success': False,
                                     'message': exc.message,
                                     'status_code': exc.status})

    @app.exception_handler(UnauthorizedException)
    async def handle_unauthorized_exception(request: Request, exc: UnauthorizedException):
        logger.error(exc.message)
        return JSONResponse(status_code=HTTP_400_BAD_REQUEST,
                            content={'success': False,
                                     'message': exc.message,
                                     'status_code': exc.status})
