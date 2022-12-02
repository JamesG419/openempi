from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Permission")


@attr.s(auto_attribs=True)
class Permission:
    """
    Attributes:
        description (Union[Unset, str]):
        name (Union[Unset, str]):
        permission_id (Union[Unset, int]):
    """

    description: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    permission_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        name = self.name
        permission_id = self.permission_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if name is not UNSET:
            field_dict["name"] = name
        if permission_id is not UNSET:
            field_dict["permissionId"] = permission_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        name = d.pop("name", UNSET)

        permission_id = d.pop("permissionId", UNSET)

        permission = cls(
            description=description,
            name=name,
            permission_id=permission_id,
        )

        permission.additional_properties = d
        return permission

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
