from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_attribute_datatype import EntityAttributeDatatype


T = TypeVar("T", bound="EntityAttribute")


@attr.s(auto_attribs=True)
class EntityAttribute:
    """
    Attributes:
        case_insensitive (Union[Unset, bool]):
        datatype (Union[Unset, EntityAttributeDatatype]):
        date_changed_str (Union[Unset, str]):
        date_created_str (Union[Unset, str]):
        date_voided_str (Union[Unset, str]):
        description (Union[Unset, str]):
        display_name (Union[Unset, str]):
        display_order (Union[Unset, int]):
        entity_attribute_id (Union[Unset, int]):
        indexed (Union[Unset, bool]):
        is_custom (Union[Unset, bool]):
        name (Union[Unset, str]):
        searchable (Union[Unset, bool]):
        user_changed_by_id (Union[Unset, int]):
        user_created_by_id (Union[Unset, int]):
        user_voided_by_id (Union[Unset, int]):
    """

    case_insensitive: Union[Unset, bool] = UNSET
    datatype: Union[Unset, "EntityAttributeDatatype"] = UNSET
    date_changed_str: Union[Unset, str] = UNSET
    date_created_str: Union[Unset, str] = UNSET
    date_voided_str: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    display_order: Union[Unset, int] = UNSET
    entity_attribute_id: Union[Unset, int] = UNSET
    indexed: Union[Unset, bool] = UNSET
    is_custom: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    searchable: Union[Unset, bool] = UNSET
    user_changed_by_id: Union[Unset, int] = UNSET
    user_created_by_id: Union[Unset, int] = UNSET
    user_voided_by_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        case_insensitive = self.case_insensitive
        datatype: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.datatype, Unset):
            datatype = self.datatype.to_dict()

        date_changed_str = self.date_changed_str
        date_created_str = self.date_created_str
        date_voided_str = self.date_voided_str
        description = self.description
        display_name = self.display_name
        display_order = self.display_order
        entity_attribute_id = self.entity_attribute_id
        indexed = self.indexed
        is_custom = self.is_custom
        name = self.name
        searchable = self.searchable
        user_changed_by_id = self.user_changed_by_id
        user_created_by_id = self.user_created_by_id
        user_voided_by_id = self.user_voided_by_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if case_insensitive is not UNSET:
            field_dict["caseInsensitive"] = case_insensitive
        if datatype is not UNSET:
            field_dict["datatype"] = datatype
        if date_changed_str is not UNSET:
            field_dict["dateChangedStr"] = date_changed_str
        if date_created_str is not UNSET:
            field_dict["dateCreatedStr"] = date_created_str
        if date_voided_str is not UNSET:
            field_dict["dateVoidedStr"] = date_voided_str
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if display_order is not UNSET:
            field_dict["displayOrder"] = display_order
        if entity_attribute_id is not UNSET:
            field_dict["entityAttributeId"] = entity_attribute_id
        if indexed is not UNSET:
            field_dict["indexed"] = indexed
        if is_custom is not UNSET:
            field_dict["isCustom"] = is_custom
        if name is not UNSET:
            field_dict["name"] = name
        if searchable is not UNSET:
            field_dict["searchable"] = searchable
        if user_changed_by_id is not UNSET:
            field_dict["userChangedById"] = user_changed_by_id
        if user_created_by_id is not UNSET:
            field_dict["userCreatedById"] = user_created_by_id
        if user_voided_by_id is not UNSET:
            field_dict["userVoidedById"] = user_voided_by_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_attribute_datatype import EntityAttributeDatatype

        d = src_dict.copy()
        case_insensitive = d.pop("caseInsensitive", UNSET)

        _datatype = d.pop("datatype", UNSET)
        datatype: Union[Unset, EntityAttributeDatatype]
        if isinstance(_datatype, Unset):
            datatype = UNSET
        else:
            datatype = EntityAttributeDatatype.from_dict(_datatype)

        date_changed_str = d.pop("dateChangedStr", UNSET)

        date_created_str = d.pop("dateCreatedStr", UNSET)

        date_voided_str = d.pop("dateVoidedStr", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("displayName", UNSET)

        display_order = d.pop("displayOrder", UNSET)

        entity_attribute_id = d.pop("entityAttributeId", UNSET)

        indexed = d.pop("indexed", UNSET)

        is_custom = d.pop("isCustom", UNSET)

        name = d.pop("name", UNSET)

        searchable = d.pop("searchable", UNSET)

        user_changed_by_id = d.pop("userChangedById", UNSET)

        user_created_by_id = d.pop("userCreatedById", UNSET)

        user_voided_by_id = d.pop("userVoidedById", UNSET)

        entity_attribute = cls(
            case_insensitive=case_insensitive,
            datatype=datatype,
            date_changed_str=date_changed_str,
            date_created_str=date_created_str,
            date_voided_str=date_voided_str,
            description=description,
            display_name=display_name,
            display_order=display_order,
            entity_attribute_id=entity_attribute_id,
            indexed=indexed,
            is_custom=is_custom,
            name=name,
            searchable=searchable,
            user_changed_by_id=user_changed_by_id,
            user_created_by_id=user_created_by_id,
            user_voided_by_id=user_voided_by_id,
        )

        entity_attribute.additional_properties = d
        return entity_attribute

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
