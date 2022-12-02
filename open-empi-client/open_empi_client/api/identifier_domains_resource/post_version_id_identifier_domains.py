from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.identifier_domain import IdentifierDomain
from ...types import Response


def _get_kwargs(
    version_id: str = "1.0",
    *,
    client: Client,
    json_body: IdentifierDomain,
) -> Dict[str, Any]:
    url = "{}/{versionId}/identifier-domains".format(client.base_url, versionId=version_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, IdentifierDomain]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = IdentifierDomain.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.CONFLICT:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == HTTPStatus.INTERNAL_SERVER_ERROR:
        response_500 = cast(Any, None)
        return response_500
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, IdentifierDomain]]:
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
    json_body: IdentifierDomain,
) -> Response[Union[Any, IdentifierDomain]]:
    """Define a new identifier domain

     Use this endpoint to define a new identifier domain. An identifier domain is an object that defines
    an organization that assigns identifiers to records. An identifier domain must at least have an
    identifier domain name and either a namespace identifier, the pair universal identifier and
    identifier type code, or both values specified. When creating a new identifier you must not specify
    an identifier domain id as it is assigned by the system.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (IdentifierDomain):

    Returns:
        Response[Union[Any, IdentifierDomain]]
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
    json_body: IdentifierDomain,
) -> Optional[Union[Any, IdentifierDomain]]:
    """Define a new identifier domain

     Use this endpoint to define a new identifier domain. An identifier domain is an object that defines
    an organization that assigns identifiers to records. An identifier domain must at least have an
    identifier domain name and either a namespace identifier, the pair universal identifier and
    identifier type code, or both values specified. When creating a new identifier you must not specify
    an identifier domain id as it is assigned by the system.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (IdentifierDomain):

    Returns:
        Response[Union[Any, IdentifierDomain]]
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
    json_body: IdentifierDomain,
) -> Response[Union[Any, IdentifierDomain]]:
    """Define a new identifier domain

     Use this endpoint to define a new identifier domain. An identifier domain is an object that defines
    an organization that assigns identifiers to records. An identifier domain must at least have an
    identifier domain name and either a namespace identifier, the pair universal identifier and
    identifier type code, or both values specified. When creating a new identifier you must not specify
    an identifier domain id as it is assigned by the system.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (IdentifierDomain):

    Returns:
        Response[Union[Any, IdentifierDomain]]
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
    json_body: IdentifierDomain,
) -> Optional[Union[Any, IdentifierDomain]]:
    """Define a new identifier domain

     Use this endpoint to define a new identifier domain. An identifier domain is an object that defines
    an organization that assigns identifiers to records. An identifier domain must at least have an
    identifier domain name and either a namespace identifier, the pair universal identifier and
    identifier type code, or both values specified. When creating a new identifier you must not specify
    an identifier domain id as it is assigned by the system.

    Args:
        version_id (str):  Default: '1.0'.
        json_body (IdentifierDomain):

    Returns:
        Response[Union[Any, IdentifierDomain]]
    """

    return (
        await asyncio_detailed(
            version_id=version_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
