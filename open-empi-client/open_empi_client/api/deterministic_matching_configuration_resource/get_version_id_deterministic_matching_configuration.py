from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_version_id_deterministic_matching_configuration_response_200_item import (
    GetVersionIdDeterministicMatchingConfigurationResponse200Item,
)
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Dict[str, Any]:
    url = "{}/{versionId}/deterministic-matching/configuration".format(client.base_url, versionId=version_id)

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


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, List["GetVersionIdDeterministicMatchingConfigurationResponse200Item"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GetVersionIdDeterministicMatchingConfigurationResponse200Item.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, List["GetVersionIdDeterministicMatchingConfigurationResponse200Item"]]]:
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
) -> Response[Union[Any, List["GetVersionIdDeterministicMatchingConfigurationResponse200Item"]]]:
    """Get the deterministic matching service configuration

     This endpoint allows you to retrieve the current configuration of the deterministic matching
    service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['GetVersionIdDeterministicMatchingConfigurationResponse200Item']]]
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
) -> Optional[Union[Any, List["GetVersionIdDeterministicMatchingConfigurationResponse200Item"]]]:
    """Get the deterministic matching service configuration

     This endpoint allows you to retrieve the current configuration of the deterministic matching
    service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['GetVersionIdDeterministicMatchingConfigurationResponse200Item']]]
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
) -> Response[Union[Any, List["GetVersionIdDeterministicMatchingConfigurationResponse200Item"]]]:
    """Get the deterministic matching service configuration

     This endpoint allows you to retrieve the current configuration of the deterministic matching
    service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['GetVersionIdDeterministicMatchingConfigurationResponse200Item']]]
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
) -> Optional[Union[Any, List["GetVersionIdDeterministicMatchingConfigurationResponse200Item"]]]:
    """Get the deterministic matching service configuration

     This endpoint allows you to retrieve the current configuration of the deterministic matching
    service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Union[Any, List['GetVersionIdDeterministicMatchingConfigurationResponse200Item']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            entity_id=entity_id,
        )
    ).parsed
