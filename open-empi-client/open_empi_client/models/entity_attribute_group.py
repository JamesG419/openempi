from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_attribute_group_attribute import EntityAttributeGroupAttribute


T = TypeVar("T", bound="EntityAttributeGroup")


@attr.s(auto_attribs=True)
class EntityAttributeGroup:
    """
    Attributes:
        display_name (Union[Unset, str]):
        display_order (Union[Unset, int]):
        entity_attribute_group_id (Union[Unset, int]):
        entity_attributes (Union[Unset, List['EntityAttributeGroupAttribute']]):
        entity_id (Union[Unset, int]):
        name (Union[Unset, str]):
    """

    display_name: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    entity_attribute_group_id: Union[Unset, int] = UNSET
    entity_attributes: Union[Unset, List["EntityAttributeGroupAttribute"]] = UNSET
    entity_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        display_name = self.display_name
        display_order = self.display_order
        entity_attribute_group_id = self.entity_attribute_group_id
        entity_attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.entity_attributes, Unset):
            entity_attributes = []
            for entity_attributes_item_data in self.entity_attributes:
                entity_attributes_item = entity_attributes_item_data.to_dict()

                entity_attributes.append(entity_attributes_item)

        entity_id = self.entity_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if entity_attribute_group_id is not UNSET:
            field_dict["entityAttributeGroupId"] = entity_attribute_group_id
        if entity_attributes is not UNSET:
            field_dict["entityAttributes"] = entity_attributes
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_attribute_group_attribute import EntityAttributeGroupAttribute

        d = src_dict.copy()
        display_name = d.pop("displayName", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        entity_attribute_group_id = d.pop("entityAttributeGroupId", UNSET)

        entity_attributes = []
        _entity_attributes = d.pop("entityAttributes", UNSET)
        for entity_attributes_item_data in _entity_attributes or []:
            entity_attributes_item = EntityAttributeGroupAttribute.from_dict(entity_attributes_item_data)

            entity_attributes.append(entity_attributes_item)

        entity_id = d.pop("entityId", UNSET)

        name = d.pop("name", UNSET)

        entity_attribute_group = cls(
            display_name=display_name,
            display_order=display_order,
            entity_attribute_group_id=entity_attribute_group_id,
            entity_attributes=entity_attributes,
            entity_id=entity_id,
            name=name,
        )

        entity_attribute_group.additional_properties = d
        return entity_attribute_group

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
