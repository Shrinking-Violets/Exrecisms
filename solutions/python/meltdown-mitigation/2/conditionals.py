
def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000:
        return True
    else:
        return  False
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    percent = (generated_power/theoretical_max_power) * 100

    if percent >= 80:
        return "green"
    elif 80 > percent >= 60:
        return "orange"
    elif 60 > percent >= 30:
        return "red"
    elif percent < 30:
        return"black"
        
def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if (temperature * neutrons_produced_per_second) <= 0.9 * threshold:
        return "LOW"
    elif 0.9 * threshold <= (temperature * neutrons_produced_per_second) <= 1.1 * threshold: 
        return "NORMAL"
    else:
        return "DANGER"

   