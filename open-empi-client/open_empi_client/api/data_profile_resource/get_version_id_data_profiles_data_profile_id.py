from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.data_profile import DataProfile
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = '1.0',
    data_profile_id: int,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/{versionId}/data-profiles/{dataProfileId}".format(
        client.base_url,versionId=version_id,dataProfileId=data_profile_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DataProfile]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = DataProfile.from_dict(response.json())



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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DataProfile]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: str = '1.0',
    data_profile_id: int,
    *,
    client: Client,

) -> Response[Union[Any, DataProfile]]:
    """Get the data profile

     This endpoint allows you to retrieve the data profile identified by its unique identifier

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):

    Returns:
        Response[Union[Any, DataProfile]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
data_profile_id=data_profile_id,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    version_id: str = '1.0',
    data_profile_id: int,
    *,
    client: Client,

) -> Optional[Union[Any, DataProfile]]:
    """Get the data profile

     This endpoint allows you to retrieve the data profile identified by its unique identifier

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):

    Returns:
        Response[Union[Any, DataProfile]]
    """


    return sync_detailed(
        version_id=version_id,
data_profile_id=data_profile_id,
client=client,

    ).parsed

async def asyncio_detailed(
    version_id: str = '1.0',
    data_profile_id: int,
    *,
    client: Client,

) -> Response[Union[Any, DataProfile]]:
    """Get the data profile

     This endpoint allows you to retrieve the data profile identified by its unique identifier

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):

    Returns:
        Response[Union[Any, DataProfile]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
data_profile_id=data_profile_id,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    version_id: str = '1.0',
    data_profile_id: int,
    *,
    client: Client,

) -> Optional[Union[Any, DataProfile]]:
    """Get the data profile

     This endpoint allows you to retrieve the data profile identified by its unique identifier

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):

    Returns:
        Response[Union[Any, DataProfile]]
    """


    return (await asyncio_detailed(
        version_id=version_id,
data_profile_id=data_profile_id,
client=client,

    )).parsed

