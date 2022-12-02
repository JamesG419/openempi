from http import HTTPStatus
from typing import Any, Dict

import httpx

from ...client import Client
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/{versionId}/notifications/getNotificationCount".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Response[Any]:
    """Your GET endpoint

     Returns the total number of notifications that are stored in the repository.

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Response[Any]:
    """Your GET endpoint

     Returns the total number of notifications that are stored in the repository.

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
