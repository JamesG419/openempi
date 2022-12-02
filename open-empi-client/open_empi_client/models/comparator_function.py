from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comparator_function_parameter_map import ComparatorFunctionParameterMap


T = TypeVar("T", bound="ComparatorFunction")


@attr.s(auto_attribs=True)
class ComparatorFunction:
    """
    Attributes:
        function_name (Union[Unset, str]):
        parameter_map (Union[Unset, ComparatorFunctionParameterMap]):
    """

    function_name: Union[Unset, str] = UNSET
    parameter_map: Union[Unset, "ComparatorFunctionParameterMap"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        function_name = self.function_name
        parameter_map: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.parameter_map, Unset):
            parameter_map = self.parameter_map.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if function_name is not UNSET:
            field_dict["functionName"] = function_name
        if parameter_map is not UNSET:
            field_dict["parameterMap"] = parameter_map

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comparator_function_parameter_map import ComparatorFunctionParameterMap

        d = src_dict.copy()
        function_name = d.pop("functionName", UNSET)

        _parameter_map = d.pop("parameterMap", UNSET)
        parameter_map: Union[Unset, ComparatorFunctionParameterMap]
        if isinstance(_parameter_map, Unset):
            parameter_map = UNSET
        else:
            parameter_map = ComparatorFunctionParameterMap.from_dict(_parameter_map)

        comparator_function = cls(
            function_name=function_name,
            parameter_map=parameter_map,
        )

        comparator_function.additional_properties = d
        return comparator_function

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
