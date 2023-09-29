import pytest
from lib.task_tracker import *

'''
Given a text containing #TODO
returns "Contains #TODO"
'''
def test_task_tracker():
    assert task_tracker("#TODO eat") == "Contains #TODO"

'''
Given a text not containing #TODO
returns "Does not contain #TODO"
'''
def test_task_tracker():
    assert task_tracker("i need to eat") == "Does not contain #TODO"

'''
Given an empty string
returns the error message: "I need a string containing #TODO"
'''
def test_task_tracker_with_empty():
    with pytest.raises (Exception) as e:
        task_tracker("")
    error_message = str(e.value)

