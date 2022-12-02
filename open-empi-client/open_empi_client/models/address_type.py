from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AddressType")


@attr.s(auto_attribs=True)
class AddressType:
    """
    Attributes:
        address_type_cd (Union[Unset, int]):
        address_type_code (Union[Unset, str]):
        adrdress_type_description (Union[Unset, str]):
        address_type_name (Union[Unset, str]):
    """

    address_type_cd: Union[Unset, int] = UNSET
    address_type_code: Union[Unset, str] = UNSET
    adrdress_type_description: Union[Unset, str] = UNSET
    address_type_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        address_type_cd = self.address_type_cd
        address_type_code = self.address_type_code
        adrdress_type_description = self.adrdress_type_description
        address_type_name = self.address_type_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if address_type_cd is not UNSET:
            field_dict["addressTypeCd"] = address_type_cd
        if address_type_code is not UNSET:
            field_dict["addressTypeCode"] = address_type_code
        if adrdress_type_description is not UNSET:
            field_dict["adrdressTypeDescription"] = adrdress_type_description
        if address_type_name is not UNSET:
            field_dict["addressTypeName"] = address_type_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        address_type_cd = d.pop("addressTypeCd", UNSET)

        address_type_code = d.pop("addressTypeCode", UNSET)

        adrdress_type_description = d.pop("adrdressTypeDescription", UNSET)

        address_type_name = d.pop("addressTypeName", UNSET)

        address_type = cls(
            address_type_cd=address_type_cd,
            address_type_code=address_type_code,
            adrdress_type_description=adrdress_type_description,
            address_type_name=address_type_name,
        )

        address_type.additional_properties = d
        return address_type

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
