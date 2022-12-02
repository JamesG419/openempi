from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityAttributeGroupAttribute")


@attr.s(auto_attribs=True)
class EntityAttributeGroupAttribute:
    """
    Attributes:
        entity_attribute_group_attribute_id (Union[Unset, int]):
        entity_attribute_id (Union[Unset, int]):
    """

    entity_attribute_group_attribute_id: Union[Unset, int] = UNSET
    entity_attribute_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_attribute_group_attribute_id = self.entity_attribute_group_attribute_id
        entity_attribute_id = self.entity_attribute_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_attribute_group_attribute_id is not UNSET:
            field_dict["entityAttributeGroupAttributeId"] = entity_attribute_group_attribute_id
        if entity_attribute_id is not UNSET:
            field_dict["entityAttributeId"] = entity_attribute_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        entity_attribute_group_attribute_id = d.pop("entityAttributeGroupAttributeId", UNSET)

        entity_attribute_id = d.pop("entityAttributeId", UNSET)

        entity_attribute_group_attribute = cls(
            entity_attribute_group_attribute_id=entity_attribute_group_attribute_id,
            entity_attribute_id=entity_attribute_id,
        )

        entity_attribute_group_attribute.additional_properties = d
        return entity_attribute_group_attribute

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
