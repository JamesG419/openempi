from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity import Entity
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,
    purge: Union[Unset, None, bool] = True,

) -> Dict[str, Any]:
    url = "{}/{versionId}/entities/{id}".format(
        client.base_url,versionId=version_id,id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    params: Dict[str, Any] = {}
    params["purge"] = purge



    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}


    

    

    return {
	    "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Entity]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = Entity.from_dict(response.json())



        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Entity]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,
    purge: Union[Unset, None, bool] = True,

) -> Response[Union[Any, Entity]]:
    """Delete the entity by its id

     This endpoint allows you to delete an entity definition using its unique identifier. Note that this
    will not delete the database directory that supports this entity and this must bedone manually after
    the server has been shutdown.

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        purge (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[Any, Entity]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
client=client,
purge=purge,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,
    purge: Union[Unset, None, bool] = True,

) -> Optional[Union[Any, Entity]]:
    """Delete the entity by its id

     This endpoint allows you to delete an entity definition using its unique identifier. Note that this
    will not delete the database directory that supports this entity and this must bedone manually after
    the server has been shutdown.

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        purge (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[Any, Entity]]
    """


    return sync_detailed(
        version_id=version_id,
id=id,
client=client,
purge=purge,

    ).parsed

async def asyncio_detailed(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,
    purge: Union[Unset, None, bool] = True,

) -> Response[Union[Any, Entity]]:
    """Delete the entity by its id

     This endpoint allows you to delete an entity definition using its unique identifier. Note that this
    will not delete the database directory that supports this entity and this must bedone manually after
    the server has been shutdown.

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        purge (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[Any, Entity]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
client=client,
purge=purge,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    version_id: str = '1.0',
    id: int,
    *,
    client: Client,
    purge: Union[Unset, None, bool] = True,

) -> Optional[Union[Any, Entity]]:
    """Delete the entity by its id

     This endpoint allows you to delete an entity definition using its unique identifier. Note that this
    will not delete the database directory that supports this entity and this must bedone manually after
    the server has been shutdown.

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        purge (Union[Unset, None, bool]):  Default: True.

    Returns:
        Response[Union[Any, Entity]]
    """


    return (await asyncio_detailed(
        version_id=version_id,
id=id,
client=client,
purge=purge,

    )).parsed

