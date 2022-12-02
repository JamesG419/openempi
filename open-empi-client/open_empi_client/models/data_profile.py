from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataProfile")


@attr.s(auto_attribs=True)
class DataProfile:
    """
    Attributes:
        data_profile_id (Union[Unset, int]):
        data_source_id (Union[Unset, int]):
        date_completed_str (Union[Unset, str]):
        date_initiated_str (Union[Unset, str]):
        entity_id (Union[Unset, int]):
    """

    data_profile_id: Union[Unset, int] = UNSET
    data_source_id: Union[Unset, int] = UNSET
    date_completed_str: Union[Unset, str] = UNSET
    date_initiated_str: Union[Unset, str] = UNSET
    entity_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        data_profile_id = self.data_profile_id
        data_source_id = self.data_source_id
        date_completed_str = self.date_completed_str
        date_initiated_str = self.date_initiated_str
        entity_id = self.entity_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data_profile_id is not UNSET:
            field_dict["dataProfileId"] = data_profile_id
        if data_source_id is not UNSET:
            field_dict["dataSourceId"] = data_source_id
        if date_completed_str is not UNSET:
            field_dict["dateCompletedStr"] = date_completed_str
        if date_initiated_str is not UNSET:
            field_dict["dateInitiatedStr"] = date_initiated_str
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        data_profile_id = d.pop("dataProfileId", UNSET)

        data_source_id = d.pop("dataSourceId", UNSET)

        date_completed_str = d.pop("dateCompletedStr", UNSET)

        date_initiated_str = d.pop("dateInitiatedStr", UNSET)

        entity_id = d.pop("entityId", UNSET)

        data_profile = cls(
            data_profile_id=data_profile_id,
            data_source_id=data_source_id,
            date_completed_str=date_completed_str,
            date_initiated_str=date_initiated_str,
            entity_id=entity_id,
        )

        data_profile.additional_properties = d
        return data_profile

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
