from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.blocking_configuration import BlockingConfiguration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/{versionId}/blocking-configuration".format(client.base_url, versionId=version_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, BlockingConfiguration]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BlockingConfiguration.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, BlockingConfiguration]]:
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
    entity_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, BlockingConfiguration]]:
    """Get the blocking service configuration

     This endpoint allows you to retrieve the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
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
    entity_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, BlockingConfiguration]]:
    """Get the blocking service configuration

     This endpoint allows you to retrieve the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
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
    entity_id: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, BlockingConfiguration]]:
    """Get the blocking service configuration

     This endpoint allows you to retrieve the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
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
    entity_id: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, BlockingConfiguration]]:
    """Get the blocking service configuration

     This endpoint allows you to retrieve the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            entity_id=entity_id,
        )
    ).parsed
