from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.audit_event_type import AuditEventType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    end_date: Union[Unset, None, str] = UNSET,
    entity_id: int,
    event_types: Union[Unset, None, str] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = 100,
    start_date: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/{versionId}/audit-events".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["endDate"] = end_date

    params["entityId"] = entity_id

    params["eventTypes"] = event_types

    params["firstResult"] = first_result

    params["maxResults"] = max_results

    params["startDate"] = start_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
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
    end_date: Union[Unset, None, str] = UNSET,
    entity_id: int,
    event_types: Union[Unset, None, str] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = 100,
    start_date: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event

     This endpoint allows you to retrieve the list of audit events that satisfy the request criteria
    specified
    in the request. You may filter the list of audit events returned using the start date, end date, and
    event types. The endpoint also allows you to page through the requests using the paging
    parameters. The start and end dates should be in the format YYYYMMDD and the event types
    should be specified as a comma separated list of event type codes (e.g.: 101,102).

    Args:
        version_id (str):  Default: '1.0'.
        end_date (Union[Unset, None, str]):  Example: 20221231.
        entity_id (int):
        event_types (Union[Unset, None, str]):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        start_date (Union[Unset, None, str]):  Example: 20221231.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        end_date=end_date,
        entity_id=entity_id,
        event_types=event_types,
        first_result=first_result,
        max_results=max_results,
        start_date=start_date,
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
    end_date: Union[Unset, None, str] = UNSET,
    entity_id: int,
    event_types: Union[Unset, None, str] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = 100,
    start_date: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event

     This endpoint allows you to retrieve the list of audit events that satisfy the request criteria
    specified
    in the request. You may filter the list of audit events returned using the start date, end date, and
    event types. The endpoint also allows you to page through the requests using the paging
    parameters. The start and end dates should be in the format YYYYMMDD and the event types
    should be specified as a comma separated list of event type codes (e.g.: 101,102).

    Args:
        version_id (str):  Default: '1.0'.
        end_date (Union[Unset, None, str]):  Example: 20221231.
        entity_id (int):
        event_types (Union[Unset, None, str]):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        start_date (Union[Unset, None, str]):  Example: 20221231.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        end_date=end_date,
        entity_id=entity_id,
        event_types=event_types,
        first_result=first_result,
        max_results=max_results,
        start_date=start_date,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    end_date: Union[Unset, None, str] = UNSET,
    entity_id: int,
    event_types: Union[Unset, None, str] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = 100,
    start_date: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event

     This endpoint allows you to retrieve the list of audit events that satisfy the request criteria
    specified
    in the request. You may filter the list of audit events returned using the start date, end date, and
    event types. The endpoint also allows you to page through the requests using the paging
    parameters. The start and end dates should be in the format YYYYMMDD and the event types
    should be specified as a comma separated list of event type codes (e.g.: 101,102).

    Args:
        version_id (str):  Default: '1.0'.
        end_date (Union[Unset, None, str]):  Example: 20221231.
        entity_id (int):
        event_types (Union[Unset, None, str]):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        start_date (Union[Unset, None, str]):  Example: 20221231.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        end_date=end_date,
        entity_id=entity_id,
        event_types=event_types,
        first_result=first_result,
        max_results=max_results,
        start_date=start_date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
    end_date: Union[Unset, None, str] = UNSET,
    entity_id: int,
    event_types: Union[Unset, None, str] = UNSET,
    first_result: Union[Unset, None, int] = UNSET,
    max_results: Union[Unset, None, int] = 100,
    start_date: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["AuditEventType"]]]:
    """Get the list of audit event

     This endpoint allows you to retrieve the list of audit events that satisfy the request criteria
    specified
    in the request. You may filter the list of audit events returned using the start date, end date, and
    event types. The endpoint also allows you to page through the requests using the paging
    parameters. The start and end dates should be in the format YYYYMMDD and the event types
    should be specified as a comma separated list of event type codes (e.g.: 101,102).

    Args:
        version_id (str):  Default: '1.0'.
        end_date (Union[Unset, None, str]):  Example: 20221231.
        entity_id (int):
        event_types (Union[Unset, None, str]):
        first_result (Union[Unset, None, int]):
        max_results (Union[Unset, None, int]):  Default: 100.
        start_date (Union[Unset, None, str]):  Example: 20221231.

    Returns:
        Response[Union[Any, List['AuditEventType']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            end_date=end_date,
            entity_id=entity_id,
            event_types=event_types,
            first_result=first_result,
            max_results=max_results,
            start_date=start_date,
        )
    ).parsed
