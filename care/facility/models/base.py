from care.utils.models.base import BaseModel


def pretty_boolean(val, a="YES", b="NO", c="Not Specified"):
    if val is None:
        return c
    if val:
        return a
    return b


def reverse_choices(choices):
    output = {}
    for choice in choices:
        output[choice[0]] = choice[1]
    return output


def covert_choice_dict(choices):   # we have same function in choicefilter and inverse_choices.py
    output = {}
    for choice in choices:
        output[choice[1]] = choice[0]
    return output


def covert_choice_dict_class(choices_class):
    output = {}
    for choice in choices_class:
        output[choice.name] = choice.value
    return output


class FacilityBaseModel(BaseModel):
    class Meta:
        abstract = True


class PatientBaseModel(BaseModel):
    class Meta:
        abstract = True
