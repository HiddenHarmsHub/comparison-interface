from comparison_interface.configuration.csv_processor import CsvProcessor


def test_minimum_csv_procesed_correctly():
    """
    GIVEN a csv file with the minimum required columns
    WHEN the function to turn the csv file into the JSON (Dict) config is called
    THEN the correct data is produced
    """
    processor = CsvProcessor()
    data = processor.create_config_from_csv('tests_python/test_configurations/csv_example_1/example_1.csv')
    expected_data = {
        "groups": [
            {
                "name": "default",
                "displayName": "default",
                "items": [
                    {"name": "north_east", "displayName": "North East", "imageName": "item_1.png"},
                    {"name": "north_west", "displayName": "North West", "imageName": "item_2.png"},
                    {
                        "name": "yorkshire_and_humberside",
                        "displayName": "Yorkshire and Humberside",
                        "imageName": "item_3.png",
                    },
                    {"name": "east_midlands", "displayName": "East Midlands", "imageName": "item_4.png"},
                    {"name": "west_midlands", "displayName": "West Midlands", "imageName": "item_5.png"},
                    {"name": "eastern", "displayName": "Eastern", "imageName": "item_6.png"},
                    {"name": "london", "displayName": "London", "imageName": "item_7.png"},
                    {"name": "south_east", "displayName": "South East", "imageName": "item_8.png"},
                    {"name": "south_west", "displayName": "South West", "imageName": "item_9.png"},
                ],
            },
        ],
        "weightConfiguration": "equal",
    }
    assert data == expected_data


def test_maximal_csv_processed_correctly():
    """
    GIVEN a csv file with the maximum columns
    WHEN the function to turn the csv file into the JSON (Dict) config is called
    THEN the correct data is produced
    """
    processor = CsvProcessor()
    data = processor.create_config_from_csv('tests_python/test_configurations/csv_example_2/example_2.csv')
    expected_data = {
        "groups": [
            {
                "name": "england",
                "displayName": "England",
                "items": [
                    {"name": "north_east", "displayName": "North East", "imageName": "item_1.png"},
                    {"name": "north_west", "displayName": "North West", "imageName": "item_2.png"},
                    {
                        "name": "yorkshire_and_humberside",
                        "displayName": "Yorkshire & Humberside",
                        "imageName": "item_3.png",
                    },
                    {"name": "east_midlands", "displayName": "East Midlands", "imageName": "item_4.png"},
                    {"name": "west_midlands", "displayName": "West Midlands", "imageName": "item_5.png"},
                    {"name": "eastern", "displayName": "Eastern", "imageName": "item_6.png"},
                    {"name": "london", "displayName": "London", "imageName": "item_7.png"},
                    {"name": "south_east", "displayName": "South East", "imageName": "item_8.png"},
                    {"name": "south_west", "displayName": "South West", "imageName": "item_9.png"},
                ],
            },
            {
                "name": "wales_scotland_northern_ireland",
                "displayName": "Wales, Scotland, Northern Ireland",
                "items": [
                    {"name": "wales", "displayName": "Wales", "imageName": "item_10.png"},
                    {"name": "scotland", "displayName": "Scotland", "imageName": "item_11.png"},
                    {"name": "northern_ireland", "displayName": "Northern Ireland", "imageName": "item_12.png"},
                ],
            },
        ],
        "weightConfiguration": "equal",
    }
    assert data == expected_data
