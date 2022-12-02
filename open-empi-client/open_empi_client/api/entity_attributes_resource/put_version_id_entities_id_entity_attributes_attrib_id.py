from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_attribute import EntityAttribute
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = '1.0',
    id: int,
    attrib_id: int,
    *,
    client: Client,
    json_body: EntityAttribute,

) -> Dict[str, Any]:
    url = "{}/{versionId}/entities/{id}/entity-attributes/{attribId}".format(
        client.base_url,versionId=version_id,id=id,attribId=attrib_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List['EntityAttribute']]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in (_response_200):
            response_200_item = EntityAttribute.from_dict(response_200_item_data)



            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List['EntityAttribute']]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: str = '1.0',
    id: int,
    attrib_id: int,
    *,
    client: Client,
    json_body: EntityAttribute,

) -> Response[Union[Any, List['EntityAttribute']]]:
    """Update an entity attribute

     This endpoint allows you to update the definition of an entity attribute

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        attrib_id (int):
        json_body (EntityAttribute):

    Returns:
        Response[Union[Any, List['EntityAttribute']]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
attrib_id=attrib_id,
client=client,
json_body=json_body,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)

def sync(
    version_id: str = '1.0',
    id: int,
    attrib_id: int,
    *,
    client: Client,
    json_body: EntityAttribute,

) -> Optional[Union[Any, List['EntityAttribute']]]:
    """Update an entity attribute

     This endpoint allows you to update the definition of an entity attribute

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        attrib_id (int):
        json_body (EntityAttribute):

    Returns:
        Response[Union[Any, List['EntityAttribute']]]
    """


    return sync_detailed(
        version_id=version_id,
id=id,
attrib_id=attrib_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    version_id: str = '1.0',
    id: int,
    attrib_id: int,
    *,
    client: Client,
    json_body: EntityAttribute,

) -> Response[Union[Any, List['EntityAttribute']]]:
    """Update an entity attribute

     This endpoint allows you to update the definition of an entity attribute

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        attrib_id (int):
        json_body (EntityAttribute):

    Returns:
        Response[Union[Any, List['EntityAttribute']]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
attrib_id=attrib_id,
client=client,
json_body=json_body,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)

async def asyncio(
    version_id: str = '1.0',
    id: int,
    attrib_id: int,
    *,
    client: Client,
    json_body: EntityAttribute,

) -> Optional[Union[Any, List['EntityAttribute']]]:
    """Update an entity attribute

     This endpoint allows you to update the definition of an entity attribute

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        attrib_id (int):
        json_body (EntityAttribute):

    Returns:
        Response[Union[Any, List['EntityAttribute']]]
    """


    return (await asyncio_detailed(
        version_id=version_id,
id=id,
attrib_id=attrib_id,
client=client,
json_body=json_body,

    )).parsed

