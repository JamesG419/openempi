from http import HTTPStatus
from typing import Any, Dict

import httpx

from ...client import Client
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Dict[str, Any]:
    url = "{}/{versionId}/custom-fields/records".format(client.base_url, versionId=version_id)

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


def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Response[Any]:
    """Generate custom fields for all records

     This endpoint allows you to regenerate the values for all custom fields currently defined against
    all the records in the repository. The response from the request is a job entry that refers to the
    job that was created to handle the regeneration of the custom fields for all records in an
    asynchronous manner.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    version_id: str = "1.0",
    *,
    client: Client,
    entity_id: int,
) -> Response[Any]:
    """Generate custom fields for all records

     This endpoint allows you to regenerate the values for all custom fields currently defined against
    all the records in the repository. The response from the request is a job entry that refers to the
    job that was created to handle the regeneration of the custom fields for all records in an
    asynchronous manner.

    Args:
        version_id (str):  Default: '1.0'.
        entity_id (int):

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        version_id=version_id,
        client=client,
        entity_id=entity_id,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)
