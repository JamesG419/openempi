import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.report import Report
    from ..models.user import User


T = TypeVar("T", bound="ReportRequestEntry")


@attr.s(auto_attribs=True)
class ReportRequestEntry:
    """
    Attributes:
        date_completed (Union[Unset, datetime.datetime]):
        date_completed_str (Union[Unset, str]):
        date_requested (Union[Unset, str]):
        date_requested_str (Union[Unset, str]):
        entity (Union[Unset, Entity]):
        report (Union[Unset, Report]):
        report_handle (Union[Unset, str]):
        report_request_id (Union[Unset, int]):
        user_requested (Union[Unset, User]):
    """

    date_completed: Union[Unset, datetime.datetime] = UNSET
    date_completed_str: Union[Unset, str] = UNSET
    date_requested: Union[Unset, str] = UNSET
    date_requested_str: Union[Unset, str] = UNSET
    entity: Union[Unset, "Entity"] = UNSET
    report: Union[Unset, "Report"] = UNSET
    report_handle: Union[Unset, str] = UNSET
    report_request_id: Union[Unset, int] = UNSET
    user_requested: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_completed: Union[Unset, str] = UNSET
        if not isinstance(self.date_completed, Unset):
            date_completed = self.date_completed.isoformat()

        date_completed_str = self.date_completed_str
        date_requested = self.date_requested
        date_requested_str = self.date_requested_str
        entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        report: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.report, Unset):
            report = self.report.to_dict()

        report_handle = self.report_handle
        report_request_id = self.report_request_id
        user_requested: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_requested, Unset):
            user_requested = self.user_requested.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_completed is not UNSET:
            field_dict["dateCompleted"] = date_completed
        if date_completed_str is not UNSET:
            field_dict["dateCompletedStr"] = date_completed_str
        if date_requested is not UNSET:
            field_dict["dateRequested"] = date_requested
        if date_requested_str is not UNSET:
            field_dict["dateRequestedStr"] = date_requested_str
        if entity is not UNSET:
            field_dict["entity"] = entity
        if report is not UNSET:
            field_dict["report"] = report
        if report_handle is not UNSET:
            field_dict["reportHandle"] = report_handle
        if report_request_id is not UNSET:
            field_dict["reportRequestId"] = report_request_id
        if user_requested is not UNSET:
            field_dict["userRequested"] = user_requested

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.report import Report
        from ..models.user import User

        d = src_dict.copy()
        _date_completed = d.pop("dateCompleted", UNSET)
        date_completed: Union[Unset, datetime.datetime]
        if isinstance(_date_completed, Unset):
            date_completed = UNSET
        else:
            date_completed = isoparse(_date_completed)

        date_completed_str = d.pop("dateCompletedStr", UNSET)

        date_requested = d.pop("dateRequested", UNSET)

        date_requested_str = d.pop("dateRequestedStr", UNSET)

        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, Entity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = Entity.from_dict(_entity)

        _report = d.pop("report", UNSET)
        report: Union[Unset, Report]
        if isinstance(_report, Unset):
            report = UNSET
        else:
            report = Report.from_dict(_report)

        report_handle = d.pop("reportHandle", UNSET)

        report_request_id = d.pop("reportRequestId", UNSET)

        _user_requested = d.pop("userRequested", UNSET)
        user_requested: Union[Unset, User]
        if isinstance(_user_requested, Unset):
            user_requested = UNSET
        else:
            user_requested = User.from_dict(_user_requested)

        report_request_entry = cls(
            date_completed=date_completed,
            date_completed_str=date_completed_str,
            date_requested=date_requested,
            date_requested_str=date_requested_str,
            entity=entity,
            report=report,
            report_handle=report_handle,
            report_request_id=report_request_id,
            user_requested=user_requested,
        )

        report_request_entry.additional_properties = d
        return report_request_entry

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
