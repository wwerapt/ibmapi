# webinterface/calculate.py
import numpy as np
import pandas as pd

def calculate_values(post_data):
    branch_results = {}

    # Assuming your branch numbers follow a specific pattern
    for i in range(1, 31):  # Adjust the range according to your actual branch numbers
        media_key = f"media_br{i}"
        campaign_key = f"campaign_br{i}"
        touchpoint_key = f"touchpoint_br{i}"
        
        # Retrieve values from post_data and convert to integers
        # Using 0 as default if the key doesn't exist
        media_value = int(post_data.get(media_key, 0))
        campaign_value = int(post_data.get(campaign_key, 0))
        touchpoint_value = int(post_data.get(touchpoint_key, 0))
        
        # Perform the calculation
        branch_result = media_value * campaign_value * touchpoint_value
        
        # Store the result in a dictionary with the branch number as key
        branch_results[f"xbr{i}"] = branch_result
        
    print(branch_results)

    

    return branch_results
