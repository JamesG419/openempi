from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.custom_field import CustomField
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Dict[str, Any]:
    url = "{}/{versionId}/custom-fields".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["entityId"] = entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List["CustomField"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CustomField.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List["CustomField"]]]:
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
    entity_id: int,
) -> Response[Union[Any, List["CustomField"]]]:
    """Retrieve the list of custom fields of an entity

     This endpoint allows you to retrieve the list of custom fields defined in association with an entity
    that is located by its unique identifier.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['CustomField']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
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
    entity_id: int,
) -> Optional[Union[Any, List["CustomField"]]]:
    """Retrieve the list of custom fields of an entity

     This endpoint allows you to retrieve the list of custom fields defined in association with an entity
    that is located by its unique identifier.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['CustomField']]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Response[Union[Any, List["CustomField"]]]:
    """Retrieve the list of custom fields of an entity

     This endpoint allows you to retrieve the list of custom fields defined in association with an entity
    that is located by its unique identifier.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['CustomField']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Optional[Union[Any, List["CustomField"]]]:
    """Retrieve the list of custom fields of an entity

     This endpoint allows you to retrieve the list of custom fields defined in association with an entity
    that is located by its unique identifier.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['CustomField']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            entity_id=entity_id,
        )
    ).parsed