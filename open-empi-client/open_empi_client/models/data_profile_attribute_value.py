from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataProfileAttributeValue")


@attr.s(auto_attribs=True)
class DataProfileAttributeValue:
    """
    Attributes:
        attribute_id (Union[Unset, int]):
        attribute_value (Union[Unset, str]):
        attribute_value_id (Union[Unset, int]):
        frequency (Union[Unset, int]):
    """

    attribute_id: Union[Unset, int] = UNSET
    attribute_value: Union[Unset, str] = UNSET
    attribute_value_id: Union[Unset, int] = UNSET
    frequency: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_id = self.attribute_id
        attribute_value = self.attribute_value
        attribute_value_id = self.attribute_value_id
        frequency = self.frequency

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_id is not UNSET:
            field_dict["attributeId"] = attribute_id
        if attribute_value is not UNSET:
            field_dict["attributeValue"] = attribute_value
        if attribute_value_id is not UNSET:
            field_dict["attributeValueId"] = attribute_value_id
        if frequency is not UNSET:
            field_dict["frequency"] = frequency

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_id = d.pop("attributeId", UNSET)

        attribute_value = d.pop("attributeValue", UNSET)

        attribute_value_id = d.pop("attributeValueId", UNSET)

        frequency = d.pop("frequency", UNSET)

        data_profile_attribute_value = cls(
            attribute_id=attribute_id,
            attribute_value=attribute_value,
            attribute_value_id=attribute_value_id,
            frequency=frequency,
        )

        data_profile_attribute_value.additional_properties = d
        return data_profile_attribute_value

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
