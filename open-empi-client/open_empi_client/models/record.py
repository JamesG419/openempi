from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.field_value import FieldValue
    from ..models.identifier import Identifier
    from ..models.user import User


T = TypeVar("T", bound="Record")


@attr.s(auto_attribs=True)
class Record:
    """
    Attributes:
        date_changed (Union[Unset, str]):
        date_created (Union[Unset, str]):
        date_voided (Union[Unset, str]):
        entity_id (Union[Unset, int]):
        fields (Union[Unset, List['FieldValue']]):
        identifiers (Union[Unset, List['Identifier']]):
        internal_record_id (Union[Unset, str]):
        record_id (Union[Unset, int]):
        user_changed_by (Union[Unset, User]):
        user_created_by (Union[Unset, User]):
        user_voided_by (Union[Unset, User]):
    """

    date_changed: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_voided: Union[Unset, str] = UNSET
    entity_id: Union[Unset, int] = UNSET
    fields: Union[Unset, List["FieldValue"]] = UNSET
    identifiers: Union[Unset, List["Identifier"]] = UNSET
    internal_record_id: Union[Unset, str] = UNSET
    record_id: Union[Unset, int] = UNSET
    user_changed_by: Union[Unset, "User"] = UNSET
    user_created_by: Union[Unset, "User"] = UNSET
    user_voided_by: Union[Unset, "User"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_changed = self.date_changed
        date_created = self.date_created
        date_voided = self.date_voided
        entity_id = self.entity_id
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = []
            for identifiers_item_data in self.identifiers:
                identifiers_item = identifiers_item_data.to_dict()

                identifiers.append(identifiers_item)

        internal_record_id = self.internal_record_id
        record_id = self.record_id
        user_changed_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_changed_by, Unset):
            user_changed_by = self.user_changed_by.to_dict()

        user_created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_created_by, Unset):
            user_created_by = self.user_created_by.to_dict()

        user_voided_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_voided_by, Unset):
            user_voided_by = self.user_voided_by.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_changed is not UNSET:
            field_dict["dateChanged"] = date_changed
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_voided is not UNSET:
            field_dict["dateVoided"] = date_voided
        if entity_id is not UNSET:
            field_dict["entityId"] = entity_id
        if fields is not UNSET:
            field_dict["fields"] = fields
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if internal_record_id is not UNSET:
            field_dict["internalRecordId"] = internal_record_id
        if record_id is not UNSET:
            field_dict["recordId"] = record_id
        if user_changed_by is not UNSET:
            field_dict["userChangedBy"] = user_changed_by
        if user_created_by is not UNSET:
            field_dict["userCreatedBy"] = user_created_by
        if user_voided_by is not UNSET:
            field_dict["userVoidedBy"] = user_voided_by

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.field_value import FieldValue
        from ..models.identifier import Identifier
        from ..models.user import User

        d = src_dict.copy()
        date_changed = d.pop("dateChanged", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        date_voided = d.pop("dateVoided", UNSET)

        entity_id = d.pop("entityId", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = FieldValue.from_dict(fields_item_data)

            fields.append(fields_item)

        identifiers = []
        _identifiers = d.pop("identifiers", UNSET)
        for identifiers_item_data in _identifiers or []:
            identifiers_item = Identifier.from_dict(identifiers_item_data)

            identifiers.append(identifiers_item)

        internal_record_id = d.pop("internalRecordId", UNSET)

        record_id = d.pop("recordId", UNSET)

        _user_changed_by = d.pop("userChangedBy", UNSET)
        user_changed_by: Union[Unset, User]
        if isinstance(_user_changed_by, Unset):
            user_changed_by = UNSET
        else:
            user_changed_by = User.from_dict(_user_changed_by)

        _user_created_by = d.pop("userCreatedBy", UNSET)
        user_created_by: Union[Unset, User]
        if isinstance(_user_created_by, Unset):
            user_created_by = UNSET
        else:
            user_created_by = User.from_dict(_user_created_by)

        _user_voided_by = d.pop("userVoidedBy", UNSET)
        user_voided_by: Union[Unset, User]
        if isinstance(_user_voided_by, Unset):
            user_voided_by = UNSET
        else:
            user_voided_by = User.from_dict(_user_voided_by)

        record = cls(
            date_changed=date_changed,
            date_created=date_created,
            date_voided=date_voided,
            entity_id=entity_id,
            fields=fields,
            identifiers=identifiers,
            internal_record_id=internal_record_id,
            record_id=record_id,
            user_changed_by=user_changed_by,
            user_created_by=user_created_by,
            user_voided_by=user_voided_by,
        )

        record.additional_properties = d
        return record

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
