from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_domain import IdentifierDomain


T = TypeVar("T", bound="IdentifierDomainAttributeRequest")


@attr.s(auto_attribs=True)
class IdentifierDomainAttributeRequest:
    """
    Attributes:
        attribute_name (Union[Unset, str]):
        attribute_value (Union[Unset, str]):
        identifier_domain (Union[Unset, IdentifierDomain]):
    """

    attribute_name: Union[Unset, str] = UNSET
    attribute_value: Union[Unset, str] = UNSET
    identifier_domain: Union[Unset, "IdentifierDomain"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name
        attribute_value = self.attribute_value
        identifier_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier_domain, Unset):
            identifier_domain = self.identifier_domain.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if attribute_value is not UNSET:
            field_dict["attributeValue"] = attribute_value
        if identifier_domain is not UNSET:
            field_dict["identifierDomain"] = identifier_domain

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_domain import IdentifierDomain

        d = src_dict.copy()
        attribute_name = d.pop("attributeName", UNSET)

        attribute_value = d.pop("attributeValue", UNSET)

        _identifier_domain = d.pop("identifierDomain", UNSET)
        identifier_domain: Union[Unset, IdentifierDomain]
        if isinstance(_identifier_domain, Unset):
            identifier_domain = UNSET
        else:
            identifier_domain = IdentifierDomain.from_dict(_identifier_domain)

        identifier_domain_attribute_request = cls(
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            identifier_domain=identifier_domain,
        )

        identifier_domain_attribute_request.additional_properties = d
        return identifier_domain_attribute_request

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
