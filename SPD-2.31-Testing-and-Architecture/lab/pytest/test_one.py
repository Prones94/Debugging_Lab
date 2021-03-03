# test_one.py
import math

def calculate_kinetic_energy(mass, velocity):
    """Returns kinetic energy of mass [kg] with velocity [ms]."""
    return 0.5 * mass * velocity ** 2

def test_calculate_kinetic_energy():
    mass = 10 # [kg]
    velocity = 4 # [m/s]
    assert calculate_kinetic_energy(mass, velocity) == 80

def get_average(li):
    sum = 0
    for num in li:
        sum += num
    mean = sum / len(li)
    return mean

def test_get_average_normal_use_case():
    assert math.isclose(get_average([1,2,3,4]), 2.5)