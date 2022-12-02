from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="File")


@attr.s(auto_attribs=True)
class File:
    """
    Attributes:
        date_created_str (Union[Unset, str]):
        filename (Union[Unset, str]):
        imported (Union[Unset, str]):
        is_entity (Union[Unset, str]):
        name (Union[Unset, str]):
        owner_id (Union[Unset, int]):
        profiled (Union[Unset, str]):
        user_file_id (Union[Unset, int]):
    """

    date_created_str: Union[Unset, str] = UNSET
    filename: Union[Unset, str] = UNSET
    imported: Union[Unset, str] = UNSET
    is_entity: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    owner_id: Union[Unset, int] = UNSET
    profiled: Union[Unset, str] = UNSET
    user_file_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created_str = self.date_created_str
        filename = self.filename
        imported = self.imported
        is_entity = self.is_entity
        name = self.name
        owner_id = self.owner_id
        profiled = self.profiled
        user_file_id = self.user_file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created_str is not UNSET:
            field_dict["dateCreatedStr"] = date_created_str
        if filename is not UNSET:
            field_dict["filename"] = filename
        if imported is not UNSET:
            field_dict["imported"] = imported
        if is_entity is not UNSET:
            field_dict["isEntity"] = is_entity
        if name is not UNSET:
            field_dict["name"] = name
        if owner_id is not UNSET:
            field_dict["ownerId"] = owner_id
        if profiled is not UNSET:
            field_dict["profiled"] = profiled
        if user_file_id is not UNSET:
            field_dict["userFileId"] = user_file_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        date_created_str = d.pop("dateCreatedStr", UNSET)

        filename = d.pop("filename", UNSET)

        imported = d.pop("imported", UNSET)

        is_entity = d.pop("isEntity", UNSET)

        name = d.pop("name", UNSET)

        owner_id = d.pop("ownerId", UNSET)

        profiled = d.pop("profiled", UNSET)

        user_file_id = d.pop("userFileId", UNSET)

        file = cls(
            date_created_str=date_created_str,
            filename=filename,
            imported=imported,
            is_entity=is_entity,
            name=name,
            owner_id=owner_id,
            profiled=profiled,
            user_file_id=user_file_id,
        )

        file.additional_properties = d
        return file

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
