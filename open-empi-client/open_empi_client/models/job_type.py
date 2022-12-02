from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobType")


@attr.s(auto_attribs=True)
class JobType:
    """
    Attributes:
        job_type_cd (Union[Unset, int]):
        job_type_description (Union[Unset, str]):
        job_type_name (Union[Unset, str]):
    """

    job_type_cd: Union[Unset, int] = UNSET
    job_type_description: Union[Unset, str] = UNSET
    job_type_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_type_cd = self.job_type_cd
        job_type_description = self.job_type_description
        job_type_name = self.job_type_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_type_cd is not UNSET:
            field_dict["jobTypeCd"] = job_type_cd
        if job_type_description is not UNSET:
            field_dict["jobTypeDescription"] = job_type_description
        if job_type_name is not UNSET:
            field_dict["jobTypeName"] = job_type_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_type_cd = d.pop("jobTypeCd", UNSET)

        job_type_description = d.pop("jobTypeDescription", UNSET)

        job_type_name = d.pop("jobTypeName", UNSET)

        job_type = cls(
            job_type_cd=job_type_cd,
            job_type_description=job_type_description,
            job_type_name=job_type_name,
        )

        job_type.additional_properties = d
        return job_type

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
