from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SynonymEntry")


@attr.s(auto_attribs=True)
class SynonymEntry:
    """
    Attributes:
        field_name (Union[Unset, str]):
        synonym_id (Union[Unset, str]):
        synonyms (Union[Unset, List[str]]):
    """

    field_name: Union[Unset, str] = UNSET
    synonym_id: Union[Unset, str] = UNSET
    synonyms: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_name = self.field_name
        synonym_id = self.synonym_id
        synonyms: Union[Unset, List[str]] = UNSET
        if not isinstance(self.synonyms, Unset):
            synonyms = self.synonyms

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if synonym_id is not UNSET:
            field_dict["synonymId"] = synonym_id
        if synonyms is not UNSET:
            field_dict["synonyms"] = synonyms

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_name = d.pop("fieldName", UNSET)

        synonym_id = d.pop("synonymId", UNSET)

        synonyms = cast(List[str], d.pop("synonyms", UNSET))

        synonym_entry = cls(
            field_name=field_name,
            synonym_id=synonym_id,
            synonyms=synonyms,
        )

        synonym_entry.additional_properties = d
        return synonym_entry

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
