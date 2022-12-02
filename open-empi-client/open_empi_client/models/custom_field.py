from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field_configuration_parameters import CustomFieldConfigurationParameters


T = TypeVar("T", bound="CustomField")


@attr.s(auto_attribs=True)
class CustomField:
    """
    Attributes:
        configuration_parameters (Union[Unset, CustomFieldConfigurationParameters]):
        custom_field_id (Union[Unset, int]):
        entity_name (Union[Unset, str]):
        field_name (Union[Unset, str]):
        order_seq (Union[Unset, int]):
        source_field_name (Union[Unset, str]):
        transformation_function_name (Union[Unset, str]):
    """

    configuration_parameters: Union[Unset, "CustomFieldConfigurationParameters"] = UNSET
    custom_field_id: Union[Unset, int] = UNSET
    entity_name: Union[Unset, str] = UNSET
    field_name: Union[Unset, str] = UNSET
    order_seq: Union[Unset, int] = UNSET
    source_field_name: Union[Unset, str] = UNSET
    transformation_function_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configuration_parameters: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.configuration_parameters, Unset):
            configuration_parameters = self.configuration_parameters.to_dict()

        custom_field_id = self.custom_field_id
        entity_name = self.entity_name
        field_name = self.field_name
        order_seq = self.order_seq
        source_field_name = self.source_field_name
        transformation_function_name = self.transformation_function_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_parameters is not UNSET:
            field_dict["configurationParameters"] = configuration_parameters
        if custom_field_id is not UNSET:
            field_dict["customFieldId"] = custom_field_id
        if entity_name is not UNSET:
            field_dict["entityName"] = entity_name
        if field_name is not UNSET:
            field_dict["fieldName"] = field_name
        if order_seq is not UNSET:
            field_dict["orderSeq"] = order_seq
        if source_field_name is not UNSET:
            field_dict["sourceFieldName"] = source_field_name
        if transformation_function_name is not UNSET:
            field_dict["transformationFunctionName"] = transformation_function_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.custom_field_configuration_parameters import CustomFieldConfigurationParameters

        d = src_dict.copy()
        _configuration_parameters = d.pop("configurationParameters", UNSET)
        configuration_parameters: Union[Unset, CustomFieldConfigurationParameters]
        if isinstance(_configuration_parameters, Unset):
            configuration_parameters = UNSET
        else:
            configuration_parameters = CustomFieldConfigurationParameters.from_dict(_configuration_parameters)

        custom_field_id = d.pop("customFieldId", UNSET)

        entity_name = d.pop("entityName", UNSET)

        field_name = d.pop("fieldName", UNSET)

        order_seq = d.pop("orderSeq", UNSET)

        source_field_name = d.pop("sourceFieldName", UNSET)

        transformation_function_name = d.pop("transformationFunctionName", UNSET)

        custom_field = cls(
            configuration_parameters=configuration_parameters,
            custom_field_id=custom_field_id,
            entity_name=entity_name,
            field_name=field_name,
            order_seq=order_seq,
            source_field_name=source_field_name,
            transformation_function_name=transformation_function_name,
        )

        custom_field.additional_properties = d
        return custom_field

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
