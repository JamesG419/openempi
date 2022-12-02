from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.person import Person


T = TypeVar("T", bound="PersonPagedRequest")


@attr.s(auto_attribs=True)
class PersonPagedRequest:
    """
    Attributes:
        first_result (Union[Unset, int]):
        max_results (Union[Unset, int]):
        person (Union[Unset, Person]):
    """

    first_result: Union[Unset, int] = UNSET
    max_results: Union[Unset, int] = UNSET
    person: Union[Unset, "Person"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        first_result = self.first_result
        max_results = self.max_results
        person: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person, Unset):
            person = self.person.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if first_result is not UNSET:
            field_dict["firstResult"] = first_result
        if max_results is not UNSET:
            field_dict["maxResults"] = max_results
        if person is not UNSET:
            field_dict["person"] = person

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.person import Person

        d = src_dict.copy()
        first_result = d.pop("firstResult", UNSET)

        max_results = d.pop("maxResults", UNSET)

        _person = d.pop("person", UNSET)
        person: Union[Unset, Person]
        if isinstance(_person, Unset):
            person = UNSET
        else:
            person = Person.from_dict(_person)

        person_paged_request = cls(
            first_result=first_result,
            max_results=max_results,
            person=person,
        )

        person_paged_request.additional_properties = d
        return person_paged_request

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
