from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EthnicGroup")


@attr.s(auto_attribs=True)
class EthnicGroup:
    """
    Attributes:
        enthic_group_cd (Union[Unset, int]):
        enthic_group_code (Union[Unset, str]):
        enthnic_group_description (Union[Unset, str]):
        enthic_group_name (Union[Unset, str]):
    """

    enthic_group_cd: Union[Unset, int] = UNSET
    enthic_group_code: Union[Unset, str] = UNSET
    enthnic_group_description: Union[Unset, str] = UNSET
    enthic_group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        enthic_group_cd = self.enthic_group_cd
        enthic_group_code = self.enthic_group_code
        enthnic_group_description = self.enthnic_group_description
        enthic_group_name = self.enthic_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enthic_group_cd is not UNSET:
            field_dict["enthicGroupCd"] = enthic_group_cd
        if enthic_group_code is not UNSET:
            field_dict["enthicGroupCode"] = enthic_group_code
        if enthnic_group_description is not UNSET:
            field_dict["enthnicGroupDescription"] = enthnic_group_description
        if enthic_group_name is not UNSET:
            field_dict["enthicGroupName"] = enthic_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        enthic_group_cd = d.pop("enthicGroupCd", UNSET)

        enthic_group_code = d.pop("enthicGroupCode", UNSET)

        enthnic_group_description = d.pop("enthnicGroupDescription", UNSET)

        enthic_group_name = d.pop("enthicGroupName", UNSET)

        ethnic_group = cls(
            enthic_group_cd=enthic_group_cd,
            enthic_group_code=enthic_group_code,
            enthnic_group_description=enthnic_group_description,
            enthic_group_name=enthic_group_name,
        )

        ethnic_group.additional_properties = d
        return ethnic_group

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
