from http import HTTPStatus
from typing import Any, Dict, List, Optional

import httpx

from ...client import Client
from ...models.file import File
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/{versionId}/files".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List["File"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = File.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List["File"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Response[List["File"]]:
    """Retrieve all the user file entries

     This endpoint allows you to retrieve all the user file entries from the system

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[List['File']]
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


def sync(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Optional[List["File"]]:
    """Retrieve all the user file entries

     This endpoint allows you to retrieve all the user file entries from the system

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[List['File']]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Response[List["File"]]:
    """Retrieve all the user file entries

     This endpoint allows you to retrieve all the user file entries from the system

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[List['File']]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Optional[List["File"]]:
    """Retrieve all the user file entries

     This endpoint allows you to retrieve all the user file entries from the system

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[List['File']]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
        )
    ).parsed
