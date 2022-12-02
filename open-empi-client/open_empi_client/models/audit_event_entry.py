from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.record import Record


T = TypeVar("T", bound="AuditEventEntry")


@attr.s(auto_attribs=True)
class AuditEventEntry:
    """
    Attributes:
        alt_ref_record (Union[Unset, Record]):
        alt_ref_record_id (Union[Unset, int]):
        audit_event_description (Union[Unset, str]):
        audit_event_type_id (Union[Unset, int]):
        audit_event_id (Union[Unset, int]):
        date_created_str (Union[Unset, str]):
        entity_name (Union[Unset, str]):
        ref_record (Union[Unset, Record]):
        ref_record_id (Union[Unset, int]):
        user_created_by_id (Union[Unset, int]):
    """

    alt_ref_record: Union[Unset, "Record"] = UNSET
    alt_ref_record_id: Union[Unset, int] = UNSET
    audit_event_description: Union[Unset, str] = UNSET
    audit_event_type_id: Union[Unset, int] = UNSET
    audit_event_id: Union[Unset, int] = UNSET
    date_created_str: Union[Unset, str] = UNSET
    entity_name: Union[Unset, str] = UNSET
    ref_record: Union[Unset, "Record"] = UNSET
    ref_record_id: Union[Unset, int] = UNSET
    user_created_by_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        alt_ref_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.alt_ref_record, Unset):
            alt_ref_record = self.alt_ref_record.to_dict()

        alt_ref_record_id = self.alt_ref_record_id
        audit_event_description = self.audit_event_description
        audit_event_type_id = self.audit_event_type_id
        audit_event_id = self.audit_event_id
        date_created_str = self.date_created_str
        entity_name = self.entity_name
        ref_record: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ref_record, Unset):
            ref_record = self.ref_record.to_dict()

        ref_record_id = self.ref_record_id
        user_created_by_id = self.user_created_by_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if alt_ref_record is not UNSET:
            field_dict["altRefRecord"] = alt_ref_record
        if alt_ref_record_id is not UNSET:
            field_dict["altRefRecordId"] = alt_ref_record_id
        if audit_event_description is not UNSET:
            field_dict["auditEventDescription"] = audit_event_description
        if audit_event_type_id is not UNSET:
            field_dict["auditEventTypeId"] = audit_event_type_id
        if audit_event_id is not UNSET:
            field_dict["auditEventId"] = audit_event_id
        if date_created_str is not UNSET:
            field_dict["dateCreatedStr"] = date_created_str
        if entity_name is not UNSET:
            field_dict["entityName"] = entity_name
        if ref_record is not UNSET:
            field_dict["refRecord"] = ref_record
        if ref_record_id is not UNSET:
            field_dict["refRecordId"] = ref_record_id
        if user_created_by_id is not UNSET:
            field_dict["userCreatedById"] = user_created_by_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.record import Record

        d = src_dict.copy()
        _alt_ref_record = d.pop("altRefRecord", UNSET)
        alt_ref_record: Union[Unset, Record]
        if isinstance(_alt_ref_record, Unset):
            alt_ref_record = UNSET
        else:
            alt_ref_record = Record.from_dict(_alt_ref_record)

        alt_ref_record_id = d.pop("altRefRecordId", UNSET)

        audit_event_description = d.pop("auditEventDescription", UNSET)

        audit_event_type_id = d.pop("auditEventTypeId", UNSET)

        audit_event_id = d.pop("auditEventId", UNSET)

        date_created_str = d.pop("dateCreatedStr", UNSET)

        entity_name = d.pop("entityName", UNSET)

        _ref_record = d.pop("refRecord", UNSET)
        ref_record: Union[Unset, Record]
        if isinstance(_ref_record, Unset):
            ref_record = UNSET
        else:
            ref_record = Record.from_dict(_ref_record)

        ref_record_id = d.pop("refRecordId", UNSET)

        user_created_by_id = d.pop("userCreatedById", UNSET)

        audit_event_entry = cls(
            alt_ref_record=alt_ref_record,
            alt_ref_record_id=alt_ref_record_id,
            audit_event_description=audit_event_description,
            audit_event_type_id=audit_event_type_id,
            audit_event_id=audit_event_id,
            date_created_str=date_created_str,
            entity_name=entity_name,
            ref_record=ref_record,
            ref_record_id=ref_record_id,
            user_created_by_id=user_created_by_id,
        )

        audit_event_entry.additional_properties = d
        return audit_event_entry

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
