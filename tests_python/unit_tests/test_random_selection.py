import json
import os
from datetime import datetime, timezone

import pytest
from PIL import Image
from sqlalchemy import MetaData
from sqlalchemy.exc import SQLAlchemyError

from comparison_interface.db.connection import db
from comparison_interface.db.models import UserGroup
from comparison_interface.views import rank
from comparison_interface.views.register import Request
from tests_python.conftest import execute_setup


@pytest.fixture()
def larger_app():
    """Set up the project for testing with equal weights."""
    # create the images
    with open("tests_python/test_configurations/config-larger.json", mode="r") as config_file:
        config_dict = json.load(config_file)
    for image_config in config_dict['comparisonConfiguration']['groups'][0]['items']:
        image_name = image_config['imageName']
        new_image = Image.new("RGB", (300, 300))
        new_image.save(f"comparison_interface/static/images/{image_name}", "PNG")
    app = execute_setup("../tests_python/test_configurations/config-larger.json")
    yield app

    with app.app_context():
        # delete the created images
        for image_config in config_dict['comparisonConfiguration']['groups'][0]['items']:
            image_name = image_config['imageName']
            os.remove(f"comparison_interface/static/images/{image_name}")
        db.session.remove()
        db.drop_all()
        os.unlink('instance/test_database.db')


@pytest.fixture()
def larger_client(larger_app):
    """Return the test client for the equal weight app."""
    with larger_app.app_context():
        yield larger_app.test_client()


@pytest.fixture()
def add_basic_data_larger(larger_client):
    # add data for a user in the group
    user_data = {}
    user_data['created_date'] = datetime.now(timezone.utc)
    db_engine = db.engines[None]
    db_meta = MetaData()
    db_meta.reflect(bind=db_engine)
    table = db_meta.tables["user"]
    new_user_sql = table.insert().values(**user_data)
    try:
        # Insert the user into the database
        with db.engine.begin() as connection:
            result = connection.execute(new_user_sql)
        id = result.lastrowid
    except SQLAlchemyError as e:
        raise RuntimeError(str(e))
    db.session.commit
    # insert the group preferences for the user (assumes groups are always added the same way)
    user_group_data = {
        'user_id': id,
        'group_id': 1,
        'created_date': datetime.now(timezone.utc),
    }
    user_group = UserGroup(**user_group_data)
    db.session.add(user_group)
    db.session.commit()
    yield


@pytest.mark.usefixtures('add_basic_data_larger')
def test_random_item_retrieval(mocker, larger_app):
    """
    GIVEN a flask app configured for testing with a configuration file with 70 items with equal weights
    WHEN a user has an active session specifying a group_id and _get_random_items is called
    THEN the correct list of 70 item ids are provided to the random number generator
    """
    request = Request(larger_app, {})
    request._session['user_id'] = 1
    request._session['group_ids'] = [1]
    request._session['weight_conf'] = 'equal'
    request._session['previous_comparison_id'] = None
    request._session['comparison_ids'] = []
    ranker = rank.Rank(request, request._session)
    spy = mocker.spy(rank, 'choice')
    items = ranker._get_random_items()
    # check that we feed the correct ids to the random item generator
    expected_ids = [x for x in range(1, 71)]
    spy.assert_called_once_with(expected_ids, 2, False)
    # check that we get two items returned from the range
    assert len(items) == 2
    assert items[0].item_id in expected_ids
    assert items[1].item_id in expected_ids


@pytest.mark.usefixtures('add_basic_data_larger')
def test_random_item_retrieval_on_repeat(larger_app):
    """
    GIVEN a flask app configured for testing with a configuration file with 70 items with equal weights
    WHEN a user has an active session specifying a group_id and _get_random_items is called multiple times
    THEN in repeated calls the generation of the item ids remains random

    Makes 100 calls to _get_random_items 100 times and checks that the mean uniqueness of pairs over those runs is
    greater than or equal to 97
    """
    request = Request(larger_app, {})
    request._session['user_id'] = 1
    request._session['group_ids'] = [1]
    request._session['weight_conf'] = 'equal'
    request._session['previous_comparison_id'] = None
    request._session['comparison_ids'] = []
    ranker = rank.Rank(request, request._session)
    uniqueness_counts = []
    for _ in range(1, 100):
        suggested_item_ids = []
        for _ in range(0, 100):
            items = ranker._get_random_items()
            suggested_item_ids.append(items)
        assert len(suggested_item_ids) == 100
        unique_items = set(suggested_item_ids)
        uniqueness_counts.append(len(unique_items))
    mean_uniqueness = sum(uniqueness_counts) / len(uniqueness_counts)
    assert mean_uniqueness >= 100 - 3
