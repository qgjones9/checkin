from mongoengine import ValidationError


def grade_level_validator(val):
    if val not in ["01", "02", "k3", "k4", "k5"]:
        raise ValidationError('value can not be empty')

