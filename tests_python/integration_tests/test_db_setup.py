from sqlalchemy import text

from comparison_interface.db.connection import db


def test_user_setup(equal_weight_app):
    """
    GIVEN a flask app configured for testing and equal weights
    WHEN the database is initialised
    THEN the user table is built correctly from the config
    """
    with equal_weight_app.app_context():
        sql = 'SELECT * FROM "user"'
        user_columns = db.session.execute(text(sql)).keys()
        assert len(user_columns) == 9
        assert user_columns == [
            'user_id',
            'created_date',
            'completed_cycles',
            'name',
            'country',
            'allergies',
            'age',
            'email',
            'accepted_ethics_agreement',
        ]


def test_setup_items_equal_weights(equal_weight_app):
    """
    GIVEN a flask app configured for testing and equal weights
    WHEN the database is initialised
    THEN the correct groups and items are added to the database but no custom item pairs are added
    """
    with equal_weight_app.app_context():
        item_count_sql = 'SELECT * FROM "item"'
        items = db.session.execute(text(item_count_sql)).all()
        assert len(items) == 12

        group_count_sql = 'SELECT * FROM "group"'
        groups = db.session.execute(text(group_count_sql)).all()
        assert len(groups) == 2

        item_group_count_sql = 'SELECT * FROM "item_group"'
        item_groups = db.session.execute(text(item_group_count_sql)).all()
        assert len(item_groups) == 12

        pair_sql = 'SELECT * FROM "custom_item_pair"'
        pairs = db.session.execute(text(pair_sql)).all()
        assert len(pairs) == 0

        website_control_sql = 'SELECT * FROM "website_control"'
        website_control = db.session.execute(text(website_control_sql)).all()
        assert len(website_control) == 1

        user_sql = 'SELECT * FROM "user"'
        users = db.session.execute(text(user_sql)).all()
        assert len(users) == 0


def test_setup_items_custom_weights(custom_weight_app):
    """
    GIVEN a flask app configured for testing and custom weights
    WHEN the database is initialised
    THEN the correct groups, items custom item pairs are added to the database
    """
    with custom_weight_app.app_context():
        item_sql = 'SELECT * FROM "item"'
        items = db.session.execute(text(item_sql)).all()
        assert len(items) == 6

        group_sql = 'SELECT * FROM "group"'
        groups = db.session.execute(text(group_sql)).all()
        assert len(groups) == 2

        item_group_sql = 'SELECT * FROM "item_group"'
        item_groups = db.session.execute(text(item_group_sql)).all()
        assert len(item_groups) == 7

        pair_sql = 'SELECT * FROM "custom_item_pair"'
        pairs = db.session.execute(text(pair_sql)).all()
        assert len(pairs) == 9

        website_control_sql = 'SELECT * FROM "website_control"'
        website_control = db.session.execute(text(website_control_sql)).all()
        assert len(website_control) == 1

        user_sql = 'SELECT * FROM "user"'
        users = db.session.execute(text(user_sql)).all()
        assert len(users) == 0
