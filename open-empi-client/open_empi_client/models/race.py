from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Race")


@attr.s(auto_attribs=True)
class Race:
    """
    Attributes:
        race_cd (Union[Unset, int]):
        race_code (Union[Unset, str]):
        race_description (Union[Unset, str]):
        race_name (Union[Unset, str]):
    """

    race_cd: Union[Unset, int] = UNSET
    race_code: Union[Unset, str] = UNSET
    race_description: Union[Unset, str] = UNSET
    race_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        race_cd = self.race_cd
        race_code = self.race_code
        race_description = self.race_description
        race_name = self.race_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if race_cd is not UNSET:
            field_dict["raceCd"] = race_cd
        if race_code is not UNSET:
            field_dict["raceCode"] = race_code
        if race_description is not UNSET:
            field_dict["raceDescription"] = race_description
        if race_name is not UNSET:
            field_dict["raceName"] = race_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        race_cd = d.pop("raceCd", UNSET)

        race_code = d.pop("raceCode", UNSET)

        race_description = d.pop("raceDescription", UNSET)

        race_name = d.pop("raceName", UNSET)

        race = cls(
            race_cd=race_cd,
            race_code=race_code,
            race_description=race_description,
            race_name=race_name,
        )

        race.additional_properties = d
        return race

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
