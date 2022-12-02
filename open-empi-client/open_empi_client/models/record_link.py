from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="RecordLink")


@attr.s(auto_attribs=True)
class RecordLink:
    """
    Attributes:
        date_created (Union[Unset, str]):
        date_reviewed (Union[Unset, str]):
        entity_id (Union[Unset, int]):
        left_record (Union[Unset, Record]):
        record_link_id (Union[Unset, str]):
        right_record (Union[Unset, Record]):
        source (Union[Unset, str]):
        state (Union[Unset, str]):
        user_created_by (Union[Unset, int]):
        user_reviewed_by (Union[Unset, int]):
        vector (Union[Unset, int]):
        weight (Union[Unset, float]):
    """

    date_created: Union[Unset, str] = UNSET
    date_reviewed: Union[Unset, str] = UNSET
    entity_id: Union[Unset, int] = UNSET
    left_record: Union[Unset, "Record"] = UNSET
    record_link_id: Union[Unset, str] = UNSET
    right_record: Union[Unset, "Record"] = UNSET
    source: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    user_created_by: Union[Unset, int] = UNSET
    user_reviewed_by: Union[Unset, int] = UNSET
    vector: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created = self.date_created
        date_reviewed = self.date_reviewed
        entity_id = self.entity_id
        left_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.left_record, Unset):
            left_record = self.left_record.to_dict()

        record_link_id = self.record_link_id
        right_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.right_record, Unset):
            right_record = self.right_record.to_dict()

        source = self.source
        state = self.state
        user_created_by = self.user_created_by
        user_reviewed_by = self.user_reviewed_by
        vector = self.vector
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_reviewed is not UNSET:
            field_dict["dateReviewed"] = date_reviewed
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if left_record is not UNSET:
            field_dict["leftRecord"] = left_record
        if record_link_id is not UNSET:
            field_dict["recordLinkId"] = record_link_id
        if right_record is not UNSET:
            field_dict["rightRecord"] = right_record
        if source is not UNSET:
            field_dict["source"] = source
        if state is not UNSET:
            field_dict["state"] = state
        if user_created_by is not UNSET:
            field_dict["userCreatedBy"] = user_created_by
        if user_reviewed_by is not UNSET:
            field_dict["userReviewedBy"] = user_reviewed_by
        if vector is not UNSET:
            field_dict["vector"] = vector
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record import Record

        d = src_dict.copy()
        date_created = d.pop("dateCreated", UNSET)

        date_reviewed = d.pop("dateReviewed", UNSET)

        entity_id = d.pop("entityId", UNSET)

        _left_record = d.pop("leftRecord", UNSET)
        left_record: Union[Unset, Record]
        if isinstance(_left_record, Unset):
            left_record = UNSET
        else:
            left_record = Record.from_dict(_left_record)

        record_link_id = d.pop("recordLinkId", UNSET)

        _right_record = d.pop("rightRecord", UNSET)
        right_record: Union[Unset, Record]
        if isinstance(_right_record, Unset):
            right_record = UNSET
        else:
            right_record = Record.from_dict(_right_record)

        source = d.pop("source", UNSET)

        state = d.pop("state", UNSET)

        user_created_by = d.pop("userCreatedBy", UNSET)

        user_reviewed_by = d.pop("userReviewedBy", UNSET)

        vector = d.pop("vector", UNSET)

        weight = d.pop("weight", UNSET)

        record_link = cls(
            date_created=date_created,
            date_reviewed=date_reviewed,
            entity_id=entity_id,
            left_record=left_record,
            record_link_id=record_link_id,
            right_record=right_record,
            source=source,
            state=state,
            user_created_by=user_created_by,
            user_reviewed_by=user_reviewed_by,
            vector=vector,
            weight=weight,
        )

        record_link.additional_properties = d
        return record_link

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
