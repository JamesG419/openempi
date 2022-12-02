from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.probabilistic_matching_configuration import ProbabilisticMatchingConfiguration
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    json_body: ProbabilisticMatchingConfiguration,
) -> Dict[str, Any]:
    url = "{}/{versionId}/probabilistic-matching/configuration".format(client.base_url, versionId=version_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List["ProbabilisticMatchingConfiguration"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ProbabilisticMatchingConfiguration.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List["ProbabilisticMatchingConfiguration"]]]:
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
    json_body: ProbabilisticMatchingConfiguration,
) -> Response[Union[Any, List["ProbabilisticMatchingConfiguration"]]]:
    """Update the probabilistic matching configuration

     This endpoint allows you to update the current configuration of the probabilistic matching service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (ProbabilisticMatchingConfiguration):

    Returns:
        Response[Union[Any, List['ProbabilisticMatchingConfiguration']]]
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
    json_body: ProbabilisticMatchingConfiguration,
) -> Optional[Union[Any, List["ProbabilisticMatchingConfiguration"]]]:
    """Update the probabilistic matching configuration

     This endpoint allows you to update the current configuration of the probabilistic matching service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (ProbabilisticMatchingConfiguration):

    Returns:
        Response[Union[Any, List['ProbabilisticMatchingConfiguration']]]
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
    json_body: ProbabilisticMatchingConfiguration,
) -> Response[Union[Any, List["ProbabilisticMatchingConfiguration"]]]:
    """Update the probabilistic matching configuration

     This endpoint allows you to update the current configuration of the probabilistic matching service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (ProbabilisticMatchingConfiguration):

    Returns:
        Response[Union[Any, List['ProbabilisticMatchingConfiguration']]]
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
    json_body: ProbabilisticMatchingConfiguration,
) -> Optional[Union[Any, List["ProbabilisticMatchingConfiguration"]]]:
    """Update the probabilistic matching configuration

     This endpoint allows you to update the current configuration of the probabilistic matching service.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (ProbabilisticMatchingConfiguration):

    Returns:
        Response[Union[Any, List['ProbabilisticMatchingConfiguration']]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
