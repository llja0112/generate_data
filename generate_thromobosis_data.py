import matplotlib.pyplot as plt
import random
import string
import pandas as pd
from faker import Faker

def generate_random_string(length):
    letters_digits = string.ascii_lowercase + string.digits
    result_str = ''.join(random.choice(letters_digits) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str

def generate_random_number(min, max):
    return random.randint(min, max)

def generate_random_gender():
    genders = ['Male', 'Female']
    return genders[random.randint(0,1)]

# settings
population_size = 20

columns = [
        'Patient Identifier', 
        'Age', 
        'Gender', 
        'Thrombotic Event', 
        'Bleeding Event', 
        'Thrombotic only Event', 
        'Bleeding only Event', 
        'Thrombotic Bleeding Event',
        'Acute Respiratory Distress Syndrome',
        'Mechanical Ventilation',
        'Inotropic Medications',
        'ICU Stay',
        'Death'
]

data = pd.DataFrame(columns=columns)
for i in range(population_size):
    data = data.append({
        'Patient Identifier': generate_random_string(8),
        'Age' generate_random_number(20,85),
        'Gender': generate_random_number(0,1),
        'Thrombotic Event': generate_random_number(0,1),
        'Thrombotic only Event': generate_random_number(0,1), 
        'Bleeding only Event': generate_random_number(0,1), 
        'Thrombotic Bleeding Event': generate_random_number(0,1),
        'Acute Respiratory Distress Syndrome': generate_random_number(0,1),
        'Mechanical Ventilation': generate_random_number(0,1),
        'Inotropic Medications': generate_random_number(0,1),
        'ICU Stay': generate_random_number(0,1),
        'Death': generate_random_number(0,1)
        })

