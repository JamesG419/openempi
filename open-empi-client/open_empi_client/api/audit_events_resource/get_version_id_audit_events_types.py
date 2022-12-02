from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.audit_event_type import AuditEventType
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/{versionId}/audit-events/types".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List["AuditEventType"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AuditEventType.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List["AuditEventType"]]]:
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
) -> Response[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event types.

     This endpoint allows you to retrieve the list of audit event types that the system records

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
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
) -> Optional[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event types.

     This endpoint allows you to retrieve the list of audit event types that the system records

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Response[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event types.

     This endpoint allows you to retrieve the list of audit event types that the system records

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
) -> Optional[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event types.

     This endpoint allows you to retrieve the list of audit event types that the system records

    Args:
        version_id (str):  Default: '1.0'.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
        )
    ).parsed
