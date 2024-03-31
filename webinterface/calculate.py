# webinterface/calculate.py
import numpy as np
import pandas as pd
import math
import random

def calculate_values(post_data):
    branch_results = {}

    # Retrieve the 'day' value from post_data and convert to integer
    day_value = int(post_data.get('day', 1))  # Using 1 as default if the key doesn't exist

    # Assuming your branch numbers follow a specific pattern
    for i in range(1, 31):  # Adjust the range according to your actual branch numbers
        media_key = f"media_br{i}"
        campaign_key = f"campaign_br{i}"
        touchpoint_key = f"touchpoint_br{i}"
        service_key = f"service_br{i}"  # New
        special_key = f"special_br{i}"  # New
        
        # Retrieve values from post_data and convert to integers
        # Using 0 as default if the key doesn't exist
        media_value = int(post_data.get(media_key, 0))
        campaign_value = int(post_data.get(campaign_key, 0))
        touchpoint_value = int(post_data.get(touchpoint_key, 0))
        service_value = int(post_data.get(service_key, 0))  # New
        special_value = int(post_data.get(special_key, 0))  # New
        
        # Perform the calculation
        # Example calculation modified to include service_value and special_value
        # Modify the formula as per your requirements
        branch_result = (media_value * campaign_value * touchpoint_value * service_value * special_value)
        
        # Store the result in a dictionary with the branch number as key
        branch_results[f"br{i}"] = branch_result
        
    #print(branch_results)

    xbr = pd.DataFrame(list(branch_results.items()), columns=['branch', 'xbr'])

    print(xbr)

    print(day_value)

    #------------- living area --------------------------------

    living_area_data = {
    'understand_customer': [1,1,1,1,1,
                           1,1,1,1,1,
                           1,1,1,1,1,
                           1,1,1,1,1,
                           1,1,1,1,1,
                           1,1,1,1,1],
    'climate': [1,1,1,1,1,
                1,1,1,1,1,
                1,1,1,1,1,
                1,1,1,1,1,
                1,1,1,1,1,
                1,1,1,1,1],
    'income_per_head': [1,1,1,1,1,
                        1,1,1,1,1,
                        1,1,1,1,1,
                        1,1,1,1,1,
                        1,1,1,1,1,
                        1,1,1,1,2],
    'heatmap': [1,1,1,1,1,
                1,1,1,1,1,
                1,1,1,1,1,
                1,1,1,5,1,
                1,1,1,1,1,
                1.2,1.5,1.3,1.05,2]
    }

    # Create the DataFrame
    living_area = pd.DataFrame(living_area_data, index=['br'+str(i) for i in range(1, 31)])

    # Calculate the total
    living_area['total'] = living_area['understand_customer'] * living_area['climate'] * living_area['income_per_head'] * living_area['heatmap']


    #------------- persona --------------------------------
    persona_data = {
    'gender': [0,1,0,1,0,1,0,1,0,1],
    'age': ['15-30','15-30','30-45','30-45','45-55',
           '45-55','55-65','55-65','65+','65+'],
    'skin_problem': [1] * 10,
    'behavior': [1] * 10,
    'repeat': [1] * 10,
    'response': [1,0.95,0.78,1.2,1.32,0.85,0.98,0.156,0.81,1.35]
    }

    # Create the DataFrame
    persona = pd.DataFrame(persona_data, index=['persona'+str(i) for i in range(1, 11)])

    return branch_results
