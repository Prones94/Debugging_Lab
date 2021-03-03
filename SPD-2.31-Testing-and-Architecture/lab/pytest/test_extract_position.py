import pytest
import extract_position_function as e4

@pytest.fixture
def average_input():
  return "|update| the position location accelerator is x:21.432"

@pytest.fixture
def null_input():
  """For whatever reason its null"""
  return None

@pytest.fixture
def error_input():
  return "|error| calculation no work"

def test_null_case(null_input):
  """Reads in a log that is None"""
  assert e4.extract_position(null_input) == None

def test_average_case(average_input):
  assert e4.extract_position(average_input) == "21.432"

