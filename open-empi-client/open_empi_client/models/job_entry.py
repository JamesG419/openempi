from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.job_status import JobStatus
    from ..models.job_type import JobType


T = TypeVar("T", bound="JobEntry")


@attr.s(auto_attribs=True)
class JobEntry:
    """
    Attributes:
        date_completed (Union[Unset, str]):
        date_created (Union[Unset, str]):
        date_started (Union[Unset, str]):
        items_errored (Union[Unset, int]):
        items_processed (Union[Unset, int]):
        items_successful (Union[Unset, int]):
        job_description (Union[Unset, str]):
        job_entry_id (Union[Unset, int]):
        job_parameters (Union[Unset, str]):
        job_status (Union[Unset, JobStatus]):
        job_type (Union[Unset, JobType]):
    """

    date_completed: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_started: Union[Unset, str] = UNSET
    items_errored: Union[Unset, int] = UNSET
    items_processed: Union[Unset, int] = UNSET
    items_successful: Union[Unset, int] = UNSET
    job_description: Union[Unset, str] = UNSET
    job_entry_id: Union[Unset, int] = UNSET
    job_parameters: Union[Unset, str] = UNSET
    job_status: Union[Unset, "JobStatus"] = UNSET
    job_type: Union[Unset, "JobType"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        date_completed = self.date_completed
        date_created = self.date_created
        date_started = self.date_started
        items_errored = self.items_errored
        items_processed = self.items_processed
        items_successful = self.items_successful
        job_description = self.job_description
        job_entry_id = self.job_entry_id
        job_parameters = self.job_parameters
        job_status: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_status, Unset):
            job_status = self.job_status.to_dict()

        job_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.job_type, Unset):
            job_type = self.job_type.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if date_completed is not UNSET:
            field_dict["dateCompleted"] = date_completed
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_started is not UNSET:
            field_dict["dateStarted"] = date_started
        if items_errored is not UNSET:
            field_dict["itemsErrored"] = items_errored
        if items_processed is not UNSET:
            field_dict["itemsProcessed"] = items_processed
        if items_successful is not UNSET:
            field_dict["itemsSuccessful"] = items_successful
        if job_description is not UNSET:
            field_dict["jobDescription"] = job_description
        if job_entry_id is not UNSET:
            field_dict["jobEntryId"] = job_entry_id
        if job_parameters is not UNSET:
            field_dict["jobParameters"] = job_parameters
        if job_status is not UNSET:
            field_dict["jobStatus"] = job_status
        if job_type is not UNSET:
            field_dict["jobType"] = job_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.job_status import JobStatus
        from ..models.job_type import JobType

        d = src_dict.copy()
        date_completed = d.pop("dateCompleted", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        date_started = d.pop("dateStarted", UNSET)

        items_errored = d.pop("itemsErrored", UNSET)

        items_processed = d.pop("itemsProcessed", UNSET)

        items_successful = d.pop("itemsSuccessful", UNSET)

        job_description = d.pop("jobDescription", UNSET)

        job_entry_id = d.pop("jobEntryId", UNSET)

        job_parameters = d.pop("jobParameters", UNSET)

        _job_status = d.pop("jobStatus", UNSET)
        job_status: Union[Unset, JobStatus]
        if isinstance(_job_status, Unset):
            job_status = UNSET
        else:
            job_status = JobStatus.from_dict(_job_status)

        _job_type = d.pop("jobType", UNSET)
        job_type: Union[Unset, JobType]
        if isinstance(_job_type, Unset):
            job_type = UNSET
        else:
            job_type = JobType.from_dict(_job_type)

        job_entry = cls(
            date_completed=date_completed,
            date_created=date_created,
            date_started=date_started,
            items_errored=items_errored,
            items_processed=items_processed,
            items_successful=items_successful,
            job_description=job_description,
            job_entry_id=job_entry_id,
            job_parameters=job_parameters,
            job_status=job_status,
            job_type=job_type,
        )

        job_entry.additional_properties = d
        return job_entry

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
