from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.entity_attribute_group import EntityAttributeGroup
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = '1.0',
    id: int,
    entity_attribute_group_id: int,
    *,
    client: Client,
    json_body: EntityAttributeGroup,

) -> Dict[str, Any]:
    url = "{}/{versionId}/entities/{id}/attribute-groups/{entityAttributeGroupId}".format(
        client.base_url,versionId=version_id,id=id,entityAttributeGroupId=entity_attribute_group_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, EntityAttributeGroup]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EntityAttributeGroup.from_dict(response.json())



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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, EntityAttributeGroup]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: str = '1.0',
    id: int,
    entity_attribute_group_id: int,
    *,
    client: Client,
    json_body: EntityAttributeGroup,

) -> Response[Union[Any, EntityAttributeGroup]]:
    """Update an attribute group of an entity definition

     This endpoint allows you to update an attribute group of an existing entity definition

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        entity_attribute_group_id (int):
        json_body (EntityAttributeGroup):

    Returns:
        Response[Union[Any, EntityAttributeGroup]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
entity_attribute_group_id=entity_attribute_group_id,
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
    entity_attribute_group_id: int,
    *,
    client: Client,
    json_body: EntityAttributeGroup,

) -> Optional[Union[Any, EntityAttributeGroup]]:
    """Update an attribute group of an entity definition

     This endpoint allows you to update an attribute group of an existing entity definition

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        entity_attribute_group_id (int):
        json_body (EntityAttributeGroup):

    Returns:
        Response[Union[Any, EntityAttributeGroup]]
    """


    return sync_detailed(
        version_id=version_id,
id=id,
entity_attribute_group_id=entity_attribute_group_id,
client=client,
json_body=json_body,

    ).parsed

async def asyncio_detailed(
    version_id: str = '1.0',
    id: int,
    entity_attribute_group_id: int,
    *,
    client: Client,
    json_body: EntityAttributeGroup,

) -> Response[Union[Any, EntityAttributeGroup]]:
    """Update an attribute group of an entity definition

     This endpoint allows you to update an attribute group of an existing entity definition

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        entity_attribute_group_id (int):
        json_body (EntityAttributeGroup):

    Returns:
        Response[Union[Any, EntityAttributeGroup]]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
id=id,
entity_attribute_group_id=entity_attribute_group_id,
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
    entity_attribute_group_id: int,
    *,
    client: Client,
    json_body: EntityAttributeGroup,

) -> Optional[Union[Any, EntityAttributeGroup]]:
    """Update an attribute group of an entity definition

     This endpoint allows you to update an attribute group of an existing entity definition

    Args:
        version_id (str):  Default: '1.0'.
        id (int):
        entity_attribute_group_id (int):
        json_body (EntityAttributeGroup):

    Returns:
        Response[Union[Any, EntityAttributeGroup]]
    """


    return (await asyncio_detailed(
        version_id=version_id,
id=id,
entity_attribute_group_id=entity_attribute_group_id,
client=client,
json_body=json_body,

    )).parsed

