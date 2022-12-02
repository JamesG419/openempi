from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Nationality")


@attr.s(auto_attribs=True)
class Nationality:
    """
    Attributes:
        nationality_cd (Union[Unset, int]):
        nationality_code (Union[Unset, str]):
        nationality_description (Union[Unset, str]):
        nationality_name (Union[Unset, str]):
    """

    nationality_cd: Union[Unset, int] = UNSET
    nationality_code: Union[Unset, str] = UNSET
    nationality_description: Union[Unset, str] = UNSET
    nationality_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        nationality_cd = self.nationality_cd
        nationality_code = self.nationality_code
        nationality_description = self.nationality_description
        nationality_name = self.nationality_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if nationality_cd is not UNSET:
            field_dict["nationalityCd"] = nationality_cd
        if nationality_code is not UNSET:
            field_dict["nationalityCode"] = nationality_code
        if nationality_description is not UNSET:
            field_dict["nationalityDescription"] = nationality_description
        if nationality_name is not UNSET:
            field_dict["nationalityName"] = nationality_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        nationality_cd = d.pop("nationalityCd", UNSET)

        nationality_code = d.pop("nationalityCode", UNSET)

        nationality_description = d.pop("nationalityDescription", UNSET)

        nationality_name = d.pop("nationalityName", UNSET)

        nationality = cls(
            nationality_cd=nationality_cd,
            nationality_code=nationality_code,
            nationality_description=nationality_description,
            nationality_name=nationality_name,
        )

        nationality.additional_properties = d
        return nationality

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
