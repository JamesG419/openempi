from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.job_entry import JobEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/{versionId}/probabilistic-matching/model".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["entityId"] = entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, JobEntry]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = JobEntry.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, JobEntry]]:
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
) -> Response[Union[Any, JobEntry]]:
    """Initialize the classification model for the matching algorithm

     This endpoint allows you to initialize the classification model that the particular matching
    algorithm uses to make classification decisions. This needs to be done when the configuration of the
    matching algorithm is initially setup or when the configuration changes. Once the system is running
    in production you should not run this operation since it will overwrite any customization you have
    applied to the configuration of the matching algorithm.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, JobEntry]]
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
) -> Optional[Union[Any, JobEntry]]:
    """Initialize the classification model for the matching algorithm

     This endpoint allows you to initialize the classification model that the particular matching
    algorithm uses to make classification decisions. This needs to be done when the configuration of the
    matching algorithm is initially setup or when the configuration changes. Once the system is running
    in production you should not run this operation since it will overwrite any customization you have
    applied to the configuration of the matching algorithm.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, JobEntry]]
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
) -> Response[Union[Any, JobEntry]]:
    """Initialize the classification model for the matching algorithm

     This endpoint allows you to initialize the classification model that the particular matching
    algorithm uses to make classification decisions. This needs to be done when the configuration of the
    matching algorithm is initially setup or when the configuration changes. Once the system is running
    in production you should not run this operation since it will overwrite any customization you have
    applied to the configuration of the matching algorithm.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, JobEntry]]
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
) -> Optional[Union[Any, JobEntry]]:
    """Initialize the classification model for the matching algorithm

     This endpoint allows you to initialize the classification model that the particular matching
    algorithm uses to make classification decisions. This needs to be done when the configuration of the
    matching algorithm is initially setup or when the configuration changes. Once the system is running
    in production you should not run this operation since it will overwrite any customization you have
    applied to the configuration of the matching algorithm.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, JobEntry]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            entity_id=entity_id,
        )
    ).parsed
