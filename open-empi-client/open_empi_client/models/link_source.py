from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="LinkSource")


@attr.s(auto_attribs=True)
class LinkSource:
    """
    Attributes:
        link_source_id (Union[Unset, int]):
        source_description (Union[Unset, str]):
        source_name (Union[Unset, str]):
    """

    link_source_id: Union[Unset, int] = UNSET
    source_description: Union[Unset, str] = UNSET
    source_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        link_source_id = self.link_source_id
        source_description = self.source_description
        source_name = self.source_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if link_source_id is not UNSET:
            field_dict["linkSourceId"] = link_source_id
        if source_description is not UNSET:
            field_dict["sourceDescription"] = source_description
        if source_name is not UNSET:
            field_dict["sourceName"] = source_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        link_source_id = d.pop("linkSourceId", UNSET)

        source_description = d.pop("sourceDescription", UNSET)

        source_name = d.pop("sourceName", UNSET)

        link_source = cls(
            link_source_id=link_source_id,
            source_description=source_description,
            source_name=source_name,
        )

        link_source.additional_properties = d
        return link_source

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
