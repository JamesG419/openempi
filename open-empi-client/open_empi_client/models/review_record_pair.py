import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.link_source import LinkSource
    from ..models.person import Person
    from ..models.user import User


T = TypeVar("T", bound="ReviewRecordPair")


@attr.s(auto_attribs=True)
class ReviewRecordPair:
    """
    Attributes:
        date_created (Union[Unset, datetime.datetime]):
        date_reviewed (Union[Unset, datetime.datetime]):
        link_source (Union[Unset, LinkSource]):
        person_left (Union[Unset, Person]):
        person_right (Union[Unset, Person]):
        records_mathch (Union[Unset, bool]):
        review_record_pair_id (Union[Unset, int]):
        user_created_by (Union[Unset, User]):
        user_reviewed_by (Union[Unset, User]):
        vector (Union[Unset, int]):
        weight (Union[Unset, float]):
    """

    date_created: Union[Unset, datetime.datetime] = UNSET
    date_reviewed: Union[Unset, datetime.datetime] = UNSET
    link_source: Union[Unset, "LinkSource"] = UNSET
    person_left: Union[Unset, "Person"] = UNSET
    person_right: Union[Unset, "Person"] = UNSET
    records_mathch: Union[Unset, bool] = UNSET
    review_record_pair_id: Union[Unset, int] = UNSET
    user_created_by: Union[Unset, "User"] = UNSET
    user_reviewed_by: Union[Unset, "User"] = UNSET
    vector: Union[Unset, int] = UNSET
    weight: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_reviewed: Union[Unset, str] = UNSET
        if not isinstance(self.date_reviewed, Unset):
            date_reviewed = self.date_reviewed.isoformat()

        link_source: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.link_source, Unset):
            link_source = self.link_source.to_dict()

        person_left: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person_left, Unset):
            person_left = self.person_left.to_dict()

        person_right: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.person_right, Unset):
            person_right = self.person_right.to_dict()

        records_mathch = self.records_mathch
        review_record_pair_id = self.review_record_pair_id
        user_created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_created_by, Unset):
            user_created_by = self.user_created_by.to_dict()

        user_reviewed_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_reviewed_by, Unset):
            user_reviewed_by = self.user_reviewed_by.to_dict()

        vector = self.vector
        weight = self.weight

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_reviewed is not UNSET:
            field_dict["dateReviewed"] = date_reviewed
        if link_source is not UNSET:
            field_dict["linkSource"] = link_source
        if person_left is not UNSET:
            field_dict["personLeft"] = person_left
        if person_right is not UNSET:
            field_dict["personRight"] = person_right
        if records_mathch is not UNSET:
            field_dict["recordsMathch"] = records_mathch
        if review_record_pair_id is not UNSET:
            field_dict["reviewRecordPairId"] = review_record_pair_id
        if user_created_by is not UNSET:
            field_dict["userCreatedBy"] = user_created_by
        if user_reviewed_by is not UNSET:
            field_dict["userReviewedBy"] = user_reviewed_by
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
        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_reviewed = d.pop("dateReviewed", UNSET)
        date_reviewed: Union[Unset, datetime.datetime]
        if isinstance(_date_reviewed, Unset):
            date_reviewed = UNSET
        else:
            date_reviewed = isoparse(_date_reviewed)

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

        _person_right = d.pop("personRight", UNSET)
        person_right: Union[Unset, Person]
        if isinstance(_person_right, Unset):
            person_right = UNSET
        else:
            person_right = Person.from_dict(_person_right)

        records_mathch = d.pop("recordsMathch", UNSET)

        review_record_pair_id = d.pop("reviewRecordPairId", UNSET)

        _user_created_by = d.pop("userCreatedBy", UNSET)
        user_created_by: Union[Unset, User]
        if isinstance(_user_created_by, Unset):
            user_created_by = UNSET
        else:
            user_created_by = User.from_dict(_user_created_by)

        _user_reviewed_by = d.pop("userReviewedBy", UNSET)
        user_reviewed_by: Union[Unset, User]
        if isinstance(_user_reviewed_by, Unset):
            user_reviewed_by = UNSET
        else:
            user_reviewed_by = User.from_dict(_user_reviewed_by)

        vector = d.pop("vector", UNSET)

        weight = d.pop("weight", UNSET)

        review_record_pair = cls(
            date_created=date_created,
            date_reviewed=date_reviewed,
            link_source=link_source,
            person_left=person_left,
            person_right=person_right,
            records_mathch=records_mathch,
            review_record_pair_id=review_record_pair_id,
            user_created_by=user_created_by,
            user_reviewed_by=user_reviewed_by,
            vector=vector,
            weight=weight,
        )

        review_record_pair.additional_properties = d
        return review_record_pair

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
