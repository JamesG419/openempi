from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address import Address
    from ..models.identifier_domain import IdentifierDomain
    from ..models.permission import Permission
    from ..models.role import Role


T = TypeVar("T", bound="User")


@attr.s(auto_attribs=True)
class User:
    """
    Attributes:
        account_expired (Union[Unset, bool]):
        account_locked (Union[Unset, bool]):
        address (Union[Unset, Address]):
        credentials_expired (Union[Unset, bool]):
        email (Union[Unset, str]):
        enabled (Union[Unset, bool]):
        first_name (Union[Unset, str]):
        id (Union[Unset, int]):
        identifier_domain (Union[Unset, IdentifierDomain]):
        last_name (Union[Unset, str]):
        password (Union[Unset, str]):
        password_hint (Union[Unset, str]):
        permissions (Union[Unset, List['Permission']]):
        phone_number (Union[Unset, str]):
        roles (Union[Unset, List['Role']]):
        username (Union[Unset, str]):
        website (Union[Unset, str]):
    """

    account_expired: Union[Unset, bool] = UNSET
    account_locked: Union[Unset, bool] = UNSET
    address: Union[Unset, "Address"] = UNSET
    credentials_expired: Union[Unset, bool] = UNSET
    email: Union[Unset, str] = UNSET
    enabled: Union[Unset, bool] = UNSET
    first_name: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    identifier_domain: Union[Unset, "IdentifierDomain"] = UNSET
    last_name: Union[Unset, str] = UNSET
    password: Union[Unset, str] = UNSET
    password_hint: Union[Unset, str] = UNSET
    permissions: Union[Unset, List["Permission"]] = UNSET
    phone_number: Union[Unset, str] = UNSET
    roles: Union[Unset, List["Role"]] = UNSET
    username: Union[Unset, str] = UNSET
    website: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account_expired = self.account_expired
        account_locked = self.account_locked
        address: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address, Unset):
            address = self.address.to_dict()

        credentials_expired = self.credentials_expired
        email = self.email
        enabled = self.enabled
        first_name = self.first_name
        id = self.id
        identifier_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier_domain, Unset):
            identifier_domain = self.identifier_domain.to_dict()

        last_name = self.last_name
        password = self.password
        password_hint = self.password_hint
        permissions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = []
            for permissions_item_data in self.permissions:
                permissions_item = permissions_item_data.to_dict()

                permissions.append(permissions_item)

        phone_number = self.phone_number
        roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.roles, Unset):
            roles = []
            for roles_item_data in self.roles:
                roles_item = roles_item_data.to_dict()

                roles.append(roles_item)

        username = self.username
        website = self.website

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_expired is not UNSET:
            field_dict["accountExpired"] = account_expired
        if account_locked is not UNSET:
            field_dict["accountLocked"] = account_locked
        if address is not UNSET:
            field_dict["address"] = address
        if credentials_expired is not UNSET:
            field_dict["credentialsExpired"] = credentials_expired
        if email is not UNSET:
            field_dict["email"] = email
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if id is not UNSET:
            field_dict["id"] = id
        if identifier_domain is not UNSET:
            field_dict["identifierDomain"] = identifier_domain
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if password is not UNSET:
            field_dict["password"] = password
        if password_hint is not UNSET:
            field_dict["passwordHint"] = password_hint
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if roles is not UNSET:
            field_dict["roles"] = roles
        if username is not UNSET:
            field_dict["username"] = username
        if website is not UNSET:
            field_dict["website"] = website

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address import Address
        from ..models.identifier_domain import IdentifierDomain
        from ..models.permission import Permission
        from ..models.role import Role

        d = src_dict.copy()
        account_expired = d.pop("accountExpired", UNSET)

        account_locked = d.pop("accountLocked", UNSET)

        _address = d.pop("address", UNSET)
        address: Union[Unset, Address]
        if isinstance(_address, Unset):
            address = UNSET
        else:
            address = Address.from_dict(_address)

        credentials_expired = d.pop("credentialsExpired", UNSET)

        email = d.pop("email", UNSET)

        enabled = d.pop("enabled", UNSET)

        first_name = d.pop("firstName", UNSET)

        id = d.pop("id", UNSET)

        _identifier_domain = d.pop("identifierDomain", UNSET)
        identifier_domain: Union[Unset, IdentifierDomain]
        if isinstance(_identifier_domain, Unset):
            identifier_domain = UNSET
        else:
            identifier_domain = IdentifierDomain.from_dict(_identifier_domain)

        last_name = d.pop("lastName", UNSET)

        password = d.pop("password", UNSET)

        password_hint = d.pop("passwordHint", UNSET)

        permissions = []
        _permissions = d.pop("permissions", UNSET)
        for permissions_item_data in _permissions or []:
            permissions_item = Permission.from_dict(permissions_item_data)

            permissions.append(permissions_item)

        phone_number = d.pop("phoneNumber", UNSET)

        roles = []
        _roles = d.pop("roles", UNSET)
        for roles_item_data in _roles or []:
            roles_item = Role.from_dict(roles_item_data)

            roles.append(roles_item)

        username = d.pop("username", UNSET)

        website = d.pop("website", UNSET)

        user = cls(
            account_expired=account_expired,
            account_locked=account_locked,
            address=address,
            credentials_expired=credentials_expired,
            email=email,
            enabled=enabled,
            first_name=first_name,
            id=id,
            identifier_domain=identifier_domain,
            last_name=last_name,
            password=password,
            password_hint=password_hint,
            permissions=permissions,
            phone_number=phone_number,
            roles=roles,
            username=username,
            website=website,
        )

        user.additional_properties = d
        return user

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
