WELL_DONE = 900000
MEDIUM = 600000
COOKED_CONSTANT = 0.05
​
def is_cookeding_criteria_satisfied(time, temperature, pressure, desired_state):
    is_well_done = time * temperature * pressure * COOKED_CONSTANT >= WELL_DONE
    is_medium = time * temperature * pressure * COOKED_CONSTANT >= MEDIUM
    if desired_state == 'well-done' and is_well_done:
        return True
    if desired_state == 'medium' and is_medium:
        return True
