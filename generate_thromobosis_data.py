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

def generate_random_number(min_num, max_num):
    return random.randint(min_num, max_num)

def generate_random_float(min_num, max_num):
    return random.uniform(min_num, max_num)

def generate_random_gender():
    genders = ['Male', 'Female']
    return genders[random.randint(0,1)]

def generate_random_lab(lab_name):
    values = parameters[parameters['Test Name'] == lab_name].values[0]
    return generate_random_float(values[1], values[2])

# settings
population_size = 20
thrombotic_test_size = 8
parameters = pd.read_csv('parameters.csv', index_col=0)
fake = Faker()
data_folder = 'synthetic_data/'

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

thrombotic_columns = [
        'Patient Identifier',
        'Test Name',
        'Test Value',
        'Test Datetime'
]

thrombotic_data = pd.DataFrame(columns=thrombotic_columns)

thrombotic_parameter_names = [
'Prothrombin Time',
'Activated Partial Thromboplastin Time',
'International Normalised Ratio',
'D-Dimer',
'Fibrinogen'
]

# patient_identifier = generate_random_string(8)
# for i in range(thrombotic_test_size):
#     datetime = fake.date_time_between(start_date='-' + str(i) + 'd', end_date='-' + str(i+1) + 'd' ).strftime('%Y-%m-%d %H:%M:%S')
#     for parameter_name in thrombotic_parameter_names:
#         thrombotic_data = thrombotic_data.append({
#             'Patient Identifier': patient_identifier,
#             'Test Name': parameter_name,
#             'Test Value': generate_random_lab(parameter_name),
#             'Test Datetime': datetime
#             }, ignore_index=True)

for i in range(population_size):
    thrombotic_event = generate_random_number(0,1)
    bleeding_event = generate_random_number(0,1)
    thrombotic_event_only = 0
    bleeding_event_only = 0
    thrombotic_bleeding_event = thrombotic_event & bleeding_event

    if thrombotic_event == 1 and bleeding_event == 0:
        thrombotic_event_only = 1

    if thrombotic_event == 0 and bleeding_event == 1:
        bleeding_event_only = 1


    patient_identifier = generate_random_string(8)
    data = data.append({
        'Patient Identifier': patient_identifier,
        'Age': generate_random_number(20,85),
        'Gender': generate_random_number(0,1),
        'Thrombotic Event': thrombotic_event,
        'Bleeding Event': bleeding_event,
        'Thrombotic only Event': thrombotic_event_only, 
        'Bleeding only Event': bleeding_event_only, 
        'Thrombotic Bleeding Event': thrombotic_bleeding_event,
        'Acute Respiratory Distress Syndrome': generate_random_number(0,1),
        'Mechanical Ventilation': generate_random_number(0,1),
        'Inotropic Medications': generate_random_number(0,1),
        'ICU Stay': generate_random_number(0,1),
        'Death': generate_random_number(0,1)
        }, ignore_index=True)

    for i in range(thrombotic_test_size):
        datetime = fake.date_time_between(start_date='-' + str(i) + 'd', end_date='-' + str(i+1) + 'd' ).strftime('%Y-%m-%d %H:%M:%S')
        for parameter_name in thrombotic_parameter_names:
            thrombotic_data = thrombotic_data.append({
                'Patient Identifier': patient_identifier,
                'Test Name': parameter_name,
                'Test Value': generate_random_lab(parameter_name),
                'Test Datetime': datetime
                }, ignore_index=True)

data.to_csv(data_folder + 'data.csv')
thrombotic_data.to_csv(data_folder + 'thrombotic_data.csv')
