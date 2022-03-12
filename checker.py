# Run as python checker.py model.py
# Requires Python 3.7 or newer

# Import model loader
from Part_1.model import Model

# Model class which performs the checks on the provided model.
model = Model()

# Check Exist properties.
model.check_property_exists()

# Check Xmin properties.
model.check_property_xmin()

#schedule.create_schedules_from_txt_file('trace.txt')
print("Model checker finished successfully")