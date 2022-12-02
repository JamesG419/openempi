from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportParameter")


@attr.s(auto_attribs=True)
class ReportParameter:
    """
    Attributes:
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        name_displayed (Union[Unset, str]):
        parameter_datatype (Union[Unset, int]):
        report_parameter_id (Union[Unset, int]):
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    name_displayed: Union[Unset, str] = UNSET
    parameter_datatype: Union[Unset, int] = UNSET
    report_parameter_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        name_displayed = self.name_displayed
        parameter_datatype = self.parameter_datatype
        report_parameter_id = self.report_parameter_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if name_displayed is not UNSET:
            field_dict["nameDisplayed"] = name_displayed
        if parameter_datatype is not UNSET:
            field_dict["parameterDatatype"] = parameter_datatype
        if report_parameter_id is not UNSET:
            field_dict["reportParameterId"] = report_parameter_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        name_displayed = d.pop("nameDisplayed", UNSET)

        parameter_datatype = d.pop("parameterDatatype", UNSET)

        report_parameter_id = d.pop("reportParameterId", UNSET)

        report_parameter = cls(
            description=description,
            name=name,
            name_displayed=name_displayed,
            parameter_datatype=parameter_datatype,
            report_parameter_id=report_parameter_id,
        )

        report_parameter.additional_properties = d
        return report_parameter

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
