from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PhoneType")


@attr.s(auto_attribs=True)
class PhoneType:
    """
    Attributes:
        phone_type_cd (Union[Unset, int]):
        phone_type_code (Union[Unset, str]):
        phone_type_description (Union[Unset, str]):
        phone_type_name (Union[Unset, str]):
    """

    phone_type_cd: Union[Unset, int] = UNSET
    phone_type_code: Union[Unset, str] = UNSET
    phone_type_description: Union[Unset, str] = UNSET
    phone_type_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        phone_type_cd = self.phone_type_cd
        phone_type_code = self.phone_type_code
        phone_type_description = self.phone_type_description
        phone_type_name = self.phone_type_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if phone_type_cd is not UNSET:
            field_dict["phoneTypeCd"] = phone_type_cd
        if phone_type_code is not UNSET:
            field_dict["phoneTypeCode"] = phone_type_code
        if phone_type_description is not UNSET:
            field_dict["phoneTypeDescription"] = phone_type_description
        if phone_type_name is not UNSET:
            field_dict["phoneTypeName"] = phone_type_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        phone_type_cd = d.pop("phoneTypeCd", UNSET)

        phone_type_code = d.pop("phoneTypeCode", UNSET)

        phone_type_description = d.pop("phoneTypeDescription", UNSET)

        phone_type_name = d.pop("phoneTypeName", UNSET)

        phone_type = cls(
            phone_type_cd=phone_type_cd,
            phone_type_code=phone_type_code,
            phone_type_description=phone_type_description,
            phone_type_name=phone_type_name,
        )

        phone_type.additional_properties = d
        return phone_type

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
