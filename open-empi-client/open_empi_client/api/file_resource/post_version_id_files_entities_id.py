from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/{versionId}/files/entities/{id}".format(
        client.base_url,versionId=version_id,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "post",
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
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,

) -> Response[Any]:
    """Export an entity into a file

     This endpoint allows you to export an entity definition, creating a file in the process. This is
    useful for backing up the definition of an entity and may be used to either recreate the entity or
    create a clone of the entity after changing the name of the entity in the export file. The id refers
    to the entity that will be exported into a file.

    Args:
        version_id (str):  Default: '1.0'.
        id (int):

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,

) -> Response[Any]:
    """Export an entity into a file

     This endpoint allows you to export an entity definition, creating a file in the process. This is
    useful for backing up the definition of an entity and may be used to either recreate the entity or
    create a clone of the entity after changing the name of the entity in the export file. The id refers
    to the entity that will be exported into a file.

    Args:
        version_id (str):  Default: '1.0'.
        id (int):

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)


