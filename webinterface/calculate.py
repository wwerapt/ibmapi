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

    #------------- Mock Total Demand Branch --------------------------------

    # Set the random seed for reproducibility
    np.random.seed(42)

    # Generate random demand for each branch
    demand = np.random.randint(500, 1201, size=30)

    # Create a DataFrame to store branch number and demand
    branch_demand = pd.DataFrame({
        'branch': [f'br{i}' for i in range(1, 31)],
        'demand': demand
    })

    # Merge xbr and living_area DataFrames
    merged_df = xbr.merge(living_area, how='left', left_on='branch', right_index=True)

    # Calculate the 'coefficient' column
    merged_df['coefficient'] = merged_df['xbr'] * merged_df['total']

    # Create branch_demand DataFrame
    branch_demand = pd.DataFrame({
        'branch': merged_df['branch'],
        'demand': demand,
        'coefficient': merged_df['coefficient']
    })

    branch_demand['total_demand'] = branch_demand['demand'] * branch_demand['coefficient']

    # Round up to the nearest integer
    branch_demand['total_demand'] = np.ceil(branch_demand['total_demand']).astype(int)

    branch_proportions = {
        'br1': {'ProductA': 0.20, 'ProductB': 0.30, 'ProductC': 0.25, 'ProductD': 0.25},
        'br2': {'ProductA': 0.25, 'ProductB': 0.25, 'ProductC': 0.25, 'ProductD': 0.25}, 
        'br3': {'ProductA': 0.30, 'ProductB': 0.20, 'ProductC': 0.30, 'ProductD': 0.20},
        'br4': {'ProductA': 0.10, 'ProductB': 0.40, 'ProductC': 0.30, 'ProductD': 0.20},
        'br5': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br6': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br7': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br8': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br9': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br10': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br11': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br12': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br13': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br14': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br15': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br16': {'ProductA': 0.20, 'ProductB': 0.30, 'ProductC': 0.25, 'ProductD': 0.25},
        'br17': {'ProductA': 0.25, 'ProductB': 0.25, 'ProductC': 0.25, 'ProductD': 0.25}, 
        'br18': {'ProductA': 0.30, 'ProductB': 0.20, 'ProductC': 0.30, 'ProductD': 0.20},
        'br19': {'ProductA': 0.10, 'ProductB': 0.40, 'ProductC': 0.30, 'ProductD': 0.20},
        'br20': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br21': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br22': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br23': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br24': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br25': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br26': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br27': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br28': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br29': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25},
        'br30': {'ProductA': 0.35, 'ProductB': 0.15, 'ProductC': 0.25, 'ProductD': 0.25}
    }

    # Function to calculate product demands
    def calculate_custom_product_demand(row):
        props = branch_proportions.get(row['branch'])
        for product, proportion in props.items():
            row[product] = math.ceil(row['total_demand'] * proportion)
        return row


    # Apply the function to calculate product demands
    branch_demand = branch_demand.apply(calculate_custom_product_demand, axis=1)

    # Rename the columns to match your final structure
    branch_demand.rename(columns={
        'ProductA': 'productA',
        'ProductB': 'productB',
        'ProductC': 'productC',
        'ProductD': 'productD'
    }, inplace=True)

    print(branch_demand)

    #------------- Generate Transactions --------------------------------

    def generate_age(age_str):
        if age_str == '65+':
            return random.randint(65, 75)
        else:
            start_age, end_age = map(int, age_str.split('-'))
            return random.randint(start_age, end_age)

    def generate_transactions(product_demands, persona):
        transactions = []
        adjusted_response = persona['response'] * persona['repeat']
        probabilities = adjusted_response / adjusted_response.sum()
        remaining_demands = product_demands.copy()

        while sum(remaining_demands.values()) > 0:
            chosen_persona = persona.sample(weights=probabilities).iloc[0]
            gender = chosen_persona['gender']
            age_str = chosen_persona['age']
            age = generate_age(age_str)

            # Initialize transaction with all product keys set to 0 and include persona info
            transaction = { 'productA': 0, 'productB': 0, 'productC': 0, 'productD': 0, 'gender': gender, 'age': age }

            # Probability of adding each additional product
            add_product_prob = 1.0
            while random.random() < add_product_prob and sum(remaining_demands.values()) > 0:
                product = random.choices(list(remaining_demands.keys()), weights=list(remaining_demands.values()), k=1)[0]
                if remaining_demands[product] > 0:
                    # Add product to transaction
                    transaction[product] += 1
                    remaining_demands[product] -= 1

                    # Decrease probability for next product
                    add_product_prob *= 0.7  # Adjust this factor to control the decrease rate

            transactions.append(transaction)

        return transactions
    
    all_branch_transactions = []

    for index, row in branch_demand.iterrows():
        product_demands = {
            'productA': row['productA'],
            'productB': row['productB'],
            'productC': row['productC'],
            'productD': row['productD']
        }
        
        transactions = generate_transactions(product_demands, persona)
        
        # Optionally, you might want to include branch information in each transaction
        for transaction in transactions:
            transaction['branch'] = row['branch']
        
        all_branch_transactions.extend(transactions)

    # Show a summary of generated transactions for all branches
    print(f"Total transactions generated for all branches: {len(all_branch_transactions)}")

    
    return branch_results
