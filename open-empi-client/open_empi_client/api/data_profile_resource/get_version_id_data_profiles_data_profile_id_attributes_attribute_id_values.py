from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.data_profile_attribute_value import DataProfileAttributeValue
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = '1.0',
    data_profile_id: int,
    attribute_id: int,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/{versionId}/data-profiles/{dataProfileId}/attributes/{attributeId}/values".format(
        client.base_url,versionId=version_id,dataProfileId=data_profile_id,attributeId=attribute_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[List['DataProfileAttributeValue']]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = DataProfileAttributeValue.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[List['DataProfileAttributeValue']]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: str = '1.0',
    data_profile_id: int,
    attribute_id: int,
    *,
    client: Client,

) -> Response[List['DataProfileAttributeValue']]:
    """Your GET endpoint

     This endpoint allows you to retrieve the list of values that occur frequently for a given data
    profile attribute along with its frequency of occurrence for each such value. You must specify the
    data profile and the specific attributes whose frequent value distribution you want to receive.

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):
        attribute_id (int):

    Returns:
        Response[List['DataProfileAttributeValue']]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
data_profile_id=data_profile_id,
attribute_id=attribute_id,
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
    attribute_id: int,
    *,
    client: Client,

) -> Optional[List['DataProfileAttributeValue']]:
    """Your GET endpoint

     This endpoint allows you to retrieve the list of values that occur frequently for a given data
    profile attribute along with its frequency of occurrence for each such value. You must specify the
    data profile and the specific attributes whose frequent value distribution you want to receive.

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):
        attribute_id (int):

    Returns:
        Response[List['DataProfileAttributeValue']]
    """


    return sync_detailed(
        version_id=version_id,
data_profile_id=data_profile_id,
attribute_id=attribute_id,
client=client,

    ).parsed

async def asyncio_detailed(
    version_id: str = '1.0',
    data_profile_id: int,
    attribute_id: int,
    *,
    client: Client,

) -> Response[List['DataProfileAttributeValue']]:
    """Your GET endpoint

     This endpoint allows you to retrieve the list of values that occur frequently for a given data
    profile attribute along with its frequency of occurrence for each such value. You must specify the
    data profile and the specific attributes whose frequent value distribution you want to receive.

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):
        attribute_id (int):

    Returns:
        Response[List['DataProfileAttributeValue']]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
data_profile_id=data_profile_id,
attribute_id=attribute_id,
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
    attribute_id: int,
    *,
    client: Client,

) -> Optional[List['DataProfileAttributeValue']]:
    """Your GET endpoint

     This endpoint allows you to retrieve the list of values that occur frequently for a given data
    profile attribute along with its frequency of occurrence for each such value. You must specify the
    data profile and the specific attributes whose frequent value distribution you want to receive.

    Args:
        version_id (str):  Default: '1.0'.
        data_profile_id (int):
        attribute_id (int):

    Returns:
        Response[List['DataProfileAttributeValue']]
    """


    return (await asyncio_detailed(
        version_id=version_id,
data_profile_id=data_profile_id,
attribute_id=attribute_id,
client=client,

    )).parsed

