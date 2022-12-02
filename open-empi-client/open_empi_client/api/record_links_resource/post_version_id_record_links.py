from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.record_link import RecordLink
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    json_body: RecordLink,
) -> Dict[str, Any]:
    url = "{}/{versionId}/record-links".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RecordLink]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RecordLink.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RecordLink]]:
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
    json_body: RecordLink,
) -> Response[Union[Any, RecordLink]]:
    """Add a record link

     This endpoint allows you to add a new record link to the system. The record link must be associated
    with a known entity and the two records that it links must already exist in the repository of the
    entity to which the link is being added.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (RecordLink):

    Returns:
        Response[Union[Any, RecordLink]]
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
    json_body: RecordLink,
) -> Optional[Union[Any, RecordLink]]:
    """Add a record link

     This endpoint allows you to add a new record link to the system. The record link must be associated
    with a known entity and the two records that it links must already exist in the repository of the
    entity to which the link is being added.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (RecordLink):

    Returns:
        Response[Union[Any, RecordLink]]
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
    json_body: RecordLink,
) -> Response[Union[Any, RecordLink]]:
    """Add a record link

     This endpoint allows you to add a new record link to the system. The record link must be associated
    with a known entity and the two records that it links must already exist in the repository of the
    entity to which the link is being added.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (RecordLink):

    Returns:
        Response[Union[Any, RecordLink]]
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
    json_body: RecordLink,
) -> Optional[Union[Any, RecordLink]]:
    """Add a record link

     This endpoint allows you to add a new record link to the system. The record link must be associated
    with a known entity and the two records that it links must already exist in the repository of the
    entity to which the link is being added.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (RecordLink):

    Returns:
        Response[Union[Any, RecordLink]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
