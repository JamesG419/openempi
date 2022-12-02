from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportRequestParameter")


@attr.s(auto_attribs=True)
class ReportRequestParameter:
    """
    Attributes:
        parameter_name (Union[Unset, str]):
        parameter_value (Union[Unset, str]):
    """

    parameter_name: Union[Unset, str] = UNSET
    parameter_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parameter_name = self.parameter_name
        parameter_value = self.parameter_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parameter_name is not UNSET:
            field_dict["parameterName"] = parameter_name
        if parameter_value is not UNSET:
            field_dict["parameterValue"] = parameter_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parameter_name = d.pop("parameterName", UNSET)

        parameter_value = d.pop("parameterValue", UNSET)

        report_request_parameter = cls(
            parameter_name=parameter_name,
            parameter_value=parameter_value,
        )

        report_request_parameter.additional_properties = d
        return report_request_parameter

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
