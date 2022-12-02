from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="DataProfileAttribute")


@attr.s(auto_attribs=True)
class DataProfileAttribute:
    """
    Attributes:
        attribute_id (Union[Unset, int]):
        attribute_name (Union[Unset, str]):
        average_length (Union[Unset, float]):
        average_token_frequency (Union[Unset, float]):
        average_value (Union[Unset, float]):
        blocking_pairs (Union[Unset, int]):
        datatype_id (Union[Unset, int]):
        distinct_count (Union[Unset, int]):
        duplicate_count (Union[Unset, int]):
        entropy (Union[Unset, float]):
        getu_value (Union[Unset, float]):
        maximum_entropy (Union[Unset, float]):
        maximum_length (Union[Unset, int]):
        maximum_value (Union[Unset, float]):
        minimum_length (Union[Unset, int]):
        minumum_value (Union[Unset, float]):
        null_count (Union[Unset, int]):
        null_rate (Union[Unset, float]):
        row_count (Union[Unset, int]):
        standard_deviation (Union[Unset, float]):
        unique_count (Union[Unset, int]):
        variance (Union[Unset, float]):
    """

    attribute_id: Union[Unset, int] = UNSET
    attribute_name: Union[Unset, str] = UNSET
    average_length: Union[Unset, float] = UNSET
    average_token_frequency: Union[Unset, float] = UNSET
    average_value: Union[Unset, float] = UNSET
    blocking_pairs: Union[Unset, int] = UNSET
    datatype_id: Union[Unset, int] = UNSET
    distinct_count: Union[Unset, int] = UNSET
    duplicate_count: Union[Unset, int] = UNSET
    entropy: Union[Unset, float] = UNSET
    getu_value: Union[Unset, float] = UNSET
    maximum_entropy: Union[Unset, float] = UNSET
    maximum_length: Union[Unset, int] = UNSET
    maximum_value: Union[Unset, float] = UNSET
    minimum_length: Union[Unset, int] = UNSET
    minumum_value: Union[Unset, float] = UNSET
    null_count: Union[Unset, int] = UNSET
    null_rate: Union[Unset, float] = UNSET
    row_count: Union[Unset, int] = UNSET
    standard_deviation: Union[Unset, float] = UNSET
    unique_count: Union[Unset, int] = UNSET
    variance: Union[Unset, float] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        attribute_id = self.attribute_id
        attribute_name = self.attribute_name
        average_length = self.average_length
        average_token_frequency = self.average_token_frequency
        average_value = self.average_value
        blocking_pairs = self.blocking_pairs
        datatype_id = self.datatype_id
        distinct_count = self.distinct_count
        duplicate_count = self.duplicate_count
        entropy = self.entropy
        getu_value = self.getu_value
        maximum_entropy = self.maximum_entropy
        maximum_length = self.maximum_length
        maximum_value = self.maximum_value
        minimum_length = self.minimum_length
        minumum_value = self.minumum_value
        null_count = self.null_count
        null_rate = self.null_rate
        row_count = self.row_count
        standard_deviation = self.standard_deviation
        unique_count = self.unique_count
        variance = self.variance

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if attribute_id is not UNSET:
            field_dict["attributeId"] = attribute_id
        if attribute_name is not UNSET:
            field_dict["attributeName"] = attribute_name
        if average_length is not UNSET:
            field_dict["averageLength"] = average_length
        if average_token_frequency is not UNSET:
            field_dict["averageTokenFrequency"] = average_token_frequency
        if average_value is not UNSET:
            field_dict["averageValue"] = average_value
        if blocking_pairs is not UNSET:
            field_dict["blockingPairs"] = blocking_pairs
        if datatype_id is not UNSET:
            field_dict["datatypeId"] = datatype_id
        if distinct_count is not UNSET:
            field_dict["distinctCount"] = distinct_count
        if duplicate_count is not UNSET:
            field_dict["duplicateCount"] = duplicate_count
        if entropy is not UNSET:
            field_dict["entropy"] = entropy
        if getu_value is not UNSET:
            field_dict["getuValue"] = getu_value
        if maximum_entropy is not UNSET:
            field_dict["maximumEntropy"] = maximum_entropy
        if maximum_length is not UNSET:
            field_dict["maximumLength"] = maximum_length
        if maximum_value is not UNSET:
            field_dict["maximumValue"] = maximum_value
        if minimum_length is not UNSET:
            field_dict["minimumLength"] = minimum_length
        if minumum_value is not UNSET:
            field_dict["minumumValue"] = minumum_value
        if null_count is not UNSET:
            field_dict["nullCount"] = null_count
        if null_rate is not UNSET:
            field_dict["nullRate"] = null_rate
        if row_count is not UNSET:
            field_dict["rowCount"] = row_count
        if standard_deviation is not UNSET:
            field_dict["standardDeviation"] = standard_deviation
        if unique_count is not UNSET:
            field_dict["uniqueCount"] = unique_count
        if variance is not UNSET:
            field_dict["variance"] = variance

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        attribute_id = d.pop("attributeId", UNSET)

        attribute_name = d.pop("attributeName", UNSET)

        average_length = d.pop("averageLength", UNSET)

        average_token_frequency = d.pop("averageTokenFrequency", UNSET)

        average_value = d.pop("averageValue", UNSET)

        blocking_pairs = d.pop("blockingPairs", UNSET)

        datatype_id = d.pop("datatypeId", UNSET)

        distinct_count = d.pop("distinctCount", UNSET)

        duplicate_count = d.pop("duplicateCount", UNSET)

        entropy = d.pop("entropy", UNSET)

        getu_value = d.pop("getuValue", UNSET)

        maximum_entropy = d.pop("maximumEntropy", UNSET)

        maximum_length = d.pop("maximumLength", UNSET)

        maximum_value = d.pop("maximumValue", UNSET)

        minimum_length = d.pop("minimumLength", UNSET)

        minumum_value = d.pop("minumumValue", UNSET)

        null_count = d.pop("nullCount", UNSET)

        null_rate = d.pop("nullRate", UNSET)

        row_count = d.pop("rowCount", UNSET)

        standard_deviation = d.pop("standardDeviation", UNSET)

        unique_count = d.pop("uniqueCount", UNSET)

        variance = d.pop("variance", UNSET)

        data_profile_attribute = cls(
            attribute_id=attribute_id,
            attribute_name=attribute_name,
            average_length=average_length,
            average_token_frequency=average_token_frequency,
            average_value=average_value,
            blocking_pairs=blocking_pairs,
            datatype_id=datatype_id,
            distinct_count=distinct_count,
            duplicate_count=duplicate_count,
            entropy=entropy,
            getu_value=getu_value,
            maximum_entropy=maximum_entropy,
            maximum_length=maximum_length,
            maximum_value=maximum_value,
            minimum_length=minimum_length,
            minumum_value=minumum_value,
            null_count=null_count,
            null_rate=null_rate,
            row_count=row_count,
            standard_deviation=standard_deviation,
            unique_count=unique_count,
            variance=variance,
        )

        data_profile_attribute.additional_properties = d
        return data_profile_attribute

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
