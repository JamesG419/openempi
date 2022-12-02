import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_update_entry import IdentifierUpdateEntry


T = TypeVar("T", bound="IdentifierUpdateEvent")


@attr.s(auto_attribs=True)
class IdentifierUpdateEvent:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]):
        identifier_update_event_id (Union[Unset, int]):
        post_update_identifiers (Union[Unset, List['IdentifierUpdateEntry']]):
        pre_update_identifiers (Union[Unset, List['IdentifierUpdateEntry']]):
        source (Union[Unset, str]):
        transition (Union[Unset, str]):
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    identifier_update_event_id: Union[Unset, int] = UNSET
    post_update_identifiers: Union[Unset, List["IdentifierUpdateEntry"]] = UNSET
    pre_update_identifiers: Union[Unset, List["IdentifierUpdateEntry"]] = UNSET
    source: Union[Unset, str] = UNSET
    transition: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        identifier_update_event_id = self.identifier_update_event_id
        post_update_identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.post_update_identifiers, Unset):
            post_update_identifiers = []
            for post_update_identifiers_item_data in self.post_update_identifiers:
                post_update_identifiers_item = post_update_identifiers_item_data.to_dict()

                post_update_identifiers.append(post_update_identifiers_item)

        pre_update_identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pre_update_identifiers, Unset):
            pre_update_identifiers = []
            for pre_update_identifiers_item_data in self.pre_update_identifiers:
                pre_update_identifiers_item = pre_update_identifiers_item_data.to_dict()

                pre_update_identifiers.append(pre_update_identifiers_item)

        source = self.source
        transition = self.transition

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if identifier_update_event_id is not UNSET:
            field_dict["identifierUpdateEventId"] = identifier_update_event_id
        if post_update_identifiers is not UNSET:
            field_dict["postUpdateIdentifiers"] = post_update_identifiers
        if pre_update_identifiers is not UNSET:
            field_dict["preUpdateIdentifiers"] = pre_update_identifiers
        if source is not UNSET:
            field_dict["source"] = source
        if transition is not UNSET:
            field_dict["transition"] = transition

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_update_entry import IdentifierUpdateEntry

        d = src_dict.copy()
        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        identifier_update_event_id = d.pop("identifierUpdateEventId", UNSET)

        post_update_identifiers = []
        _post_update_identifiers = d.pop("postUpdateIdentifiers", UNSET)
        for post_update_identifiers_item_data in _post_update_identifiers or []:
            post_update_identifiers_item = IdentifierUpdateEntry.from_dict(post_update_identifiers_item_data)

            post_update_identifiers.append(post_update_identifiers_item)

        pre_update_identifiers = []
        _pre_update_identifiers = d.pop("preUpdateIdentifiers", UNSET)
        for pre_update_identifiers_item_data in _pre_update_identifiers or []:
            pre_update_identifiers_item = IdentifierUpdateEntry.from_dict(pre_update_identifiers_item_data)

            pre_update_identifiers.append(pre_update_identifiers_item)

        source = d.pop("source", UNSET)

        transition = d.pop("transition", UNSET)

        identifier_update_event = cls(
            date_created=date_created,
            identifier_update_event_id=identifier_update_event_id,
            post_update_identifiers=post_update_identifiers,
            pre_update_identifiers=pre_update_identifiers,
            source=source,
            transition=transition,
        )

        identifier_update_event.additional_properties = d
        return identifier_update_event

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
