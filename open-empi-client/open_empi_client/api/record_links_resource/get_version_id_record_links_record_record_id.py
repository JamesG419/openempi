from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_version_id_record_links_record_record_id_direct import GetVersionIdRecordLinksRecordRecordIdDirect
from ...models.record_link import RecordLink
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: int,
    record_id: str = "1.0",
    *,
    client: Client,
    direct: Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect] = UNSET,
    entity_id: int,
    state: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/{versionId}/record-links/record/{recordId}".format(
        client.base_url, versionId=version_id, recordId=record_id
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_direct: Union[Unset, None, str] = UNSET
    if not isinstance(direct, Unset):
        json_direct = direct.value if direct else None

    params["direct"] = json_direct

    params["entityId"] = entity_id

    params["state"] = state

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List["RecordLink"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = RecordLink.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List["RecordLink"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    version_id: int,
    record_id: str = "1.0",
    *,
    client: Client,
    direct: Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect] = UNSET,
    entity_id: int,
    state: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["RecordLink"]]]:
    """Retrieve record links associated with record

     This endpoint allows you to retrieve record links associated with the record identified by the
    recordId value. You may filter the response to links of a given state such as match or probable
    links.

    Args:
        version_id (int):
        record_id (str):  Default: '1.0'.
        direct (Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect]):
        entity_id (int):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        record_id=record_id,
        client=client,
        direct=direct,
        entity_id=entity_id,
        state=state,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    version_id: int,
    record_id: str = "1.0",
    *,
    client: Client,
    direct: Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect] = UNSET,
    entity_id: int,
    state: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["RecordLink"]]]:
    """Retrieve record links associated with record

     This endpoint allows you to retrieve record links associated with the record identified by the
    recordId value. You may filter the response to links of a given state such as match or probable
    links.

    Args:
        version_id (int):
        record_id (str):  Default: '1.0'.
        direct (Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect]):
        entity_id (int):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    return sync_detailed(
        version_id=version_id,
        record_id=record_id,
        client=client,
        direct=direct,
        entity_id=entity_id,
        state=state,
    ).parsed


async def asyncio_detailed(
    version_id: int,
    record_id: str = "1.0",
    *,
    client: Client,
    direct: Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect] = UNSET,
    entity_id: int,
    state: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, List["RecordLink"]]]:
    """Retrieve record links associated with record

     This endpoint allows you to retrieve record links associated with the record identified by the
    recordId value. You may filter the response to links of a given state such as match or probable
    links.

    Args:
        version_id (int):
        record_id (str):  Default: '1.0'.
        direct (Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect]):
        entity_id (int):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        record_id=record_id,
        client=client,
        direct=direct,
        entity_id=entity_id,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: int,
    record_id: str = "1.0",
    *,
    client: Client,
    direct: Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect] = UNSET,
    entity_id: int,
    state: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, List["RecordLink"]]]:
    """Retrieve record links associated with record

     This endpoint allows you to retrieve record links associated with the record identified by the
    recordId value. You may filter the response to links of a given state such as match or probable
    links.

    Args:
        version_id (int):
        record_id (str):  Default: '1.0'.
        direct (Union[Unset, None, GetVersionIdRecordLinksRecordRecordIdDirect]):
        entity_id (int):
        state (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            record_id=record_id,
            client=client,
            direct=direct,
            entity_id=entity_id,
            state=state,
        )
    ).parsed
