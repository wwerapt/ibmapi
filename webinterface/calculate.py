# webinterface/calculate.py
import numpy as np
import pandas as pd
import math

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
        
    print(branch_results)

    xbr = pd.DataFrame(list(branch_results.items()), columns=['branch', 'xbr'])

    print(xbr)

    print(day_value)

    return branch_results
