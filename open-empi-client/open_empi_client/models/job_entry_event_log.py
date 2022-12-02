from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobEntryEventLog")


@attr.s(auto_attribs=True)
class JobEntryEventLog:
    """
    Attributes:
        date_created (Union[Unset, str]):
        event_entry_event_log_id (Union[Unset, int]):
        log_message (Union[Unset, str]):
    """

    date_created: Union[Unset, str] = UNSET
    event_entry_event_log_id: Union[Unset, int] = UNSET
    log_message: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created = self.date_created
        event_entry_event_log_id = self.event_entry_event_log_id
        log_message = self.log_message

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if event_entry_event_log_id is not UNSET:
            field_dict["eventEntryEventLogId"] = event_entry_event_log_id
        if log_message is not UNSET:
            field_dict["logMessage"] = log_message

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_created = d.pop("dateCreated", UNSET)

        event_entry_event_log_id = d.pop("eventEntryEventLogId", UNSET)

        log_message = d.pop("logMessage", UNSET)

        job_entry_event_log = cls(
            date_created=date_created,
            event_entry_event_log_id=event_entry_event_log_id,
            log_message=log_message,
        )

        job_entry_event_log.additional_properties = d
        return job_entry_event_log

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
