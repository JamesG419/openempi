from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="IdentifierDomain")


@attr.s(auto_attribs=True)
class IdentifierDomain:
    """
    Attributes:
        date_created_str (Union[Unset, str]):
        identifier_domain_description (Union[Unset, str]):
        identifier_domain_id (Union[Unset, int]):
        identifier_domain_name (Union[Unset, str]):
        namespace_identifier (Union[Unset, str]):
        universal_identifier (Union[Unset, str]):
        universal_identifier_type_code (Union[Unset, str]):
    """

    date_created_str: Union[Unset, str] = UNSET
    identifier_domain_description: Union[Unset, str] = UNSET
    identifier_domain_id: Union[Unset, int] = UNSET
    identifier_domain_name: Union[Unset, str] = UNSET
    namespace_identifier: Union[Unset, str] = UNSET
    universal_identifier: Union[Unset, str] = UNSET
    universal_identifier_type_code: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created_str = self.date_created_str
        identifier_domain_description = self.identifier_domain_description
        identifier_domain_id = self.identifier_domain_id
        identifier_domain_name = self.identifier_domain_name
        namespace_identifier = self.namespace_identifier
        universal_identifier = self.universal_identifier
        universal_identifier_type_code = self.universal_identifier_type_code

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created_str is not UNSET:
            field_dict["dateCreatedStr"] = date_created_str
        if identifier_domain_description is not UNSET:
            field_dict["identifierDomainDescription"] = identifier_domain_description
        if identifier_domain_id is not UNSET:
            field_dict["identifierDomainId"] = identifier_domain_id
        if identifier_domain_name is not UNSET:
            field_dict["identifierDomainName"] = identifier_domain_name
        if namespace_identifier is not UNSET:
            field_dict["namespaceIdentifier"] = namespace_identifier
        if universal_identifier is not UNSET:
            field_dict["universalIdentifier"] = universal_identifier
        if universal_identifier_type_code is not UNSET:
            field_dict["universalIdentifierTypeCode"] = universal_identifier_type_code

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_created_str = d.pop("dateCreatedStr", UNSET)

        identifier_domain_description = d.pop("identifierDomainDescription", UNSET)

        identifier_domain_id = d.pop("identifierDomainId", UNSET)

        identifier_domain_name = d.pop("identifierDomainName", UNSET)

        namespace_identifier = d.pop("namespaceIdentifier", UNSET)

        universal_identifier = d.pop("universalIdentifier", UNSET)

        universal_identifier_type_code = d.pop("universalIdentifierTypeCode", UNSET)

        identifier_domain = cls(
            date_created_str=date_created_str,
            identifier_domain_description=identifier_domain_description,
            identifier_domain_id=identifier_domain_id,
            identifier_domain_name=identifier_domain_name,
            namespace_identifier=namespace_identifier,
            universal_identifier=universal_identifier,
            universal_identifier_type_code=universal_identifier_type_code,
        )

        identifier_domain.additional_properties = d
        return identifier_domain

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
