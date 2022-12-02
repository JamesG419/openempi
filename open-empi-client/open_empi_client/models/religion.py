from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Religion")


@attr.s(auto_attribs=True)
class Religion:
    """
    Attributes:
        religion_cd (Union[Unset, int]):
        religion_code (Union[Unset, str]):
        religion_description (Union[Unset, str]):
        religion_name (Union[Unset, str]):
    """

    religion_cd: Union[Unset, int] = UNSET
    religion_code: Union[Unset, str] = UNSET
    religion_description: Union[Unset, str] = UNSET
    religion_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        religion_cd = self.religion_cd
        religion_code = self.religion_code
        religion_description = self.religion_description
        religion_name = self.religion_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if religion_cd is not UNSET:
            field_dict["religionCd"] = religion_cd
        if religion_code is not UNSET:
            field_dict["religionCode"] = religion_code
        if religion_description is not UNSET:
            field_dict["religionDescription"] = religion_description
        if religion_name is not UNSET:
            field_dict["religionName"] = religion_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        religion_cd = d.pop("religionCd", UNSET)

        religion_code = d.pop("religionCode", UNSET)

        religion_description = d.pop("religionDescription", UNSET)

        religion_name = d.pop("religionName", UNSET)

        religion = cls(
            religion_cd=religion_cd,
            religion_code=religion_code,
            religion_description=religion_description,
            religion_name=religion_name,
        )

        religion.additional_properties = d
        return religion

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
