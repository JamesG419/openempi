from http import HTTPStatus
from typing import Any, Dict

import httpx

from ...client import Client
from ...models.authentication_request import AuthenticationRequest
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: AuthenticationRequest,
) -> Dict[str, Any]:
    url = "{}/security-resource/authenticate".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    *,
    client: Client,
    json_body: AuthenticationRequest,
) -> Response[Any]:
    """Authenticate a user

     This endpoint allows you to authenticate a user using a username and password. You must first
    authenticate a user with OpenEMPI and receive a session key before you attempt any other operation
    that requires a session key. Once you have successfully received a session key back you must provide
    it in subsequent REST API requests using the header OPENEMPI_SESSION_KEY.

    Args:
        json_body (AuthenticationRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    *,
    client: Client,
    json_body: AuthenticationRequest,
) -> Response[Any]:
    """Authenticate a user

     This endpoint allows you to authenticate a user using a username and password. You must first
    authenticate a user with OpenEMPI and receive a session key before you attempt any other operation
    that requires a session key. Once you have successfully received a session key back you must provide
    it in subsequent REST API requests using the header OPENEMPI_SESSION_KEY.

    Args:
        json_body (AuthenticationRequest):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
