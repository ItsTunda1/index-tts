import os
import pandas as pd



# Function to transform the tensor into a format suitable for CSV
def transform_to_csv(spk_cond_emb, file_name='output.csv'):
    # Get the number of time steps (16) and features (160)
    num_time_steps = spk_cond_emb.size(1)
    num_features = 160  # This is fixed as per your requirement

    # Create an empty list to store the rows for CSV
    rows = []

    # For each time step, slice the first 160 columns and store the data
    for time_step in range(num_time_steps):
        # Extract the relevant 160 features for the current time step
        features = spk_cond_emb[0, time_step, :num_features].tolist()
        
        # Add the time step number as the first column
        rows.append([time_step] + features)

    # Create a DataFrame from the rows
    column_names = ['Steps'] + [f'T{i+1}' for i in range(num_features)]
    df = pd.DataFrame(rows, columns=column_names)
    
    # Check if the file already exists (to avoid rewriting headers)
    if os.path.exists(file_name):
        # Append to the existing CSV file (no header)
        df.to_csv(file_name, mode='a', header=False, index=False)
    else:
        # Create the CSV file with the header
        df.to_csv(file_name, mode='w', header=True, index=False)