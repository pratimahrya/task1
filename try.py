from typing import Any, Callable, Dict

dictionary = {
    "name": "papaya",
    "phone": 9869239512,
    "height": 6,
    "weight": 70,
    "race": "asian",
    "vaccinated": True
}


def type_not_matched(value: Any) -> bool:
    return True


def validate_string(value: str) -> bool:
    """Rule to validate the given string value"""
    MIN_LENGTH = 3
    MAX_LENGTH = 20
    return MIN_LENGTH < len(value) < MAX_LENGTH


def validate_int(value: int) -> bool:
    """Rule to validate the given int value"""
    MAX_LENGTH = 9999999999
    MIN_LENGTH = 1
    return MIN_LENGTH < value < MAX_LENGTH


type_validators = {str: validate_string, int: validate_int}


def default_validator(value: str) -> bool:
    return True


dict_validator = {"name": [validate_string], "phone": [validate_int]}


# def validate_dict_keys(dict: Dict, validators: Dict[Any, Callable]) -> bool:
# for key, value in dict.items():
# _validators = validators.get(key, [default_validator])
# for is_valid in _validators:
# if not is_valid(value):
# return False
# return True


def validate_dict(dict: Dict, validators: Dict[Any, Callable]) -> bool:
    for value in dict.values():
        data_type = type(value)
        if not validators.get(data_type, type_not_matched)(value):
            return False
    return True


print(validate_dict(dictionary, type_validators))
# print(validate_dict_keys(dictionary, dict_validator))