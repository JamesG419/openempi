from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_field import MatchField
    from ..models.vector_configuration import VectorConfiguration


T = TypeVar("T", bound="ProbabilisticMatchingConfiguration")


@attr.s(auto_attribs=True)
class ProbabilisticMatchingConfiguration:
    """
    Attributes:
        configuration_directory (Union[Unset, str]):
        convergence_error (Union[Unset, float]):
        entity_name (Union[Unset, str]):
        false_negative_probability (Union[Unset, float]):
        false_positive_probability (Union[Unset, float]):
        fields (Union[Unset, List['MatchField']]):
        initial_m_value (Union[Unset, float]):
        initial_p_value (Union[Unset, float]):
        initial_u_value (Union[Unset, float]):
        logging_by_vectors (Union[Unset, bool]):
        logging_by_vectors_fraction (Union[Unset, float]):
        logging_by_weight (Union[Unset, bool]):
        logging_by_weight_fraction (Union[Unset, float]):
        logging_by_weight_lower_bound (Union[Unset, float]):
        logging_by_weight_upper_bound (Union[Unset, float]):
        logging_destination (Union[Unset, str]):
        logging_vectors (Union[Unset, List[int]]):
        lower_bound (Union[Unset, float]):
        max_iterations (Union[Unset, int]):
        pvalue (Union[Unset, float]):
        sampling_rate (Union[Unset, float]):
        upper_bound (Union[Unset, float]):
        vector_config (Union[Unset, List['VectorConfiguration']]):
    """

    configuration_directory: Union[Unset, str] = UNSET
    convergence_error: Union[Unset, float] = UNSET
    entity_name: Union[Unset, str] = UNSET
    false_negative_probability: Union[Unset, float] = UNSET
    false_positive_probability: Union[Unset, float] = UNSET
    fields: Union[Unset, List["MatchField"]] = UNSET
    initial_m_value: Union[Unset, float] = UNSET
    initial_p_value: Union[Unset, float] = UNSET
    initial_u_value: Union[Unset, float] = UNSET
    logging_by_vectors: Union[Unset, bool] = UNSET
    logging_by_vectors_fraction: Union[Unset, float] = UNSET
    logging_by_weight: Union[Unset, bool] = UNSET
    logging_by_weight_fraction: Union[Unset, float] = UNSET
    logging_by_weight_lower_bound: Union[Unset, float] = UNSET
    logging_by_weight_upper_bound: Union[Unset, float] = UNSET
    logging_destination: Union[Unset, str] = UNSET
    logging_vectors: Union[Unset, List[int]] = UNSET
    lower_bound: Union[Unset, float] = UNSET
    max_iterations: Union[Unset, int] = UNSET
    pvalue: Union[Unset, float] = UNSET
    sampling_rate: Union[Unset, float] = UNSET
    upper_bound: Union[Unset, float] = UNSET
    vector_config: Union[Unset, List["VectorConfiguration"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configuration_directory = self.configuration_directory
        convergence_error = self.convergence_error
        entity_name = self.entity_name
        false_negative_probability = self.false_negative_probability
        false_positive_probability = self.false_positive_probability
        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        initial_m_value = self.initial_m_value
        initial_p_value = self.initial_p_value
        initial_u_value = self.initial_u_value
        logging_by_vectors = self.logging_by_vectors
        logging_by_vectors_fraction = self.logging_by_vectors_fraction
        logging_by_weight = self.logging_by_weight
        logging_by_weight_fraction = self.logging_by_weight_fraction
        logging_by_weight_lower_bound = self.logging_by_weight_lower_bound
        logging_by_weight_upper_bound = self.logging_by_weight_upper_bound
        logging_destination = self.logging_destination
        logging_vectors: Union[Unset, List[int]] = UNSET
        if not isinstance(self.logging_vectors, Unset):
            logging_vectors = self.logging_vectors

        lower_bound = self.lower_bound
        max_iterations = self.max_iterations
        pvalue = self.pvalue
        sampling_rate = self.sampling_rate
        upper_bound = self.upper_bound
        vector_config: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.vector_config, Unset):
            vector_config = []
            for vector_config_item_data in self.vector_config:
                vector_config_item = vector_config_item_data.to_dict()

                vector_config.append(vector_config_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configuration_directory is not UNSET:
            field_dict["configurationDirectory"] = configuration_directory
        if convergence_error is not UNSET:
            field_dict["convergenceError"] = convergence_error
        if entity_name is not UNSET:
            field_dict["entityName"] = entity_name
        if false_negative_probability is not UNSET:
            field_dict["falseNegativeProbability"] = false_negative_probability
        if false_positive_probability is not UNSET:
            field_dict["falsePositiveProbability"] = false_positive_probability
        if fields is not UNSET:
            field_dict["fields"] = fields
        if initial_m_value is not UNSET:
            field_dict["initialMValue"] = initial_m_value
        if initial_p_value is not UNSET:
            field_dict["initialPValue"] = initial_p_value
        if initial_u_value is not UNSET:
            field_dict["initialUValue"] = initial_u_value
        if logging_by_vectors is not UNSET:
            field_dict["loggingByVectors"] = logging_by_vectors
        if logging_by_vectors_fraction is not UNSET:
            field_dict["loggingByVectorsFraction"] = logging_by_vectors_fraction
        if logging_by_weight is not UNSET:
            field_dict["loggingByWeight"] = logging_by_weight
        if logging_by_weight_fraction is not UNSET:
            field_dict["loggingByWeightFraction"] = logging_by_weight_fraction
        if logging_by_weight_lower_bound is not UNSET:
            field_dict["loggingByWeightLowerBound"] = logging_by_weight_lower_bound
        if logging_by_weight_upper_bound is not UNSET:
            field_dict["loggingByWeightUpperBound"] = logging_by_weight_upper_bound
        if logging_destination is not UNSET:
            field_dict["loggingDestination"] = logging_destination
        if logging_vectors is not UNSET:
            field_dict["loggingVectors"] = logging_vectors
        if lower_bound is not UNSET:
            field_dict["lowerBound"] = lower_bound
        if max_iterations is not UNSET:
            field_dict["maxIterations"] = max_iterations
        if pvalue is not UNSET:
            field_dict["pvalue"] = pvalue
        if sampling_rate is not UNSET:
            field_dict["samplingRate"] = sampling_rate
        if upper_bound is not UNSET:
            field_dict["upperBound"] = upper_bound
        if vector_config is not UNSET:
            field_dict["vectorConfig"] = vector_config

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_field import MatchField
        from ..models.vector_configuration import VectorConfiguration

        d = src_dict.copy()
        configuration_directory = d.pop("configurationDirectory", UNSET)

        convergence_error = d.pop("convergenceError", UNSET)

        entity_name = d.pop("entityName", UNSET)

        false_negative_probability = d.pop("falseNegativeProbability", UNSET)

        false_positive_probability = d.pop("falsePositiveProbability", UNSET)

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = MatchField.from_dict(fields_item_data)

            fields.append(fields_item)

        initial_m_value = d.pop("initialMValue", UNSET)

        initial_p_value = d.pop("initialPValue", UNSET)

        initial_u_value = d.pop("initialUValue", UNSET)

        logging_by_vectors = d.pop("loggingByVectors", UNSET)

        logging_by_vectors_fraction = d.pop("loggingByVectorsFraction", UNSET)

        logging_by_weight = d.pop("loggingByWeight", UNSET)

        logging_by_weight_fraction = d.pop("loggingByWeightFraction", UNSET)

        logging_by_weight_lower_bound = d.pop("loggingByWeightLowerBound", UNSET)

        logging_by_weight_upper_bound = d.pop("loggingByWeightUpperBound", UNSET)

        logging_destination = d.pop("loggingDestination", UNSET)

        logging_vectors = cast(List[int], d.pop("loggingVectors", UNSET))

        lower_bound = d.pop("lowerBound", UNSET)

        max_iterations = d.pop("maxIterations", UNSET)

        pvalue = d.pop("pvalue", UNSET)

        sampling_rate = d.pop("samplingRate", UNSET)

        upper_bound = d.pop("upperBound", UNSET)

        vector_config = []
        _vector_config = d.pop("vectorConfig", UNSET)
        for vector_config_item_data in _vector_config or []:
            vector_config_item = VectorConfiguration.from_dict(vector_config_item_data)

            vector_config.append(vector_config_item)

        probabilistic_matching_configuration = cls(
            configuration_directory=configuration_directory,
            convergence_error=convergence_error,
            entity_name=entity_name,
            false_negative_probability=false_negative_probability,
            false_positive_probability=false_positive_probability,
            fields=fields,
            initial_m_value=initial_m_value,
            initial_p_value=initial_p_value,
            initial_u_value=initial_u_value,
            logging_by_vectors=logging_by_vectors,
            logging_by_vectors_fraction=logging_by_vectors_fraction,
            logging_by_weight=logging_by_weight,
            logging_by_weight_fraction=logging_by_weight_fraction,
            logging_by_weight_lower_bound=logging_by_weight_lower_bound,
            logging_by_weight_upper_bound=logging_by_weight_upper_bound,
            logging_destination=logging_destination,
            logging_vectors=logging_vectors,
            lower_bound=lower_bound,
            max_iterations=max_iterations,
            pvalue=pvalue,
            sampling_rate=sampling_rate,
            upper_bound=upper_bound,
            vector_config=vector_config,
        )

        probabilistic_matching_configuration.additional_properties = d
        return probabilistic_matching_configuration

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
