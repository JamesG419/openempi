import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_source import LinkSource
    from ..models.person import Person
    from ..models.user import User


T = TypeVar("T", bound="PersonLink")


@attr.s(auto_attribs=True)
class PersonLink:
    """
    Attributes:
        cluster_id (Union[Unset, int]):
        date_created (Union[Unset, datetime.datetime]):
        link_source (Union[Unset, LinkSource]):
        person_left (Union[Unset, Person]):
        person_link_id (Union[Unset, int]):
        person_right (Union[Unset, Person]):
        user_created_by (Union[Unset, User]):
        vector (Union[Unset, int]):
        weight (Union[Unset, float]):
    """

    cluster_id: Union[Unset, int] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    link_source: Union[Unset, "LinkSource"] = UNSET
    person_left: Union[Unset, "Person"] = UNSET
    person_link_id: Union[Unset, int] = UNSET
    person_right: Union[Unset, "Person"] = UNSET
    user_created_by: Union[Unset, "User"] = UNSET
    vector: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        cluster_id = self.cluster_id
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        link_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_source, Unset):
            link_source = self.link_source.to_dict()

        person_left: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person_left, Unset):
            person_left = self.person_left.to_dict()

        person_link_id = self.person_link_id
        person_right: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person_right, Unset):
            person_right = self.person_right.to_dict()

        user_created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_created_by, Unset):
            user_created_by = self.user_created_by.to_dict()

        vector = self.vector
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cluster_id is not UNSET:
            field_dict["clusterId"] = cluster_id
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if link_source is not UNSET:
            field_dict["linkSource"] = link_source
        if person_left is not UNSET:
            field_dict["personLeft"] = person_left
        if person_link_id is not UNSET:
            field_dict["personLinkId"] = person_link_id
        if person_right is not UNSET:
            field_dict["personRight"] = person_right
        if user_created_by is not UNSET:
            field_dict["userCreatedBy"] = user_created_by
        if vector is not UNSET:
            field_dict["vector"] = vector
        if weight is not UNSET:
            field_dict["weight"] = weight

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.link_source import LinkSource
        from ..models.person import Person
        from ..models.user import User

        d = src_dict.copy()
        cluster_id = d.pop("clusterId", UNSET)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _link_source = d.pop("linkSource", UNSET)
        link_source: Union[Unset, LinkSource]
        if isinstance(_link_source, Unset):
            link_source = UNSET
        else:
            link_source = LinkSource.from_dict(_link_source)

        _person_left = d.pop("personLeft", UNSET)
        person_left: Union[Unset, Person]
        if isinstance(_person_left, Unset):
            person_left = UNSET
        else:
            person_left = Person.from_dict(_person_left)

        person_link_id = d.pop("personLinkId", UNSET)

        _person_right = d.pop("personRight", UNSET)
        person_right: Union[Unset, Person]
        if isinstance(_person_right, Unset):
            person_right = UNSET
        else:
            person_right = Person.from_dict(_person_right)

        _user_created_by = d.pop("userCreatedBy", UNSET)
        user_created_by: Union[Unset, User]
        if isinstance(_user_created_by, Unset):
            user_created_by = UNSET
        else:
            user_created_by = User.from_dict(_user_created_by)

        vector = d.pop("vector", UNSET)

        weight = d.pop("weight", UNSET)

        person_link = cls(
            cluster_id=cluster_id,
            date_created=date_created,
            link_source=link_source,
            person_left=person_left,
            person_link_id=person_link_id,
            person_right=person_right,
            user_created_by=user_created_by,
            vector=vector,
            weight=weight,
        )

        person_link.additional_properties = d
        return person_link

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
