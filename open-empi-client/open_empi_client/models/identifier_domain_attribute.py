from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentifierDomainAttribute")


@attr.s(auto_attribs=True)
class IdentifierDomainAttribute:
    """
    Attributes:
        attribute_name (Union[Unset, str]):
        attribute_value (Union[Unset, str]):
        identifier_domain_attrubute_id (Union[Unset, int]):
        identifier_domain_id (Union[Unset, int]):
    """

    attribute_name: Union[Unset, str] = UNSET
    attribute_value: Union[Unset, str] = UNSET
    identifier_domain_attrubute_id: Union[Unset, int] = UNSET
    identifier_domain_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_name = self.attribute_name
        attribute_value = self.attribute_value
        identifier_domain_attrubute_id = self.identifier_domain_attrubute_id
        identifier_domain_id = self.identifier_domain_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if attribute_value is not UNSET:
            field_dict["attributeValue"] = attribute_value
        if identifier_domain_attrubute_id is not UNSET:
            field_dict["identifierDomainAttrubuteId"] = identifier_domain_attrubute_id
        if identifier_domain_id is not UNSET:
            field_dict["identifierDomainId"] = identifier_domain_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_name = d.pop("attributeName", UNSET)

        attribute_value = d.pop("attributeValue", UNSET)

        identifier_domain_attrubute_id = d.pop("identifierDomainAttrubuteId", UNSET)

        identifier_domain_id = d.pop("identifierDomainId", UNSET)

        identifier_domain_attribute = cls(
            attribute_name=attribute_name,
            attribute_value=attribute_value,
            identifier_domain_attrubute_id=identifier_domain_attrubute_id,
            identifier_domain_id=identifier_domain_id,
        )

        identifier_domain_attribute.additional_properties = d
        return identifier_domain_attribute

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
