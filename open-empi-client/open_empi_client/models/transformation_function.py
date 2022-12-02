from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TransformationFunction")


@attr.s(auto_attribs=True)
class TransformationFunction:
    """
    Attributes:
        function_name (Union[Unset, str]):
        name (Union[Unset, str]):
        parameter_names (Union[Unset, List[str]]):
    """

    function_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    parameter_names: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function_name = self.function_name
        name = self.name
        parameter_names: Union[Unset, List[str]] = UNSET
        if not isinstance(self.parameter_names, Unset):
            parameter_names = self.parameter_names

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if name is not UNSET:
            field_dict["name"] = name
        if parameter_names is not UNSET:
            field_dict["parameterNames"] = parameter_names

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        function_name = d.pop("functionName", UNSET)

        name = d.pop("name", UNSET)

        parameter_names = cast(List[str], d.pop("parameterNames", UNSET))

        transformation_function = cls(
            function_name=function_name,
            name=name,
            parameter_names=parameter_names,
        )

        transformation_function.additional_properties = d
        return transformation_function

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
