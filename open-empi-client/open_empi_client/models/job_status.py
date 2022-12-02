from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="JobStatus")


@attr.s(auto_attribs=True)
class JobStatus:
    """
    Attributes:
        job_status_cd (Union[Unset, int]):
        job_status_description (Union[Unset, str]):
        job_status_name (Union[Unset, str]):
    """

    job_status_cd: Union[Unset, int] = UNSET
    job_status_description: Union[Unset, str] = UNSET
    job_status_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        job_status_cd = self.job_status_cd
        job_status_description = self.job_status_description
        job_status_name = self.job_status_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if job_status_cd is not UNSET:
            field_dict["jobStatusCd"] = job_status_cd
        if job_status_description is not UNSET:
            field_dict["jobStatusDescription"] = job_status_description
        if job_status_name is not UNSET:
            field_dict["jobStatusName"] = job_status_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        job_status_cd = d.pop("jobStatusCd", UNSET)

        job_status_description = d.pop("jobStatusDescription", UNSET)

        job_status_name = d.pop("jobStatusName", UNSET)

        job_status = cls(
            job_status_cd=job_status_cd,
            job_status_description=job_status_description,
            job_status_name=job_status_name,
        )

        job_status.additional_properties = d
        return job_status

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
