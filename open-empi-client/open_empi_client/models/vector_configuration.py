from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="VectorConfiguration")


@attr.s(auto_attribs=True)
class VectorConfiguration:
    """
    Attributes:
        algorithm_classification (Union[Unset, int]):
        logged_link_count (Union[Unset, int]):
        manual_classification (Union[Unset, int]):
        vector_value (Union[Unset, int]):
        weight (Union[Unset, float]):
    """

    algorithm_classification: Union[Unset, int] = UNSET
    logged_link_count: Union[Unset, int] = UNSET
    manual_classification: Union[Unset, int] = UNSET
    vector_value: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        algorithm_classification = self.algorithm_classification
        logged_link_count = self.logged_link_count
        manual_classification = self.manual_classification
        vector_value = self.vector_value
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if algorithm_classification is not UNSET:
            field_dict["algorithmClassification"] = algorithm_classification
        if logged_link_count is not UNSET:
            field_dict["loggedLinkCount"] = logged_link_count
        if manual_classification is not UNSET:
            field_dict["manualClassification"] = manual_classification
        if vector_value is not UNSET:
            field_dict["vectorValue"] = vector_value
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        algorithm_classification = d.pop("algorithmClassification", UNSET)

        logged_link_count = d.pop("loggedLinkCount", UNSET)

        manual_classification = d.pop("manualClassification", UNSET)

        vector_value = d.pop("vectorValue", UNSET)

        weight = d.pop("weight", UNSET)

        vector_configuration = cls(
            algorithm_classification=algorithm_classification,
            logged_link_count=logged_link_count,
            manual_classification=manual_classification,
            vector_value=vector_value,
            weight=weight,
        )

        vector_configuration.additional_properties = d
        return vector_configuration

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
