from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Gender")


@attr.s(auto_attribs=True)
class Gender:
    """
    Attributes:
        gender_cd (Union[Unset, int]):
        gender_code (Union[Unset, str]):
        gender_description (Union[Unset, str]):
        gender_name (Union[Unset, str]):
    """

    gender_cd: Union[Unset, int] = UNSET
    gender_code: Union[Unset, str] = UNSET
    gender_description: Union[Unset, str] = UNSET
    gender_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        gender_cd = self.gender_cd
        gender_code = self.gender_code
        gender_description = self.gender_description
        gender_name = self.gender_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if gender_cd is not UNSET:
            field_dict["genderCd"] = gender_cd
        if gender_code is not UNSET:
            field_dict["genderCode"] = gender_code
        if gender_description is not UNSET:
            field_dict["genderDescription"] = gender_description
        if gender_name is not UNSET:
            field_dict["genderName"] = gender_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        gender_cd = d.pop("genderCd", UNSET)

        gender_code = d.pop("genderCode", UNSET)

        gender_description = d.pop("genderDescription", UNSET)

        gender_name = d.pop("genderName", UNSET)

        gender = cls(
            gender_cd=gender_cd,
            gender_code=gender_code,
            gender_description=gender_description,
            gender_name=gender_name,
        )

        gender.additional_properties = d
        return gender

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
