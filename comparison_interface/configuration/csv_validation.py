import os
import re
from csv import DictReader

from marshmallow import ValidationError
from PIL import Image


class CsvValidator():
    """A special validation class to validate a csv file used to upload images."""

    # Allowed Items Image size
    MIN_WIDTH = 300
    MIN_HEIGHT = 300

    def validate(self, file):
        """Validate the provided csv file."""
        with open(file, mode='r') as csv_input:
            image_data = DictReader(csv_input)
            image_data.fieldnames = [x.lower() for x in image_data.fieldnames]
            # required 'Item display name', 'image' everything else can be invented (case doesn't matter)
            required_keys = ['item display name', 'image']
            optional_keys = ['item name', 'group name', 'group display name']
            for key in required_keys:
                if key not in image_data.fieldnames:
                    raise ValidationError(
                        'The csv file must have columns named "item display  name" and "image" (case does not matter, '
                        'spaces do). Your file is missing one of these columns.'
                    )
            # TODO: should we warn about keys where are in the CSV but will be ignored?
            for entry in image_data:
                # if the optional ones are missing we expand from what we have
                self.expand_entry(entry)
                self.validate_entry(entry)
            # check all items in the group are unique
            self.validate_groups(image_data)

    def expand_entry(self, entry):
        """Expand the fields to mimic the JSON format."""
        if 'item name' not in entry:
            entry['item name'] = entry["item display name"].lower().replace(" ", "_")
        if 'group display name' not in entry:
            entry['group display name'] = 'default'
        if 'group name' not in entry:
            entry["group name"] = entry["group display name"].lower().replace(" ", "_")

    def validate_entry(self, entry):
        """Validate the provided image data."""
        # group name
        match = re.match(r"^[a-z0-9_-]+$", entry["group name"])
        if not match:
            raise ValidationError(
                "Group name can only contain alpha numeric lower case values with underscores or dashes. "
                "i.e. 'this_is_a_valid_name'. If you are not supplying a 'group name' column then this will have been "
                "automatically generated from the 'group display name' column by making the value lower case and "
                "replacing spaces with underscores. You will either need to remove any special characters from the "
                "'group display name' column or provide a 'group name' column that meets the criteria specified "
                f"above. The problem entry is '{entry['group_name']}'."
            )
        # item name
        match = re.match(r"^[a-z0-9_-]+$", entry["item name"])
        if not match:
            raise ValidationError(
                "Item name can only contain alpha numeric lower case values with underscores or dashes. "
                "i.e. 'this_is_a_valid_name'. If you are not supplying an 'item name' column then this will have been "
                "automatically generated from the 'item display name' column by making the value lower case and "
                "replacing spaces with underscores. You will either need to remove any special characters from the "
                "'item display name' column or provide an 'item name' column that meets the criteria specified "
                f"above. The problem entry is '{entry['item name']}'."
            )
        # check image path
        path = os.path.abspath(os.path.dirname(__file__)) + "/../static/images/" + entry["image"]
        if not os.path.exists(path):
            raise ValidationError(f"Image {entry['image']} not found on static/images/ folder.")

        # check image size
        try:
            im = Image.open(path)
            h, w = im.size
            if h < self.MIN_HEIGHT or w < self.MIN_WIDTH:
                raise ValidationError(f"All item images must be at least {self.MIN_HEIGHT}x{self.MIN_WIDTH}px.")
        except Exception as e:
            raise ValidationError(str(e))

    def validate_groups(self, data):
        """Check that each item name in each group is unique to that group."""
        # TODO: write this
        pass
