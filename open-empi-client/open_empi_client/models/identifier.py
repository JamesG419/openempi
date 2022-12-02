import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.identifier_domain import IdentifierDomain


T = TypeVar("T", bound="Identifier")


@attr.s(auto_attribs=True)
class Identifier:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]):
        date_voided (Union[Unset, datetime.datetime]):
        identifier (Union[Unset, str]):
        identifier_domain (Union[Unset, IdentifierDomain]):
        identifier_domain_id (Union[Unset, int]):
        identifier_id (Union[Unset, int]):
        internal_record_id (Union[Unset, str]):
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    date_voided: Union[Unset, datetime.datetime] = UNSET
    identifier: Union[Unset, str] = UNSET
    identifier_domain: Union[Unset, "IdentifierDomain"] = UNSET
    identifier_domain_id: Union[Unset, int] = UNSET
    identifier_id: Union[Unset, int] = UNSET
    internal_record_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_voided: Union[Unset, str] = UNSET
        if not isinstance(self.date_voided, Unset):
            date_voided = self.date_voided.isoformat()

        identifier = self.identifier
        identifier_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.identifier_domain, Unset):
            identifier_domain = self.identifier_domain.to_dict()

        identifier_domain_id = self.identifier_domain_id
        identifier_id = self.identifier_id
        internal_record_id = self.internal_record_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_voided is not UNSET:
            field_dict["dateVoided"] = date_voided
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if identifier_domain is not UNSET:
            field_dict["identifierDomain"] = identifier_domain
        if identifier_domain_id is not UNSET:
            field_dict["identifierDomainId"] = identifier_domain_id
        if identifier_id is not UNSET:
            field_dict["identifierId"] = identifier_id
        if internal_record_id is not UNSET:
            field_dict["internalRecordId"] = internal_record_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.identifier_domain import IdentifierDomain

        d = src_dict.copy()
        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_voided = d.pop("dateVoided", UNSET)
        date_voided: Union[Unset, datetime.datetime]
        if isinstance(_date_voided, Unset):
            date_voided = UNSET
        else:
            date_voided = isoparse(_date_voided)

        identifier = d.pop("identifier", UNSET)

        _identifier_domain = d.pop("identifierDomain", UNSET)
        identifier_domain: Union[Unset, IdentifierDomain]
        if isinstance(_identifier_domain, Unset):
            identifier_domain = UNSET
        else:
            identifier_domain = IdentifierDomain.from_dict(_identifier_domain)

        identifier_domain_id = d.pop("identifierDomainId", UNSET)

        identifier_id = d.pop("identifierId", UNSET)

        internal_record_id = d.pop("internalRecordId", UNSET)

        identifier = cls(
            date_created=date_created,
            date_voided=date_voided,
            identifier=identifier,
            identifier_domain=identifier_domain,
            identifier_domain_id=identifier_domain_id,
            identifier_id=identifier_id,
            internal_record_id=internal_record_id,
        )

        identifier.additional_properties = d
        return identifier

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
