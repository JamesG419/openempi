import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_type import AddressType
    from ..models.ethnic_group import EthnicGroup
    from ..models.gender import Gender
    from ..models.identifier_domain import IdentifierDomain
    from ..models.language import Language
    from ..models.name_type import NameType
    from ..models.nationality import Nationality
    from ..models.person_identifier import PersonIdentifier
    from ..models.phone_type import PhoneType
    from ..models.race import Race
    from ..models.religion import Religion
    from ..models.user import User


T = TypeVar("T", bound="Person")


@attr.s(auto_attribs=True)
class Person:
    """
    Attributes:
        account (Union[Unset, str]):
        account_identifier_domain (Union[Unset, IdentifierDomain]):
        address1 (Union[Unset, str]):
        adress2 (Union[Unset, str]):
        address_type (Union[Unset, AddressType]):
        birth_order (Union[Unset, int]):
        birth_place (Union[Unset, str]):
        cell (Union[Unset, str]):
        cell_id (Union[Unset, str]):
        city (Union[Unset, str]):
        country (Union[Unset, str]):
        country_code (Union[Unset, str]):
        custom1 (Union[Unset, str]):
        custom10 (Union[Unset, str]):
        custom11 (Union[Unset, str]):
        custom12 (Union[Unset, str]):
        custom13 (Union[Unset, str]):
        custom14 (Union[Unset, str]):
        custom15 (Union[Unset, str]):
        custom16 (Union[Unset, str]):
        custom17 (Union[Unset, str]):
        custom18 (Union[Unset, str]):
        custom19 (Union[Unset, str]):
        custom2 (Union[Unset, str]):
        custom20 (Union[Unset, str]):
        custom3 (Union[Unset, str]):
        custom4 (Union[Unset, str]):
        custom5 (Union[Unset, str]):
        custom6 (Union[Unset, str]):
        custom7 (Union[Unset, str]):
        custom8 (Union[Unset, str]):
        custom9 (Union[Unset, str]):
        date_changed (Union[Unset, datetime.datetime]):
        date_created (Union[Unset, datetime.datetime]):
        date_of_birth (Union[Unset, datetime.datetime]):
        date_voided (Union[Unset, datetime.datetime]):
        death_ind (Union[Unset, str]):
        death_time (Union[Unset, datetime.datetime]):
        degree (Union[Unset, str]):
        district (Union[Unset, str]):
        district_id (Union[Unset, str]):
        email (Union[Unset, str]):
        ethnic_group (Union[Unset, EthnicGroup]):
        family_name (Union[Unset, str]):
        family_name_2 (Union[Unset, str]):
        father_name (Union[Unset, str]):
        gender (Union[Unset, Gender]):
        given_name (Union[Unset, str]):
        group_number (Union[Unset, str]):
        language (Union[Unset, Language]):
        marital_status_code (Union[Unset, str]):
        middle_name (Union[Unset, str]):
        mother_name (Union[Unset, str]):
        mothers_maiden_name (Union[Unset, str]):
        multiple_birth_ind (Union[Unset, str]):
        name_type (Union[Unset, NameType]):
        nationality (Union[Unset, Nationality]):
        person_id (Union[Unset, int]):
        person_identifiers (Union[Unset, List['PersonIdentifier']]):
        phone_area_code (Union[Unset, str]):
        phone_country_code (Union[Unset, str]):
        phone_ext (Union[Unset, str]):
        phone_number (Union[Unset, str]):
        phone_type (Union[Unset, PhoneType]):
        postal_code (Union[Unset, str]):
        prefix (Union[Unset, str]):
        province (Union[Unset, str]):
        race (Union[Unset, Race]):
        religion (Union[Unset, Religion]):
        sector (Union[Unset, str]):
        sector_id (Union[Unset, str]):
        ssn (Union[Unset, str]):
        state (Union[Unset, str]):
        suffix (Union[Unset, str]):
        user_changed_by (Union[Unset, User]):
        user_created_by (Union[Unset, User]):
        user_voided_by (Union[Unset, User]):
        village (Union[Unset, str]):
        village_id (Union[Unset, str]):
    """

    account: Union[Unset, str] = UNSET
    account_identifier_domain: Union[Unset, "IdentifierDomain"] = UNSET
    address1: Union[Unset, str] = UNSET
    adress2: Union[Unset, str] = UNSET
    address_type: Union[Unset, "AddressType"] = UNSET
    birth_order: Union[Unset, int] = UNSET
    birth_place: Union[Unset, str] = UNSET
    cell: Union[Unset, str] = UNSET
    cell_id: Union[Unset, str] = UNSET
    city: Union[Unset, str] = UNSET
    country: Union[Unset, str] = UNSET
    country_code: Union[Unset, str] = UNSET
    custom1: Union[Unset, str] = UNSET
    custom10: Union[Unset, str] = UNSET
    custom11: Union[Unset, str] = UNSET
    custom12: Union[Unset, str] = UNSET
    custom13: Union[Unset, str] = UNSET
    custom14: Union[Unset, str] = UNSET
    custom15: Union[Unset, str] = UNSET
    custom16: Union[Unset, str] = UNSET
    custom17: Union[Unset, str] = UNSET
    custom18: Union[Unset, str] = UNSET
    custom19: Union[Unset, str] = UNSET
    custom2: Union[Unset, str] = UNSET
    custom20: Union[Unset, str] = UNSET
    custom3: Union[Unset, str] = UNSET
    custom4: Union[Unset, str] = UNSET
    custom5: Union[Unset, str] = UNSET
    custom6: Union[Unset, str] = UNSET
    custom7: Union[Unset, str] = UNSET
    custom8: Union[Unset, str] = UNSET
    custom9: Union[Unset, str] = UNSET
    date_changed: Union[Unset, datetime.datetime] = UNSET
    date_created: Union[Unset, datetime.datetime] = UNSET
    date_of_birth: Union[Unset, datetime.datetime] = UNSET
    date_voided: Union[Unset, datetime.datetime] = UNSET
    death_ind: Union[Unset, str] = UNSET
    death_time: Union[Unset, datetime.datetime] = UNSET
    degree: Union[Unset, str] = UNSET
    district: Union[Unset, str] = UNSET
    district_id: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    ethnic_group: Union[Unset, "EthnicGroup"] = UNSET
    family_name: Union[Unset, str] = UNSET
    family_name_2: Union[Unset, str] = UNSET
    father_name: Union[Unset, str] = UNSET
    gender: Union[Unset, "Gender"] = UNSET
    given_name: Union[Unset, str] = UNSET
    group_number: Union[Unset, str] = UNSET
    language: Union[Unset, "Language"] = UNSET
    marital_status_code: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    mother_name: Union[Unset, str] = UNSET
    mothers_maiden_name: Union[Unset, str] = UNSET
    multiple_birth_ind: Union[Unset, str] = UNSET
    name_type: Union[Unset, "NameType"] = UNSET
    nationality: Union[Unset, "Nationality"] = UNSET
    person_id: Union[Unset, int] = UNSET
    person_identifiers: Union[Unset, List["PersonIdentifier"]] = UNSET
    phone_area_code: Union[Unset, str] = UNSET
    phone_country_code: Union[Unset, str] = UNSET
    phone_ext: Union[Unset, str] = UNSET
    phone_number: Union[Unset, str] = UNSET
    phone_type: Union[Unset, "PhoneType"] = UNSET
    postal_code: Union[Unset, str] = UNSET
    prefix: Union[Unset, str] = UNSET
    province: Union[Unset, str] = UNSET
    race: Union[Unset, "Race"] = UNSET
    religion: Union[Unset, "Religion"] = UNSET
    sector: Union[Unset, str] = UNSET
    sector_id: Union[Unset, str] = UNSET
    ssn: Union[Unset, str] = UNSET
    state: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    user_changed_by: Union[Unset, "User"] = UNSET
    user_created_by: Union[Unset, "User"] = UNSET
    user_voided_by: Union[Unset, "User"] = UNSET
    village: Union[Unset, str] = UNSET
    village_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        account = self.account
        account_identifier_domain: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.account_identifier_domain, Unset):
            account_identifier_domain = self.account_identifier_domain.to_dict()

        address1 = self.address1
        adress2 = self.adress2
        address_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.address_type, Unset):
            address_type = self.address_type.to_dict()

        birth_order = self.birth_order
        birth_place = self.birth_place
        cell = self.cell
        cell_id = self.cell_id
        city = self.city
        country = self.country
        country_code = self.country_code
        custom1 = self.custom1
        custom10 = self.custom10
        custom11 = self.custom11
        custom12 = self.custom12
        custom13 = self.custom13
        custom14 = self.custom14
        custom15 = self.custom15
        custom16 = self.custom16
        custom17 = self.custom17
        custom18 = self.custom18
        custom19 = self.custom19
        custom2 = self.custom2
        custom20 = self.custom20
        custom3 = self.custom3
        custom4 = self.custom4
        custom5 = self.custom5
        custom6 = self.custom6
        custom7 = self.custom7
        custom8 = self.custom8
        custom9 = self.custom9
        date_changed: Union[Unset, str] = UNSET
        if not isinstance(self.date_changed, Unset):
            date_changed = self.date_changed.isoformat()

        date_created: Union[Unset, str] = UNSET
        if not isinstance(self.date_created, Unset):
            date_created = self.date_created.isoformat()

        date_of_birth: Union[Unset, str] = UNSET
        if not isinstance(self.date_of_birth, Unset):
            date_of_birth = self.date_of_birth.isoformat()

        date_voided: Union[Unset, str] = UNSET
        if not isinstance(self.date_voided, Unset):
            date_voided = self.date_voided.isoformat()

        death_ind = self.death_ind
        death_time: Union[Unset, str] = UNSET
        if not isinstance(self.death_time, Unset):
            death_time = self.death_time.isoformat()

        degree = self.degree
        district = self.district
        district_id = self.district_id
        email = self.email
        ethnic_group: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.ethnic_group, Unset):
            ethnic_group = self.ethnic_group.to_dict()

        family_name = self.family_name
        family_name_2 = self.family_name_2
        father_name = self.father_name
        gender: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.gender, Unset):
            gender = self.gender.to_dict()

        given_name = self.given_name
        group_number = self.group_number
        language: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.language, Unset):
            language = self.language.to_dict()

        marital_status_code = self.marital_status_code
        middle_name = self.middle_name
        mother_name = self.mother_name
        mothers_maiden_name = self.mothers_maiden_name
        multiple_birth_ind = self.multiple_birth_ind
        name_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.name_type, Unset):
            name_type = self.name_type.to_dict()

        nationality: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.nationality, Unset):
            nationality = self.nationality.to_dict()

        person_id = self.person_id
        person_identifiers: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.person_identifiers, Unset):
            person_identifiers = []
            for person_identifiers_item_data in self.person_identifiers:
                person_identifiers_item = person_identifiers_item_data.to_dict()

                person_identifiers.append(person_identifiers_item)

        phone_area_code = self.phone_area_code
        phone_country_code = self.phone_country_code
        phone_ext = self.phone_ext
        phone_number = self.phone_number
        phone_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phone_type, Unset):
            phone_type = self.phone_type.to_dict()

        postal_code = self.postal_code
        prefix = self.prefix
        province = self.province
        race: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.race, Unset):
            race = self.race.to_dict()

        religion: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.religion, Unset):
            religion = self.religion.to_dict()

        sector = self.sector
        sector_id = self.sector_id
        ssn = self.ssn
        state = self.state
        suffix = self.suffix
        user_changed_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_changed_by, Unset):
            user_changed_by = self.user_changed_by.to_dict()

        user_created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_created_by, Unset):
            user_created_by = self.user_created_by.to_dict()

        user_voided_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.user_voided_by, Unset):
            user_voided_by = self.user_voided_by.to_dict()

        village = self.village
        village_id = self.village_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account is not UNSET:
            field_dict["account"] = account
        if account_identifier_domain is not UNSET:
            field_dict["accountIdentifierDomain"] = account_identifier_domain
        if address1 is not UNSET:
            field_dict["address1"] = address1
        if adress2 is not UNSET:
            field_dict["adress2"] = adress2
        if address_type is not UNSET:
            field_dict["addressType"] = address_type
        if birth_order is not UNSET:
            field_dict["birthOrder"] = birth_order
        if birth_place is not UNSET:
            field_dict["birthPlace"] = birth_place
        if cell is not UNSET:
            field_dict["cell"] = cell
        if cell_id is not UNSET:
            field_dict["cellId"] = cell_id
        if city is not UNSET:
            field_dict["city"] = city
        if country is not UNSET:
            field_dict["country"] = country
        if country_code is not UNSET:
            field_dict["countryCode"] = country_code
        if custom1 is not UNSET:
            field_dict["custom1"] = custom1
        if custom10 is not UNSET:
            field_dict["custom10"] = custom10
        if custom11 is not UNSET:
            field_dict["custom11"] = custom11
        if custom12 is not UNSET:
            field_dict["custom12"] = custom12
        if custom13 is not UNSET:
            field_dict["custom13"] = custom13
        if custom14 is not UNSET:
            field_dict["custom14"] = custom14
        if custom15 is not UNSET:
            field_dict["custom15"] = custom15
        if custom16 is not UNSET:
            field_dict["custom16"] = custom16
        if custom17 is not UNSET:
            field_dict["custom17"] = custom17
        if custom18 is not UNSET:
            field_dict["custom18"] = custom18
        if custom19 is not UNSET:
            field_dict["custom19"] = custom19
        if custom2 is not UNSET:
            field_dict["custom2"] = custom2
        if custom20 is not UNSET:
            field_dict["custom20"] = custom20
        if custom3 is not UNSET:
            field_dict["custom3"] = custom3
        if custom4 is not UNSET:
            field_dict["custom4"] = custom4
        if custom5 is not UNSET:
            field_dict["custom5"] = custom5
        if custom6 is not UNSET:
            field_dict["custom6"] = custom6
        if custom7 is not UNSET:
            field_dict["custom7"] = custom7
        if custom8 is not UNSET:
            field_dict["custom8"] = custom8
        if custom9 is not UNSET:
            field_dict["custom9"] = custom9
        if date_changed is not UNSET:
            field_dict["dateChanged"] = date_changed
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if date_voided is not UNSET:
            field_dict["dateVoided"] = date_voided
        if death_ind is not UNSET:
            field_dict["deathInd"] = death_ind
        if death_time is not UNSET:
            field_dict["deathTime"] = death_time
        if degree is not UNSET:
            field_dict["degree"] = degree
        if district is not UNSET:
            field_dict["district"] = district
        if district_id is not UNSET:
            field_dict["districtId"] = district_id
        if email is not UNSET:
            field_dict["email"] = email
        if ethnic_group is not UNSET:
            field_dict["ethnicGroup"] = ethnic_group
        if family_name is not UNSET:
            field_dict["familyName"] = family_name
        if family_name_2 is not UNSET:
            field_dict["familyName2"] = family_name_2
        if father_name is not UNSET:
            field_dict["fatherName"] = father_name
        if gender is not UNSET:
            field_dict["gender"] = gender
        if given_name is not UNSET:
            field_dict["givenName"] = given_name
        if group_number is not UNSET:
            field_dict["groupNumber"] = group_number
        if language is not UNSET:
            field_dict["language"] = language
        if marital_status_code is not UNSET:
            field_dict["maritalStatusCode"] = marital_status_code
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if mother_name is not UNSET:
            field_dict["motherName"] = mother_name
        if mothers_maiden_name is not UNSET:
            field_dict["mothersMaidenName"] = mothers_maiden_name
        if multiple_birth_ind is not UNSET:
            field_dict["multipleBirthInd"] = multiple_birth_ind
        if name_type is not UNSET:
            field_dict["nameType"] = name_type
        if nationality is not UNSET:
            field_dict["nationality"] = nationality
        if person_id is not UNSET:
            field_dict["personId"] = person_id
        if person_identifiers is not UNSET:
            field_dict["personIdentifiers"] = person_identifiers
        if phone_area_code is not UNSET:
            field_dict["phoneAreaCode"] = phone_area_code
        if phone_country_code is not UNSET:
            field_dict["phoneCountryCode"] = phone_country_code
        if phone_ext is not UNSET:
            field_dict["phoneExt"] = phone_ext
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if phone_type is not UNSET:
            field_dict["PhoneType"] = phone_type
        if postal_code is not UNSET:
            field_dict["postalCode"] = postal_code
        if prefix is not UNSET:
            field_dict["prefix"] = prefix
        if province is not UNSET:
            field_dict["province"] = province
        if race is not UNSET:
            field_dict["race"] = race
        if religion is not UNSET:
            field_dict["religion"] = religion
        if sector is not UNSET:
            field_dict["sector"] = sector
        if sector_id is not UNSET:
            field_dict["sectorId"] = sector_id
        if ssn is not UNSET:
            field_dict["ssn"] = ssn
        if state is not UNSET:
            field_dict["state"] = state
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if user_changed_by is not UNSET:
            field_dict["userChangedBy"] = user_changed_by
        if user_created_by is not UNSET:
            field_dict["userCreatedBy"] = user_created_by
        if user_voided_by is not UNSET:
            field_dict["userVoidedBy"] = user_voided_by
        if village is not UNSET:
            field_dict["village"] = village
        if village_id is not UNSET:
            field_dict["villageId"] = village_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.address_type import AddressType
        from ..models.ethnic_group import EthnicGroup
        from ..models.gender import Gender
        from ..models.identifier_domain import IdentifierDomain
        from ..models.language import Language
        from ..models.name_type import NameType
        from ..models.nationality import Nationality
        from ..models.person_identifier import PersonIdentifier
        from ..models.phone_type import PhoneType
        from ..models.race import Race
        from ..models.religion import Religion
        from ..models.user import User

        d = src_dict.copy()
        account = d.pop("account", UNSET)

        _account_identifier_domain = d.pop("accountIdentifierDomain", UNSET)
        account_identifier_domain: Union[Unset, IdentifierDomain]
        if isinstance(_account_identifier_domain, Unset):
            account_identifier_domain = UNSET
        else:
            account_identifier_domain = IdentifierDomain.from_dict(_account_identifier_domain)

        address1 = d.pop("address1", UNSET)

        adress2 = d.pop("adress2", UNSET)

        _address_type = d.pop("addressType", UNSET)
        address_type: Union[Unset, AddressType]
        if isinstance(_address_type, Unset):
            address_type = UNSET
        else:
            address_type = AddressType.from_dict(_address_type)

        birth_order = d.pop("birthOrder", UNSET)

        birth_place = d.pop("birthPlace", UNSET)

        cell = d.pop("cell", UNSET)

        cell_id = d.pop("cellId", UNSET)

        city = d.pop("city", UNSET)

        country = d.pop("country", UNSET)

        country_code = d.pop("countryCode", UNSET)

        custom1 = d.pop("custom1", UNSET)

        custom10 = d.pop("custom10", UNSET)

        custom11 = d.pop("custom11", UNSET)

        custom12 = d.pop("custom12", UNSET)

        custom13 = d.pop("custom13", UNSET)

        custom14 = d.pop("custom14", UNSET)

        custom15 = d.pop("custom15", UNSET)

        custom16 = d.pop("custom16", UNSET)

        custom17 = d.pop("custom17", UNSET)

        custom18 = d.pop("custom18", UNSET)

        custom19 = d.pop("custom19", UNSET)

        custom2 = d.pop("custom2", UNSET)

        custom20 = d.pop("custom20", UNSET)

        custom3 = d.pop("custom3", UNSET)

        custom4 = d.pop("custom4", UNSET)

        custom5 = d.pop("custom5", UNSET)

        custom6 = d.pop("custom6", UNSET)

        custom7 = d.pop("custom7", UNSET)

        custom8 = d.pop("custom8", UNSET)

        custom9 = d.pop("custom9", UNSET)

        _date_changed = d.pop("dateChanged", UNSET)
        date_changed: Union[Unset, datetime.datetime]
        if isinstance(_date_changed, Unset):
            date_changed = UNSET
        else:
            date_changed = isoparse(_date_changed)

        _date_created = d.pop("dateCreated", UNSET)
        date_created: Union[Unset, datetime.datetime]
        if isinstance(_date_created, Unset):
            date_created = UNSET
        else:
            date_created = isoparse(_date_created)

        _date_of_birth = d.pop("dateOfBirth", UNSET)
        date_of_birth: Union[Unset, datetime.datetime]
        if isinstance(_date_of_birth, Unset):
            date_of_birth = UNSET
        else:
            date_of_birth = isoparse(_date_of_birth)

        _date_voided = d.pop("dateVoided", UNSET)
        date_voided: Union[Unset, datetime.datetime]
        if isinstance(_date_voided, Unset):
            date_voided = UNSET
        else:
            date_voided = isoparse(_date_voided)

        death_ind = d.pop("deathInd", UNSET)

        _death_time = d.pop("deathTime", UNSET)
        death_time: Union[Unset, datetime.datetime]
        if isinstance(_death_time, Unset):
            death_time = UNSET
        else:
            death_time = isoparse(_death_time)

        degree = d.pop("degree", UNSET)

        district = d.pop("district", UNSET)

        district_id = d.pop("districtId", UNSET)

        email = d.pop("email", UNSET)

        _ethnic_group = d.pop("ethnicGroup", UNSET)
        ethnic_group: Union[Unset, EthnicGroup]
        if isinstance(_ethnic_group, Unset):
            ethnic_group = UNSET
        else:
            ethnic_group = EthnicGroup.from_dict(_ethnic_group)

        family_name = d.pop("familyName", UNSET)

        family_name_2 = d.pop("familyName2", UNSET)

        father_name = d.pop("fatherName", UNSET)

        _gender = d.pop("gender", UNSET)
        gender: Union[Unset, Gender]
        if isinstance(_gender, Unset):
            gender = UNSET
        else:
            gender = Gender.from_dict(_gender)

        given_name = d.pop("givenName", UNSET)

        group_number = d.pop("groupNumber", UNSET)

        _language = d.pop("language", UNSET)
        language: Union[Unset, Language]
        if isinstance(_language, Unset):
            language = UNSET
        else:
            language = Language.from_dict(_language)

        marital_status_code = d.pop("maritalStatusCode", UNSET)

        middle_name = d.pop("middleName", UNSET)

        mother_name = d.pop("motherName", UNSET)

        mothers_maiden_name = d.pop("mothersMaidenName", UNSET)

        multiple_birth_ind = d.pop("multipleBirthInd", UNSET)

        _name_type = d.pop("nameType", UNSET)
        name_type: Union[Unset, NameType]
        if isinstance(_name_type, Unset):
            name_type = UNSET
        else:
            name_type = NameType.from_dict(_name_type)

        _nationality = d.pop("nationality", UNSET)
        nationality: Union[Unset, Nationality]
        if isinstance(_nationality, Unset):
            nationality = UNSET
        else:
            nationality = Nationality.from_dict(_nationality)

        person_id = d.pop("personId", UNSET)

        person_identifiers = []
        _person_identifiers = d.pop("personIdentifiers", UNSET)
        for person_identifiers_item_data in _person_identifiers or []:
            person_identifiers_item = PersonIdentifier.from_dict(person_identifiers_item_data)

            person_identifiers.append(person_identifiers_item)

        phone_area_code = d.pop("phoneAreaCode", UNSET)

        phone_country_code = d.pop("phoneCountryCode", UNSET)

        phone_ext = d.pop("phoneExt", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        _phone_type = d.pop("PhoneType", UNSET)
        phone_type: Union[Unset, PhoneType]
        if isinstance(_phone_type, Unset):
            phone_type = UNSET
        else:
            phone_type = PhoneType.from_dict(_phone_type)

        postal_code = d.pop("postalCode", UNSET)

        prefix = d.pop("prefix", UNSET)

        province = d.pop("province", UNSET)

        _race = d.pop("race", UNSET)
        race: Union[Unset, Race]
        if isinstance(_race, Unset):
            race = UNSET
        else:
            race = Race.from_dict(_race)

        _religion = d.pop("religion", UNSET)
        religion: Union[Unset, Religion]
        if isinstance(_religion, Unset):
            religion = UNSET
        else:
            religion = Religion.from_dict(_religion)

        sector = d.pop("sector", UNSET)

        sector_id = d.pop("sectorId", UNSET)

        ssn = d.pop("ssn", UNSET)

        state = d.pop("state", UNSET)

        suffix = d.pop("suffix", UNSET)

        _user_changed_by = d.pop("userChangedBy", UNSET)
        user_changed_by: Union[Unset, User]
        if isinstance(_user_changed_by, Unset):
            user_changed_by = UNSET
        else:
            user_changed_by = User.from_dict(_user_changed_by)

        _user_created_by = d.pop("userCreatedBy", UNSET)
        user_created_by: Union[Unset, User]
        if isinstance(_user_created_by, Unset):
            user_created_by = UNSET
        else:
            user_created_by = User.from_dict(_user_created_by)

        _user_voided_by = d.pop("userVoidedBy", UNSET)
        user_voided_by: Union[Unset, User]
        if isinstance(_user_voided_by, Unset):
            user_voided_by = UNSET
        else:
            user_voided_by = User.from_dict(_user_voided_by)

        village = d.pop("village", UNSET)

        village_id = d.pop("villageId", UNSET)

        person = cls(
            account=account,
            account_identifier_domain=account_identifier_domain,
            address1=address1,
            adress2=adress2,
            address_type=address_type,
            birth_order=birth_order,
            birth_place=birth_place,
            cell=cell,
            cell_id=cell_id,
            city=city,
            country=country,
            country_code=country_code,
            custom1=custom1,
            custom10=custom10,
            custom11=custom11,
            custom12=custom12,
            custom13=custom13,
            custom14=custom14,
            custom15=custom15,
            custom16=custom16,
            custom17=custom17,
            custom18=custom18,
            custom19=custom19,
            custom2=custom2,
            custom20=custom20,
            custom3=custom3,
            custom4=custom4,
            custom5=custom5,
            custom6=custom6,
            custom7=custom7,
            custom8=custom8,
            custom9=custom9,
            date_changed=date_changed,
            date_created=date_created,
            date_of_birth=date_of_birth,
            date_voided=date_voided,
            death_ind=death_ind,
            death_time=death_time,
            degree=degree,
            district=district,
            district_id=district_id,
            email=email,
            ethnic_group=ethnic_group,
            family_name=family_name,
            family_name_2=family_name_2,
            father_name=father_name,
            gender=gender,
            given_name=given_name,
            group_number=group_number,
            language=language,
            marital_status_code=marital_status_code,
            middle_name=middle_name,
            mother_name=mother_name,
            mothers_maiden_name=mothers_maiden_name,
            multiple_birth_ind=multiple_birth_ind,
            name_type=name_type,
            nationality=nationality,
            person_id=person_id,
            person_identifiers=person_identifiers,
            phone_area_code=phone_area_code,
            phone_country_code=phone_country_code,
            phone_ext=phone_ext,
            phone_number=phone_number,
            phone_type=phone_type,
            postal_code=postal_code,
            prefix=prefix,
            province=province,
            race=race,
            religion=religion,
            sector=sector,
            sector_id=sector_id,
            ssn=ssn,
            state=state,
            suffix=suffix,
            user_changed_by=user_changed_by,
            user_created_by=user_created_by,
            user_voided_by=user_voided_by,
            village=village,
            village_id=village_id,
        )

        person.additional_properties = d
        return person

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
