from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.blocking_round import BlockingRound


T = TypeVar("T", bound="BlockingConfiguration")


@attr.s(auto_attribs=True)
class BlockingConfiguration:
    """
    Attributes:
        blocking_rounds (Union[Unset, List['BlockingRound']]):
        entity_name (Union[Unset, str]):
        entity_version_id (Union[Unset, int]):
        maximum_block_size (Union[Unset, int]):
    """

    blocking_rounds: Union[Unset, List["BlockingRound"]] = UNSET
    entity_name: Union[Unset, str] = UNSET
    entity_version_id: Union[Unset, int] = UNSET
    maximum_block_size: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        blocking_rounds: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.blocking_rounds, Unset):
            blocking_rounds = []
            for blocking_rounds_item_data in self.blocking_rounds:
                blocking_rounds_item = blocking_rounds_item_data.to_dict()

                blocking_rounds.append(blocking_rounds_item)

        entity_name = self.entity_name
        entity_version_id = self.entity_version_id
        maximum_block_size = self.maximum_block_size

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if blocking_rounds is not UNSET:
            field_dict["blockingRounds"] = blocking_rounds
        if entity_name is not UNSET:
            field_dict["entityName"] = entity_name
        if entity_version_id is not UNSET:
            field_dict["entityVersionId"] = entity_version_id
        if maximum_block_size is not UNSET:
            field_dict["maximumBlockSize"] = maximum_block_size

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.blocking_round import BlockingRound

        d = src_dict.copy()
        blocking_rounds = []
        _blocking_rounds = d.pop("blockingRounds", UNSET)
        for blocking_rounds_item_data in _blocking_rounds or []:
            blocking_rounds_item = BlockingRound.from_dict(blocking_rounds_item_data)

            blocking_rounds.append(blocking_rounds_item)

        entity_name = d.pop("entityName", UNSET)

        entity_version_id = d.pop("entityVersionId", UNSET)

        maximum_block_size = d.pop("maximumBlockSize", UNSET)

        blocking_configuration = cls(
            blocking_rounds=blocking_rounds,
            entity_name=entity_name,
            entity_version_id=entity_version_id,
            maximum_block_size=maximum_block_size,
        )

        blocking_configuration.additional_properties = d
        return blocking_configuration

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
