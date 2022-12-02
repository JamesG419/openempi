from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AuditEventType")


@attr.s(auto_attribs=True)
class AuditEventType:
    """
    Attributes:
        audit_event_type_cd (Union[Unset, int]):
        audit_event_type_code (Union[Unset, str]):
        audit_event_type_description (Union[Unset, str]):
        audit_event_type_name (Union[Unset, str]):
    """

    audit_event_type_cd: Union[Unset, int] = UNSET
    audit_event_type_code: Union[Unset, str] = UNSET
    audit_event_type_description: Union[Unset, str] = UNSET
    audit_event_type_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        audit_event_type_cd = self.audit_event_type_cd
        audit_event_type_code = self.audit_event_type_code
        audit_event_type_description = self.audit_event_type_description
        audit_event_type_name = self.audit_event_type_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audit_event_type_cd is not UNSET:
            field_dict["auditEventTypeCd"] = audit_event_type_cd
        if audit_event_type_code is not UNSET:
            field_dict["auditEventTypeCode"] = audit_event_type_code
        if audit_event_type_description is not UNSET:
            field_dict["auditEventTypeDescription"] = audit_event_type_description
        if audit_event_type_name is not UNSET:
            field_dict["auditEventTypeName"] = audit_event_type_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        audit_event_type_cd = d.pop("auditEventTypeCd", UNSET)

        audit_event_type_code = d.pop("auditEventTypeCode", UNSET)

        audit_event_type_description = d.pop("auditEventTypeDescription", UNSET)

        audit_event_type_name = d.pop("auditEventTypeName", UNSET)

        audit_event_type = cls(
            audit_event_type_cd=audit_event_type_cd,
            audit_event_type_code=audit_event_type_code,
            audit_event_type_description=audit_event_type_description,
            audit_event_type_name=audit_event_type_name,
        )

        audit_event_type.additional_properties = d
        return audit_event_type

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
