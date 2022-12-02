from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.report_parameter import ReportParameter


T = TypeVar("T", bound="Report")


@attr.s(auto_attribs=True)
class Report:
    """
    Attributes:
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        name_displayed (Union[Unset, str]):
        report_id (Union[Unset, int]):
        report_parameters (Union[Unset, List['ReportParameter']]):
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_displayed: Union[Unset, str] = UNSET
    report_id: Union[Unset, int] = UNSET
    report_parameters: Union[Unset, List["ReportParameter"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        name_displayed = self.name_displayed
        report_id = self.report_id
        report_parameters: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.report_parameters, Unset):
            report_parameters = []
            for report_parameters_item_data in self.report_parameters:
                report_parameters_item = report_parameters_item_data.to_dict()

                report_parameters.append(report_parameters_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if name_displayed is not UNSET:
            field_dict["nameDisplayed"] = name_displayed
        if report_id is not UNSET:
            field_dict["reportId"] = report_id
        if report_parameters is not UNSET:
            field_dict["reportParameters"] = report_parameters

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.report_parameter import ReportParameter

        d = src_dict.copy()
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        name_displayed = d.pop("nameDisplayed", UNSET)

        report_id = d.pop("reportId", UNSET)

        report_parameters = []
        _report_parameters = d.pop("reportParameters", UNSET)
        for report_parameters_item_data in _report_parameters or []:
            report_parameters_item = ReportParameter.from_dict(report_parameters_item_data)

            report_parameters.append(report_parameters_item)

        report = cls(
            description=description,
            name=name,
            name_displayed=name_displayed,
            report_id=report_id,
            report_parameters=report_parameters,
        )

        report.additional_properties = d
        return report

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
