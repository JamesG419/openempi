import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="LoggedLink")


@attr.s(auto_attribs=True)
class LoggedLink:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]):
        is_null_scored (Union[Unset, bool]):
        label (Union[Unset, str]):
        left_in_record_id (Union[Unset, str]):
        left_record_id (Union[Unset, int]):
        link_id (Union[Unset, str]):
        right_in_record_id (Union[Unset, str]):
        right_record_id (Union[Unset, int]):
        vector_value (Union[Unset, int]):
        weight (Union[Unset, float]):
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    is_null_scored: Union[Unset, bool] = UNSET
    label: Union[Unset, str] = UNSET
    left_in_record_id: Union[Unset, str] = UNSET
    left_record_id: Union[Unset, int] = UNSET
    link_id: Union[Unset, str] = UNSET
    right_in_record_id: Union[Unset, str] = UNSET
    right_record_id: Union[Unset, int] = UNSET
    vector_value: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        is_null_scored = self.is_null_scored
        label = self.label
        left_in_record_id = self.left_in_record_id
        left_record_id = self.left_record_id
        link_id = self.link_id
        right_in_record_id = self.right_in_record_id
        right_record_id = self.right_record_id
        vector_value = self.vector_value
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if is_null_scored is not UNSET:
            field_dict["isNullScored"] = is_null_scored
        if label is not UNSET:
            field_dict["label"] = label
        if left_in_record_id is not UNSET:
            field_dict["leftInRecordId"] = left_in_record_id
        if left_record_id is not UNSET:
            field_dict["leftRecordId"] = left_record_id
        if link_id is not UNSET:
            field_dict["linkId"] = link_id
        if right_in_record_id is not UNSET:
            field_dict["rightInRecordId"] = right_in_record_id
        if right_record_id is not UNSET:
            field_dict["rightRecordId"] = right_record_id
        if vector_value is not UNSET:
            field_dict["vectorValue"] = vector_value
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        is_null_scored = d.pop("isNullScored", UNSET)

        label = d.pop("label", UNSET)

        left_in_record_id = d.pop("leftInRecordId", UNSET)

        left_record_id = d.pop("leftRecordId", UNSET)

        link_id = d.pop("linkId", UNSET)

        right_in_record_id = d.pop("rightInRecordId", UNSET)

        right_record_id = d.pop("rightRecordId", UNSET)

        vector_value = d.pop("vectorValue", UNSET)

        weight = d.pop("weight", UNSET)

        logged_link = cls(
            date_created=date_created,
            is_null_scored=is_null_scored,
            label=label,
            left_in_record_id=left_in_record_id,
            left_record_id=left_record_id,
            link_id=link_id,
            right_in_record_id=right_in_record_id,
            right_record_id=right_record_id,
            vector_value=vector_value,
            weight=weight,
        )

        logged_link.additional_properties = d
        return logged_link

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
