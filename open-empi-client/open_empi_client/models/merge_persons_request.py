from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person_identifier import PersonIdentifier


T = TypeVar("T", bound="MergePersonsRequest")


@attr.s(auto_attribs=True)
class MergePersonsRequest:
    """
    Attributes:
        retired_identifier (Union[Unset, PersonIdentifier]):
        surviving_identifier (Union[Unset, PersonIdentifier]):
    """

    retired_identifier: Union[Unset, "PersonIdentifier"] = UNSET
    surviving_identifier: Union[Unset, "PersonIdentifier"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        retired_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.retired_identifier, Unset):
            retired_identifier = self.retired_identifier.to_dict()

        surviving_identifier: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.surviving_identifier, Unset):
            surviving_identifier = self.surviving_identifier.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retired_identifier is not UNSET:
            field_dict["retiredIdentifier"] = retired_identifier
        if surviving_identifier is not UNSET:
            field_dict["survivingIdentifier"] = surviving_identifier

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person_identifier import PersonIdentifier

        d = src_dict.copy()
        _retired_identifier = d.pop("retiredIdentifier", UNSET)
        retired_identifier: Union[Unset, PersonIdentifier]
        if isinstance(_retired_identifier, Unset):
            retired_identifier = UNSET
        else:
            retired_identifier = PersonIdentifier.from_dict(_retired_identifier)

        _surviving_identifier = d.pop("survivingIdentifier", UNSET)
        surviving_identifier: Union[Unset, PersonIdentifier]
        if isinstance(_surviving_identifier, Unset):
            surviving_identifier = UNSET
        else:
            surviving_identifier = PersonIdentifier.from_dict(_surviving_identifier)

        merge_persons_request = cls(
            retired_identifier=retired_identifier,
            surviving_identifier=surviving_identifier,
        )

        merge_persons_request.additional_properties = d
        return merge_persons_request

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
