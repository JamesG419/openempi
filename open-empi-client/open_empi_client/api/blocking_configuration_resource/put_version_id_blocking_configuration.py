from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.blocking_configuration import BlockingConfiguration
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    json_body: BlockingConfiguration,
) -> Dict[str, Any]:
    url = "{}/{versionId}/blocking-configuration".format(client.base_url, versionId=version_id)

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
    json_body: BlockingConfiguration,
) -> Response[Union[Any, BlockingConfiguration]]:
    """Update the blocking service configuration

     This endpoint allows you to update the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (BlockingConfiguration):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        json_body=json_body,
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
    json_body: BlockingConfiguration,
) -> Optional[Union[Any, BlockingConfiguration]]:
    """Update the blocking service configuration

     This endpoint allows you to update the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (BlockingConfiguration):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    json_body: BlockingConfiguration,
) -> Response[Union[Any, BlockingConfiguration]]:
    """Update the blocking service configuration

     This endpoint allows you to update the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (BlockingConfiguration):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
    json_body: BlockingConfiguration,
) -> Optional[Union[Any, BlockingConfiguration]]:
    """Update the blocking service configuration

     This endpoint allows you to update the current configuration of the blocking service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (BlockingConfiguration):

    Returns:
        Response[Union[Any, BlockingConfiguration]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
