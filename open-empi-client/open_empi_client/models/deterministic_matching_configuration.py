from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.match_rule import MatchRule


T = TypeVar("T", bound="DeterministicMatchingConfiguration")


@attr.s(auto_attribs=True)
class DeterministicMatchingConfiguration:
    """
    Attributes:
        entity_name (Union[Unset, str]):
        rules (Union[Unset, List['MatchRule']]):
    """

    entity_name: Union[Unset, str] = UNSET
    rules: Union[Unset, List["MatchRule"]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entity_name = self.entity_name
        rules: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()

                rules.append(rules_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if entity_name is not UNSET:
            field_dict["entityName"] = entity_name
        if rules is not UNSET:
            field_dict["rules"] = rules

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.match_rule import MatchRule

        d = src_dict.copy()
        entity_name = d.pop("entityName", UNSET)

        rules = []
        _rules = d.pop("rules", UNSET)
        for rules_item_data in _rules or []:
            rules_item = MatchRule.from_dict(rules_item_data)

            rules.append(rules_item)

        deterministic_matching_configuration = cls(
            entity_name=entity_name,
            rules=rules,
        )

        deterministic_matching_configuration.additional_properties = d
        return deterministic_matching_configuration

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
