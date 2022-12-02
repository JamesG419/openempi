from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.identifier_update_event import IdentifierUpdateEvent
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    first_record: Union[Unset, None, int] = UNSET,
    max_records: Union[Unset, None, int] = 100,
    remove_records: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/{versionId}/notifications".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["firstRecord"] = first_record

    params["maxRecords"] = max_records

    params["removeRecords"] = remove_records

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List["IdentifierUpdateEvent"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IdentifierUpdateEvent.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List["IdentifierUpdateEvent"]]]:
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
    first_record: Union[Unset, None, int] = UNSET,
    max_records: Union[Unset, None, int] = 100,
    remove_records: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List["IdentifierUpdateEvent"]]]:
    """Retrieve update notification events

     Retrieve update notification events that are stored in the repository. You may use the paging
    parameters to control how many notification events are returned and the starting offset of those
    events. You may also indicate that the notification returned should be deleted from the repository.
    It is highly recommended that you delete notification events after receiving them to prevent them
    from accumulating on the server and negatively affecting server performance.

    Args:
        version_id (str):  Default: '1.0'.
        first_record (Union[Unset, None, int]):
        max_records (Union[Unset, None, int]):  Default: 100.
        remove_records (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List['IdentifierUpdateEvent']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        first_record=first_record,
        max_records=max_records,
        remove_records=remove_records,
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
    first_record: Union[Unset, None, int] = UNSET,
    max_records: Union[Unset, None, int] = 100,
    remove_records: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List["IdentifierUpdateEvent"]]]:
    """Retrieve update notification events

     Retrieve update notification events that are stored in the repository. You may use the paging
    parameters to control how many notification events are returned and the starting offset of those
    events. You may also indicate that the notification returned should be deleted from the repository.
    It is highly recommended that you delete notification events after receiving them to prevent them
    from accumulating on the server and negatively affecting server performance.

    Args:
        version_id (str):  Default: '1.0'.
        first_record (Union[Unset, None, int]):
        max_records (Union[Unset, None, int]):  Default: 100.
        remove_records (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List['IdentifierUpdateEvent']]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        first_record=first_record,
        max_records=max_records,
        remove_records=remove_records,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    first_record: Union[Unset, None, int] = UNSET,
    max_records: Union[Unset, None, int] = 100,
    remove_records: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List["IdentifierUpdateEvent"]]]:
    """Retrieve update notification events

     Retrieve update notification events that are stored in the repository. You may use the paging
    parameters to control how many notification events are returned and the starting offset of those
    events. You may also indicate that the notification returned should be deleted from the repository.
    It is highly recommended that you delete notification events after receiving them to prevent them
    from accumulating on the server and negatively affecting server performance.

    Args:
        version_id (str):  Default: '1.0'.
        first_record (Union[Unset, None, int]):
        max_records (Union[Unset, None, int]):  Default: 100.
        remove_records (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List['IdentifierUpdateEvent']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        first_record=first_record,
        max_records=max_records,
        remove_records=remove_records,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
    first_record: Union[Unset, None, int] = UNSET,
    max_records: Union[Unset, None, int] = 100,
    remove_records: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List["IdentifierUpdateEvent"]]]:
    """Retrieve update notification events

     Retrieve update notification events that are stored in the repository. You may use the paging
    parameters to control how many notification events are returned and the starting offset of those
    events. You may also indicate that the notification returned should be deleted from the repository.
    It is highly recommended that you delete notification events after receiving them to prevent them
    from accumulating on the server and negatively affecting server performance.

    Args:
        version_id (str):  Default: '1.0'.
        first_record (Union[Unset, None, int]):
        max_records (Union[Unset, None, int]):  Default: 100.
        remove_records (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List['IdentifierUpdateEvent']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            first_record=first_record,
            max_records=max_records,
            remove_records=remove_records,
        )
    ).parsed
