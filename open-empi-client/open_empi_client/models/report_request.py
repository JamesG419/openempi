import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity import Entity
    from ..models.report_request_parameter import ReportRequestParameter


T = TypeVar("T", bound="ReportRequest")


@attr.s(auto_attribs=True)
class ReportRequest:
    """
    Attributes:
        entity (Union[Unset, Entity]):
        report_id (Union[Unset, int]):
        report_parameters (Union[Unset, List['ReportRequestParameter']]):
        request_date (Union[Unset, datetime.datetime]):
    """

    entity: Union[Unset, "Entity"] = UNSET
    report_id: Union[Unset, int] = UNSET
    report_parameters: Union[Unset, List["ReportRequestParameter"]] = UNSET
    request_date: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.entity, Unset):
            entity = self.entity.to_dict()

        report_id = self.report_id
        report_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_parameters, Unset):
            report_parameters = []
            for report_parameters_item_data in self.report_parameters:
                report_parameters_item = report_parameters_item_data.to_dict()

                report_parameters.append(report_parameters_item)

        request_date: Union[Unset, str] = UNSET
        if not isinstance(self.request_date, Unset):
            request_date = self.request_date.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity is not UNSET:
            field_dict["entity"] = entity
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if report_parameters is not UNSET:
            field_dict["reportParameters"] = report_parameters
        if request_date is not UNSET:
            field_dict["requestDate"] = request_date

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity import Entity
        from ..models.report_request_parameter import ReportRequestParameter

        d = src_dict.copy()
        _entity = d.pop("entity", UNSET)
        entity: Union[Unset, Entity]
        if isinstance(_entity, Unset):
            entity = UNSET
        else:
            entity = Entity.from_dict(_entity)

        report_id = d.pop("reportId", UNSET)

        report_parameters = []
        _report_parameters = d.pop("reportParameters", UNSET)
        for report_parameters_item_data in _report_parameters or []:
            report_parameters_item = ReportRequestParameter.from_dict(report_parameters_item_data)

            report_parameters.append(report_parameters_item)

        _request_date = d.pop("requestDate", UNSET)
        request_date: Union[Unset, datetime.datetime]
        if isinstance(_request_date, Unset):
            request_date = UNSET
        else:
            request_date = isoparse(_request_date)

        report_request = cls(
            entity=entity,
            report_id=report_id,
            report_parameters=report_parameters,
            request_date=request_date,
        )

        report_request.additional_properties = d
        return report_request

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
