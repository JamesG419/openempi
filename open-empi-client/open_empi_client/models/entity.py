from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_attribute import EntityAttribute


T = TypeVar("T", bound="Entity")


@attr.s(auto_attribs=True)
class Entity:
    """
    Attributes:
        attributes (Union[Unset, List['EntityAttribute']]):
        date_changed_str (Union[Unset, str]):
        date_created_str (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        entity_id (Union[Unset, int]):
        entity_version_id (Union[Unset, int]):
        name (Union[Unset, str]):
        synchronous_matching (Union[Unset, bool]):
        user_changed_by_id (Union[Unset, int]):
        user_created_by_id (Union[Unset, int]):
        user_voided_by_id (Union[Unset, int]):
        version_id (Union[Unset, int]):
    """

    attributes: Union[Unset, List["EntityAttribute"]] = UNSET
    date_changed_str: Union[Unset, str] = UNSET
    date_created_str: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    entity_id: Union[Unset, int] = UNSET
    entity_version_id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    synchronous_matching: Union[Unset, bool] = UNSET
    user_changed_by_id: Union[Unset, int] = UNSET
    user_created_by_id: Union[Unset, int] = UNSET
    user_voided_by_id: Union[Unset, int] = UNSET
    version_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attributes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = []
            for attributes_item_data in self.attributes:
                attributes_item = attributes_item_data.to_dict()

                attributes.append(attributes_item)

        date_changed_str = self.date_changed_str
        date_created_str = self.date_created_str
        description = self.description
        display_name = self.display_name
        entity_id = self.entity_id
        entity_version_id = self.entity_version_id
        name = self.name
        synchronous_matching = self.synchronous_matching
        user_changed_by_id = self.user_changed_by_id
        user_created_by_id = self.user_created_by_id
        user_voided_by_id = self.user_voided_by_id
        version_id = self.version_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if date_changed_str is not UNSET:
            field_dict["dateChangedStr"] = date_changed_str
        if date_created_str is not UNSET:
            field_dict["dateCreatedStr"] = date_created_str
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if entity_version_id is not UNSET:
            field_dict["entityVersionId"] = entity_version_id
        if name is not UNSET:
            field_dict["name"] = name
        if synchronous_matching is not UNSET:
            field_dict["synchronousMatching"] = synchronous_matching
        if user_changed_by_id is not UNSET:
            field_dict["userChangedById"] = user_changed_by_id
        if user_created_by_id is not UNSET:
            field_dict["userCreatedById"] = user_created_by_id
        if user_voided_by_id is not UNSET:
            field_dict["userVoidedById"] = user_voided_by_id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_attribute import EntityAttribute

        d = src_dict.copy()
        attributes = []
        _attributes = d.pop("attributes", UNSET)
        for attributes_item_data in _attributes or []:
            attributes_item = EntityAttribute.from_dict(attributes_item_data)

            attributes.append(attributes_item)

        date_changed_str = d.pop("dateChangedStr", UNSET)

        date_created_str = d.pop("dateCreatedStr", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        entity_id = d.pop("entityId", UNSET)

        entity_version_id = d.pop("entityVersionId", UNSET)

        name = d.pop("name", UNSET)

        synchronous_matching = d.pop("synchronousMatching", UNSET)

        user_changed_by_id = d.pop("userChangedById", UNSET)

        user_created_by_id = d.pop("userCreatedById", UNSET)

        user_voided_by_id = d.pop("userVoidedById", UNSET)

        version_id = d.pop("versionId", UNSET)

        entity = cls(
            attributes=attributes,
            date_changed_str=date_changed_str,
            date_created_str=date_created_str,
            description=description,
            display_name=display_name,
            entity_id=entity_id,
            entity_version_id=entity_version_id,
            name=name,
            synchronous_matching=synchronous_matching,
            user_changed_by_id=user_changed_by_id,
            user_created_by_id=user_created_by_id,
            user_voided_by_id=user_voided_by_id,
            version_id=version_id,
        )

        entity.additional_properties = d
        return entity

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
