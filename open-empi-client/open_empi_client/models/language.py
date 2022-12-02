from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Language")


@attr.s(auto_attribs=True)
class Language:
    """
    Attributes:
        language_cd (Union[Unset, int]):
        language_code (Union[Unset, str]):
        language_description (Union[Unset, str]):
        language_name (Union[Unset, str]):
    """

    language_cd: Union[Unset, int] = UNSET
    language_code: Union[Unset, str] = UNSET
    language_description: Union[Unset, str] = UNSET
    language_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        language_cd = self.language_cd
        language_code = self.language_code
        language_description = self.language_description
        language_name = self.language_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if language_cd is not UNSET:
            field_dict["languageCd"] = language_cd
        if language_code is not UNSET:
            field_dict["languageCode"] = language_code
        if language_description is not UNSET:
            field_dict["languageDescription"] = language_description
        if language_name is not UNSET:
            field_dict["languageName"] = language_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        language_cd = d.pop("languageCd", UNSET)

        language_code = d.pop("languageCode", UNSET)

        language_description = d.pop("languageDescription", UNSET)

        language_name = d.pop("languageName", UNSET)

        language = cls(
            language_cd=language_cd,
            language_code=language_code,
            language_description=language_description,
            language_name=language_name,
        )

        language.additional_properties = d
        return language

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
