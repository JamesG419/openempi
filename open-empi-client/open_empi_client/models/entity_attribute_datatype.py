from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityAttributeDatatype")


@attr.s(auto_attribs=True)
class EntityAttributeDatatype:
    """
    Attributes:
        datatype_cd (Union[Unset, int]):
        display_name (Union[Unset, str]):
        name (Union[Unset, str]):
    """

    datatype_cd: Union[Unset, int] = UNSET
    display_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        datatype_cd = self.datatype_cd
        display_name = self.display_name
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if datatype_cd is not UNSET:
            field_dict["datatypeCd"] = datatype_cd
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        datatype_cd = d.pop("datatypeCd", UNSET)

        display_name = d.pop("displayName", UNSET)

        name = d.pop("name", UNSET)

        entity_attribute_datatype = cls(
            datatype_cd=datatype_cd,
            display_name=display_name,
            name=name,
        )

        entity_attribute_datatype.additional_properties = d
        return entity_attribute_datatype

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
