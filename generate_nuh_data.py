from scipy.stats import norm
import matplotlib.pyplot as plt
import random
import string
import pandas as pd
from faker import Faker

# settings
population_size = 20
fake = Faker()

def generate_norm(sample_min, sample_max, size):
    mean = (sample_min + sample_max) / 2 
    std = (sample_max - sample_min) / 2
    return norm.rvs(loc=mean, scale=std, size=size)

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

def generate_random_race():
    races = ['Chinese', 'Malay', 'Indian', 'Others']
    return races[random.randint(0,3)]

columns = ['Patient NRIC','Patient Age','Gender','Race','Deceased Ind','Death Date']
data = pd.DataFrame(columns=columns)

for i in range(20):
    data = data.append({
        'Patient NRIC': generate_random_string(8),
        'Patient Age': generate_random_number(20, 80),
        'Gender': generate_random_gender(),
        'Race': generate_random_race(),
        'Deceased Ind': generate_random_number(0,1),
        'Death Date': fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')
        }, ignore_index=True)


# data.to_csv('patient_demographics.csv')

# f = open('parameters.txt', 'r')
# parameters_string = f.read()
# parameters_array = parameters_string.split('\n')

# for parameter in parameters_array:
#     if len(parameter) == 0: 
#         break
#     parameter_array = parameter.split(',')
#     parameter_name = parameter_array[0]
#     parameter_min = float(parameter_array[1])
#     parameter_max = float(parameter_array[2])
#     # parameter_samples = generate_norm(parameter_min, parameter_max, 100)
#     print(parameter_name)
#     print(parameter_min)
#     print(parameter_max)

# hemoglobin_male = parameters_array[0]
# hemoglobin_male_array = hemoglobin_male.split(',')
# hemoglobin_male_min = float(hemoglobin_male_array[1])
# hemoglobin_male_max = float(hemoglobin_male_array[2])

# hemoglobin_male_samples = generate_norm(hemoglobin_male_min, hemoglobin_male_max, 100)
# print(hemoglobin_male_samples)

# get_random_string(8)
# get_random_string(8)
# get_random_string(6)

