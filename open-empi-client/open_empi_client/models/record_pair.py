from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="RecordPair")


@attr.s(auto_attribs=True)
class RecordPair:
    """
    Attributes:
        left_record (Union[Unset, Record]):
        match_outcome (Union[Unset, int]):
        right_record (Union[Unset, Record]):
        weight (Union[Unset, float]):
    """

    left_record: Union[Unset, "Record"] = UNSET
    match_outcome: Union[Unset, int] = UNSET
    right_record: Union[Unset, "Record"] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        left_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.left_record, Unset):
            left_record = self.left_record.to_dict()

        match_outcome = self.match_outcome
        right_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.right_record, Unset):
            right_record = self.right_record.to_dict()

        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if left_record is not UNSET:
            field_dict["leftRecord"] = left_record
        if match_outcome is not UNSET:
            field_dict["matchOutcome"] = match_outcome
        if right_record is not UNSET:
            field_dict["rightRecord"] = right_record
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record import Record

        d = src_dict.copy()
        _left_record = d.pop("leftRecord", UNSET)
        left_record: Union[Unset, Record]
        if isinstance(_left_record, Unset):
            left_record = UNSET
        else:
            left_record = Record.from_dict(_left_record)

        match_outcome = d.pop("matchOutcome", UNSET)

        _right_record = d.pop("rightRecord", UNSET)
        right_record: Union[Unset, Record]
        if isinstance(_right_record, Unset):
            right_record = UNSET
        else:
            right_record = Record.from_dict(_right_record)

        weight = d.pop("weight", UNSET)

        record_pair = cls(
            left_record=left_record,
            match_outcome=match_outcome,
            right_record=right_record,
            weight=weight,
        )

        record_pair.additional_properties = d
        return record_pair

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
