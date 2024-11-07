import pytest
from marshmallow import ValidationError

from comparison_interface.configuration.schema import BehaviourConfiguration, Weight


def test_empty_weight_schema_raises_error():
    test_schema = {}
    with pytest.raises(ValidationError) as err:
        weight_schema = Weight()
        weight_schema.load(test_schema)
    assert len(err.value.messages_dict.keys()) == 3


def test_behaviour_configuration_for_escape_route_false():
    test_behaviour_schema = {
        "exportPathLocation": "exports",
        "renderUserItemPreferencePage": False,
        "renderUserInstructionPage": False,
        "renderEthicsAgreementPage": False,
        "renderSitePoliciesPage": False,
        "renderCookiesFooter": False,
        "offerEscapeRouteBetweenCycles": False,
    }
    behaviour_schema = BehaviourConfiguration()
    try:
        behaviour_schema.load(test_behaviour_schema)
    except ValidationError as err:
        assert False, f'ValidationError raised: {err}'


def test_behaviour_configuration_for_escape_route_true_with_all_requirements():
    test_behaviour_schema = {
        "exportPathLocation": "exports",
        "renderUserItemPreferencePage": False,
        "renderUserInstructionPage": False,
        "renderEthicsAgreementPage": False,
        "renderSitePoliciesPage": False,
        "renderCookiesFooter": False,
        "offerEscapeRouteBetweenCycles": True,
        "cycleLength": 30,
        "maximumCyclesPerUser": 3,
    }
    behaviour_schema = BehaviourConfiguration()
    try:
        behaviour_schema.load(test_behaviour_schema)
    except ValidationError as err:
        assert False, f'ValidationError raised: {err}'


def test_behaviour_configuration_for_escape_route_true_with_missing_requirements():
    test_behaviour_schema = {
        "exportPathLocation": "exports",
        "renderUserItemPreferencePage": False,
        "renderUserInstructionPage": False,
        "renderEthicsAgreementPage": False,
        "renderSitePoliciesPage": False,
        "renderCookiesFooter": False,
        "offerEscapeRouteBetweenCycles": True,
        "cycleLength": 30,
    }
    with pytest.raises(ValidationError) as err:
        behaviour_schema = BehaviourConfiguration()
        behaviour_schema.load(test_behaviour_schema)
    assert len(err.value.messages_dict.keys()) == 1
