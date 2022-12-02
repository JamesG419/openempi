from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_version_id_record_links_state import GetVersionIdRecordLinksState
from ...models.record_link import RecordLink
from ...types import UNSET, Response, Unset


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
    first_result: Union[Unset, None, int] = UNSET,
    key_val: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, int] = 10,
    state: Union[Unset, None, GetVersionIdRecordLinksState] = GetVersionIdRecordLinksState.M,
) -> Dict[str, Any]:
    url = "{}/{versionId}/record-links".format(client.base_url, versionId=version_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["entityId"] = entity_id

    params["firstResult"] = first_result

    params["keyVal"] = key_val

    params["maxResults"] = max_results

    json_state: Union[Unset, None, str] = UNSET
    if not isinstance(state, Unset):
        json_state = state.value if state else None

    params["state"] = json_state

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
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
    first_result: Union[Unset, None, int] = UNSET,
    key_val: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, int] = 10,
    state: Union[Unset, None, GetVersionIdRecordLinksState] = GetVersionIdRecordLinksState.M,
) -> Response[Union[Any, List["RecordLink"]]]:
    """Retrieve record links from entity

     This endpoint allows you to retrieve all the known record links between records of an entity. You
    can filter the record links returned by state otherwise only links of match state are returned. The
    possible values are 'M' for match links, 'P' for probable links and 'A' for links of all states. You
    can also page through the links in the repository using the parameters 'firstResult' and
    'maxResults'.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):
        first_result (Union[Unset, None, int]):
        key_val (Union[Unset, None, str]):
        max_results (Union[Unset, None, int]):  Default: 10.
        state (Union[Unset, None, GetVersionIdRecordLinksState]):  Default:
            GetVersionIdRecordLinksState.M.

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
        first_result=first_result,
        key_val=key_val,
        max_results=max_results,
        state=state,
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
    first_result: Union[Unset, None, int] = UNSET,
    key_val: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, int] = 10,
    state: Union[Unset, None, GetVersionIdRecordLinksState] = GetVersionIdRecordLinksState.M,
) -> Optional[Union[Any, List["RecordLink"]]]:
    """Retrieve record links from entity

     This endpoint allows you to retrieve all the known record links between records of an entity. You
    can filter the record links returned by state otherwise only links of match state are returned. The
    possible values are 'M' for match links, 'P' for probable links and 'A' for links of all states. You
    can also page through the links in the repository using the parameters 'firstResult' and
    'maxResults'.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):
        first_result (Union[Unset, None, int]):
        key_val (Union[Unset, None, str]):
        max_results (Union[Unset, None, int]):  Default: 10.
        state (Union[Unset, None, GetVersionIdRecordLinksState]):  Default:
            GetVersionIdRecordLinksState.M.

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    return sync_detailed(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
        first_result=first_result,
        key_val=key_val,
        max_results=max_results,
        state=state,
    ).parsed


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
    first_result: Union[Unset, None, int] = UNSET,
    key_val: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, int] = 10,
    state: Union[Unset, None, GetVersionIdRecordLinksState] = GetVersionIdRecordLinksState.M,
) -> Response[Union[Any, List["RecordLink"]]]:
    """Retrieve record links from entity

     This endpoint allows you to retrieve all the known record links between records of an entity. You
    can filter the record links returned by state otherwise only links of match state are returned. The
    possible values are 'M' for match links, 'P' for probable links and 'A' for links of all states. You
    can also page through the links in the repository using the parameters 'firstResult' and
    'maxResults'.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):
        first_result (Union[Unset, None, int]):
        key_val (Union[Unset, None, str]):
        max_results (Union[Unset, None, int]):  Default: 10.
        state (Union[Unset, None, GetVersionIdRecordLinksState]):  Default:
            GetVersionIdRecordLinksState.M.

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
        first_result=first_result,
        key_val=key_val,
        max_results=max_results,
        state=state,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
    first_result: Union[Unset, None, int] = UNSET,
    key_val: Union[Unset, None, str] = UNSET,
    max_results: Union[Unset, None, int] = 10,
    state: Union[Unset, None, GetVersionIdRecordLinksState] = GetVersionIdRecordLinksState.M,
) -> Optional[Union[Any, List["RecordLink"]]]:
    """Retrieve record links from entity

     This endpoint allows you to retrieve all the known record links between records of an entity. You
    can filter the record links returned by state otherwise only links of match state are returned. The
    possible values are 'M' for match links, 'P' for probable links and 'A' for links of all states. You
    can also page through the links in the repository using the parameters 'firstResult' and
    'maxResults'.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):
        first_result (Union[Unset, None, int]):
        key_val (Union[Unset, None, str]):
        max_results (Union[Unset, None, int]):  Default: 10.
        state (Union[Unset, None, GetVersionIdRecordLinksState]):  Default:
            GetVersionIdRecordLinksState.M.

    Returns:
        Response[Union[Any, List['RecordLink']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            entity_id=entity_id,
            first_result=first_result,
            key_val=key_val,
            max_results=max_results,
            state=state,
        )
    ).parsed
