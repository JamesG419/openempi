import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user import User


T = TypeVar("T", bound="UserFile")


@attr.s(auto_attribs=True)
class UserFile:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]):
        filename (Union[Unset, str]):
        imported (Union[Unset, str]):
        is_entity (Union[Unset, bool]):
        name (Union[Unset, str]):
        owner (Union[Unset, User]):
        profile_processed (Union[Unset, str]):
        profiled (Union[Unset, str]):
        rows_imported (Union[Unset, int]):
        rows_processed (Union[Unset, int]):
        user_file_id (Union[Unset, int]):
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    filename: Union[Unset, str] = UNSET
    imported: Union[Unset, str] = UNSET
    is_entity: Union[Unset, bool] = UNSET
    name: Union[Unset, str] = UNSET
    owner: Union[Unset, "User"] = UNSET
    profile_processed: Union[Unset, str] = UNSET
    profiled: Union[Unset, str] = UNSET
    rows_imported: Union[Unset, int] = UNSET
    rows_processed: Union[Unset, int] = UNSET
    user_file_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        filename = self.filename
        imported = self.imported
        is_entity = self.is_entity
        name = self.name
        owner: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.owner, Unset):
            owner = self.owner.to_dict()

        profile_processed = self.profile_processed
        profiled = self.profiled
        rows_imported = self.rows_imported
        rows_processed = self.rows_processed
        user_file_id = self.user_file_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if filename is not UNSET:
            field_dict["filename"] = filename
        if imported is not UNSET:
            field_dict["imported"] = imported
        if is_entity is not UNSET:
            field_dict["isEntity"] = is_entity
        if name is not UNSET:
            field_dict["name"] = name
        if owner is not UNSET:
            field_dict["owner"] = owner
        if profile_processed is not UNSET:
            field_dict["profileProcessed"] = profile_processed
        if profiled is not UNSET:
            field_dict["profiled"] = profiled
        if rows_imported is not UNSET:
            field_dict["rowsImported"] = rows_imported
        if rows_processed is not UNSET:
            field_dict["rowsProcessed"] = rows_processed
        if user_file_id is not UNSET:
            field_dict["userFileId"] = user_file_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user import User

        d = src_dict.copy()
        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        filename = d.pop("filename", UNSET)

        imported = d.pop("imported", UNSET)

        is_entity = d.pop("isEntity", UNSET)

        name = d.pop("name", UNSET)

        _owner = d.pop("owner", UNSET)
        owner: Union[Unset, User]
        if isinstance(_owner, Unset):
            owner = UNSET
        else:
            owner = User.from_dict(_owner)

        profile_processed = d.pop("profileProcessed", UNSET)

        profiled = d.pop("profiled", UNSET)

        rows_imported = d.pop("rowsImported", UNSET)

        rows_processed = d.pop("rowsProcessed", UNSET)

        user_file_id = d.pop("userFileId", UNSET)

        user_file = cls(
            date_created=date_created,
            filename=filename,
            imported=imported,
            is_entity=is_entity,
            name=name,
            owner=owner,
            profile_processed=profile_processed,
            profiled=profiled,
            rows_imported=rows_imported,
            rows_processed=rows_processed,
            user_file_id=user_file_id,
        )

        user_file.additional_properties = d
        return user_file

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
