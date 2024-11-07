from datetime import datetime, timezone

import pytest

from comparison_interface.db.connection import db
from comparison_interface.db.models import Comparison


def test_api_not_available_when_not_configured(equal_weight_client):
    """
    GIVEN a flask app configured for testing and with equal weights and with API_ACCESS set to False
    WHEN the api url is requested
    THEN a 404 page is shown
    """
    response = equal_weight_client.get("/api/judgements")
    assert response.status_code == 404


def test_api_not_available_when_switched_on_but_no_key(equal_weight_client_api):
    """
    GIVEN a flask app configured for testing and with equal weights and with API_ACCESS set to True but no key file
    WHEN the api url is requested
    THEN a 501 page is shown
    """
    response = equal_weight_client_api.get("/api/judgements")
    assert response.status_code == 501


@pytest.mark.usefixtures('key_file')
def test_api_not_available_when_switched_on_but_no_key_sent(equal_weight_client_api):
    """
    GIVEN a flask app configured for testing, with equal weights, API_ACCESS and a key file
    WHEN the api url is requested but the api key is not provided
    THEN a 401 page is shown
    """
    response = equal_weight_client_api.get("/api/judgements")
    assert response.status_code == 401


@pytest.mark.usefixtures('key_file')
def test_api_available_when_switched_on_if_key_sent(equal_weight_client_api):
    """
    GIVEN a flask app configured for testing, with equal weights, API_ACCESS and a key file
    WHEN the api url is requested and the api key is provided
    THEN a 200 code is received and the comparison data is returned
    """
    comparison_data_list = [
        {
            'user_id': 1,
            'item_1_id': 1,
            'item_2_id': 2,
            'selected_item_id': 1,
            'state': 'selected',
            'created': datetime.now(timezone.utc),
            'updated': datetime.now(timezone.utc),
        },
        {
            'user_id': 1,
            'item_1_id': 4,
            'item_2_id': 3,
            'selected_item_id': None,
            'state': 'skipped',
            'created': datetime.now(timezone.utc),
            'updated': datetime.now(timezone.utc),
        },
    ]
    for comparison_data in comparison_data_list:
        comparison = Comparison(**comparison_data)
        db.session.add(comparison)
    db.session.commit()
    response = equal_weight_client_api.get("/api/judgements", headers={'x-api-key': 'test-key'})
    assert response.status_code == 200
    assert b'comparison_id\tuser_id\titem_1_id\titem_2_id\tselected_item_id\tstate\tcreated\tupdated' in response.data
    assert b'skipped' in response.data
    assert b'selected' in response.data
