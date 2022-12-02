from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.file import File
from ...types import File, Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    multipart_data: File,
) -> Dict[str, Any]:
    url = "{}/{versionId}/files".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, File]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, File]]:
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
    multipart_data: File,
) -> Response[Union[Any, File]]:
    """Import a new file

     This endpoint allows you upload a new file onto the server, creating an instance of a file resource
    in the process

    Args:
        version_id (str):  Default: '1.0'.
        multipart_data (File):

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        multipart_data=multipart_data,
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
    multipart_data: File,
) -> Optional[Union[Any, File]]:
    """Import a new file

     This endpoint allows you upload a new file onto the server, creating an instance of a file resource
    in the process

    Args:
        version_id (str):  Default: '1.0'.
        multipart_data (File):

    Returns:
        Response[Union[Any, File]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    multipart_data: File,
) -> Response[Union[Any, File]]:
    """Import a new file

     This endpoint allows you upload a new file onto the server, creating an instance of a file resource
    in the process

    Args:
        version_id (str):  Default: '1.0'.
        multipart_data (File):

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
    multipart_data: File,
) -> Optional[Union[Any, File]]:
    """Import a new file

     This endpoint allows you upload a new file onto the server, creating an instance of a file resource
    in the process

    Args:
        version_id (str):  Default: '1.0'.
        multipart_data (File):

    Returns:
        Response[Union[Any, File]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
