from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.comparator_function import ComparatorFunction


T = TypeVar("T", bound="MatchField")


@attr.s(auto_attribs=True)
class MatchField:
    """
    Attributes:
        comparator_function (Union[Unset, ComparatorFunction]):
        field_name (Union[Unset, str]):
        match_threshold (Union[Unset, float]):
        mvalue (Union[Unset, float]):
        null_scoring (Union[Unset, bool]):
        null_weight (Union[Unset, float]):
        uvalue (Union[Unset, float]):
    """

    comparator_function: Union[Unset, "ComparatorFunction"] = UNSET
    field_name: Union[Unset, str] = UNSET
    match_threshold: Union[Unset, float] = UNSET
    mvalue: Union[Unset, float] = UNSET
    null_scoring: Union[Unset, bool] = UNSET
    null_weight: Union[Unset, float] = UNSET
    uvalue: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        comparator_function: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.comparator_function, Unset):
            comparator_function = self.comparator_function.to_dict()

        field_name = self.field_name
        match_threshold = self.match_threshold
        mvalue = self.mvalue
        null_scoring = self.null_scoring
        null_weight = self.null_weight
        uvalue = self.uvalue

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if comparator_function is not UNSET:
            field_dict["comparatorFunction"] = comparator_function
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if match_threshold is not UNSET:
            field_dict["matchThreshold"] = match_threshold
        if mvalue is not UNSET:
            field_dict["mvalue"] = mvalue
        if null_scoring is not UNSET:
            field_dict["nullScoring"] = null_scoring
        if null_weight is not UNSET:
            field_dict["nullWeight"] = null_weight
        if uvalue is not UNSET:
            field_dict["uvalue"] = uvalue

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.comparator_function import ComparatorFunction

        d = src_dict.copy()
        _comparator_function = d.pop("comparatorFunction", UNSET)
        comparator_function: Union[Unset, ComparatorFunction]
        if isinstance(_comparator_function, Unset):
            comparator_function = UNSET
        else:
            comparator_function = ComparatorFunction.from_dict(_comparator_function)

        field_name = d.pop("fieldName", UNSET)

        match_threshold = d.pop("matchThreshold", UNSET)

        mvalue = d.pop("mvalue", UNSET)

        null_scoring = d.pop("nullScoring", UNSET)

        null_weight = d.pop("nullWeight", UNSET)

        uvalue = d.pop("uvalue", UNSET)

        match_field = cls(
            comparator_function=comparator_function,
            field_name=field_name,
            match_threshold=match_threshold,
            mvalue=mvalue,
            null_scoring=null_scoring,
            null_weight=null_weight,
            uvalue=uvalue,
        )

        match_field.additional_properties = d
        return match_field

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
