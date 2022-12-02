from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...models.put_version_id_pixpdq_service_state_updown_updown import PutVersionIdPixpdqServiceStateUpdownUpdown
from ...types import UNSET, Response


def _get_kwargs(
    version_id: str = '1.0',
    updown: PutVersionIdPixpdqServiceStateUpdownUpdown,
    *,
    client: Client,

) -> Dict[str, Any]:
    url = "{}/{versionId}/pixpdq-service/state/{updown}".format(
        client.base_url,versionId=version_id,updown=updown)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    

    

    

    

    

    return {
	    "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }




def _build_response(*, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=None,
    )


def sync_detailed(
    version_id: str = '1.0',
    updown: PutVersionIdPixpdqServiceStateUpdownUpdown,
    *,
    client: Client,

) -> Response[Any]:
    """Change the state of the PIX/PDQ server

     Use this endpoint to change the running state of the HL7v2 PIX/PDQ server. You can use this
    endpoint to start or stop the server.

    Args:
        version_id (str):  Default: '1.0'.
        updown (PutVersionIdPixpdqServiceStateUpdownUpdown):

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
updown=updown,
client=client,

    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


async def asyncio_detailed(
    version_id: str = '1.0',
    updown: PutVersionIdPixpdqServiceStateUpdownUpdown,
    *,
    client: Client,

) -> Response[Any]:
    """Change the state of the PIX/PDQ server

     Use this endpoint to change the running state of the HL7v2 PIX/PDQ server. You can use this
    endpoint to start or stop the server.

    Args:
        version_id (str):  Default: '1.0'.
        updown (PutVersionIdPixpdqServiceStateUpdownUpdown):

    Returns:
        Response[Any]
    """


    kwargs = _get_kwargs(
        version_id=version_id,
updown=updown,
client=client,

    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(
            **kwargs
        )

    return _build_response(response=response)


