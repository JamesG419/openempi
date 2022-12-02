from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameType")


@attr.s(auto_attribs=True)
class NameType:
    """
    Attributes:
        name_type_cd (Union[Unset, int]):
        name_type_code (Union[Unset, str]):
        name_type_description (Union[Unset, str]):
        name_type_name (Union[Unset, str]):
    """

    name_type_cd: Union[Unset, int] = UNSET
    name_type_code: Union[Unset, str] = UNSET
    name_type_description: Union[Unset, str] = UNSET
    name_type_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name_type_cd = self.name_type_cd
        name_type_code = self.name_type_code
        name_type_description = self.name_type_description
        name_type_name = self.name_type_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name_type_cd is not UNSET:
            field_dict["nameTypeCd"] = name_type_cd
        if name_type_code is not UNSET:
            field_dict["nameTypeCode"] = name_type_code
        if name_type_description is not UNSET:
            field_dict["nameTypeDescription"] = name_type_description
        if name_type_name is not UNSET:
            field_dict["nameTypeName"] = name_type_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name_type_cd = d.pop("nameTypeCd", UNSET)

        name_type_code = d.pop("nameTypeCode", UNSET)

        name_type_description = d.pop("nameTypeDescription", UNSET)

        name_type_name = d.pop("nameTypeName", UNSET)

        name_type = cls(
            name_type_cd=name_type_cd,
            name_type_code=name_type_code,
            name_type_description=name_type_description,
            name_type_name=name_type_name,
        )

        name_type.additional_properties = d
        return name_type

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
