from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_domain import IdentifierDomain


T = TypeVar("T", bound="IdentifierUpdateEntry")


@attr.s(auto_attribs=True)
class IdentifierUpdateEntry:
    """
    Attributes:
        identifier (Union[Unset, str]):
        identifier_domain (Union[Unset, IdentifierDomain]):
    """

    identifier: Union[Unset, str] = UNSET
    identifier_domain: Union[Unset, "IdentifierDomain"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier = self.identifier
        identifier_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier_domain, Unset):
            identifier_domain = self.identifier_domain.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_domain is not UNSET:
            field_dict["identifierDomain"] = identifier_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_domain import IdentifierDomain

        d = src_dict.copy()
        identifier = d.pop("identifier", UNSET)

        _identifier_domain = d.pop("identifierDomain", UNSET)
        identifier_domain: Union[Unset, IdentifierDomain]
        if isinstance(_identifier_domain, Unset):
            identifier_domain = UNSET
        else:
            identifier_domain = IdentifierDomain.from_dict(_identifier_domain)

        identifier_update_entry = cls(
            identifier=identifier,
            identifier_domain=identifier_domain,
        )

        identifier_update_entry.additional_properties = d
        return identifier_update_entry

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
