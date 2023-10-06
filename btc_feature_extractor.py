#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv

def btc_extract_feature(input_file_path, result_file_path):
    window_size = 30

    moving_averages = []  

    positions = []
    velocities = []
    accelerations = []
    jerks = []

    max_velocity_y = []
    min_velocity_y = []
    max_acceleration_y = []
    min_acceleration_y = []
    start_accelerations_y = []
    end_accelerations_y = []
    max_jerk_y = []
    min_jerk_y = []

    with open(input_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Skip the header row

        prev_frame_number = None
        prev_position_x = None
        prev_position_y = None
        prev_velocity_x = None
        prev_velocity_y = None
        acceleration_x = 0.0  # Initialize acceleration_x
        acceleration_y = 0.0  # Initialize acceleration_y
        prev_acceleration_x = None
        prev_acceleration_y = None
        prev_jerk_x = None
        prev_jerk_y = None
        jerk_x = 0.0  # Initialize jerk_x
        jerk_y = 0.0  # Initialize jerk_y

        for row in csv_reader:
            frame_number = int(row[0])
            position_x = float(row[1])
            position_y = float(row[2])

            velocity_x = 0.0  # Initialize velocity_x
            velocity_y = 0.0  # Initialize velocity_y

            if prev_frame_number is not None:
                time_interval = frame_number - prev_frame_number

                if time_interval != 0:
                    velocity_x = (position_x - prev_position_x) / time_interval
                    velocity_y = (position_y - prev_position_y) / time_interval
                    velocities.append((frame_number, velocity_x, velocity_y))

                    acceleration_x = (velocity_x - prev_velocity_x) / time_interval
                    acceleration_y = (velocity_y - prev_velocity_y) / time_interval
                    accelerations.append((frame_number, acceleration_x, acceleration_y))

                    jerk_x = (acceleration_x - prev_acceleration_x) / time_interval
                    jerk_y = (acceleration_y - prev_acceleration_y) / time_interval
                    jerks.append((frame_number, jerk_x, jerk_y))

            prev_frame_number = frame_number
            prev_position_x = position_x
            prev_position_y = position_y
            prev_velocity_x = velocity_x
            prev_velocity_y = velocity_y
            prev_acceleration_x = acceleration_x
            prev_acceleration_y = acceleration_y
            prev_jerk_x = jerk_x
            prev_jerk_y = jerk_y

            if len(accelerations) >= 30:
                group_velocities = velocities[-30:]
                max_velocity_y_value = max(group_velocities, key=lambda x: x[2])[2]
                max_velocity_y.append(max_velocity_y_value)

                min_velocity_y_value = min(group_velocities, key=lambda x: x[2])[2]
                min_velocity_y.append(min_velocity_y_value)

                group_accelerations = accelerations[-30:]
                max_acceleration_y_value = max(group_accelerations, key=lambda x: x[2])[2]
                max_acceleration_y.append(max_acceleration_y_value)

                start_accelerations_y_value = group_accelerations[0][2]
                start_accelerations_y.append(start_accelerations_y_value)

                end_accelerations_y_value = group_accelerations[-1][2]
                end_accelerations_y.append(end_accelerations_y_value)

                min_acceleration_y_value = min(group_accelerations, key=lambda x: x[2])[2]
                min_acceleration_y.append(min_acceleration_y_value)

                group_jerks = jerks[-30:]
                max_jerk_y_value = max(group_jerks, key=lambda x: x[2])[2]
                max_jerk_y.append(max_jerk_y_value)

                min_jerk_y_value = min(group_jerks, key=lambda x: x[2])[2]
                min_jerk_y.append(min_jerk_y_value)

            if len(accelerations) >= window_size:
                acceleration_window = accelerations[-window_size:]
                avg_acceleration_y = sum(item[2] for item in acceleration_window) / window_size

                moving_averages.append(avg_acceleration_y)

    # Write the extracted features to the result file
    with open(result_file_path, 'w', newline='') as result_file:
        csv_writer = csv.writer(result_file)

        # Write the header row
        csv_writer.writerow([
            'Max Velocity Y', 'Min Velocity Y', 'Max Acceleration Y', 'Min Acceleration Y',
            'Start Acceleration Y', 'End Acceleration Y', 'Max Jerk Y', 'Min Jerk Y'
        ])

        # Write the extracted feature data
        for i in range(len(max_acceleration_y)):
            feature_row = [
                max_velocity_y[i], min_velocity_y[i], max_acceleration_y[i], min_acceleration_y[i],
                start_accelerations_y[i], end_accelerations_y[i], max_jerk_y[i], min_jerk_y[i]
            ]
            csv_writer.writerow(feature_row)



# In[2]:


import csv

def btc_extract_features(input_file_path, result_file_path):
    window_size = 30

    moving_averages = []  

    positions = []
    velocities = []
    accelerations = []
    jerks = []

    max_velocity_y = []
    min_velocity_y = []
    max_acceleration_y = []
    min_acceleration_y = []
    start_accelerations_y = []
    end_accelerations_y = []
    max_jerk_y = []
    min_jerk_y = []

    with open(input_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)  # Skip the header row

        prev_frame_number = None
        prev_position_x = None
        prev_position_y = None
        prev_velocity_x = None
        prev_velocity_y = None
        acceleration_x = 0.0  # Initialize acceleration_x
        acceleration_y = 0.0  # Initialize acceleration_y
        prev_acceleration_x = None
        prev_acceleration_y = None
        prev_jerk_x = None
        prev_jerk_y = None
        jerk_x = 0.0  # Initialize jerk_x
        jerk_y = 0.0  # Initialize jerk_y

        for row in csv_reader:
            frame_number = int(row[0])
            position_x = float(row[1])
            position_y = float(row[2])

            velocity_x = 0.0  # Initialize velocity_x
            velocity_y = 0.0  # Initialize velocity_y

            if prev_frame_number is not None:
                time_interval = frame_number - prev_frame_number

                if time_interval != 0:
                    velocity_x = (position_x - prev_position_x) / time_interval
                    velocity_y = (position_y - prev_position_y) / time_interval
                    velocities.append((frame_number, velocity_x, velocity_y))

                    acceleration_x = (velocity_x - prev_velocity_x) / time_interval
                    acceleration_y = (velocity_y - prev_velocity_y) / time_interval
                    accelerations.append((frame_number, acceleration_x, acceleration_y))

                    jerk_x = (acceleration_x - prev_acceleration_x) / time_interval
                    jerk_y = (acceleration_y - prev_acceleration_y) / time_interval
                    jerks.append((frame_number, jerk_x, jerk_y))

            prev_frame_number = frame_number
            prev_position_x = position_x
            prev_position_y = position_y
            prev_velocity_x = velocity_x
            prev_velocity_y = velocity_y
            prev_acceleration_x = acceleration_x
            prev_acceleration_y = acceleration_y
            prev_jerk_x = jerk_x
            prev_jerk_y = jerk_y

            if len(accelerations) >= 30:
                group_velocities = velocities[-30:]
                max_velocity_y_value = max(group_velocities, key=lambda x: x[2])[2]
                max_velocity_y.append(max_velocity_y_value)

                min_velocity_y_value = min(group_velocities, key=lambda x: x[2])[2]
                min_velocity_y.append(min_velocity_y_value)

                group_accelerations = accelerations[-30:]
                max_acceleration_y_value = max(group_accelerations, key=lambda x: x[2])[2]
                max_acceleration_y.append(max_acceleration_y_value)

                start_accelerations_y_value = group_accelerations[0][2]
                start_accelerations_y.append(start_accelerations_y_value)

                end_accelerations_y_value = group_accelerations[-1][2]
                end_accelerations_y.append(end_accelerations_y_value)

                min_acceleration_y_value = min(group_accelerations, key=lambda x: x[2])[2]
                min_acceleration_y.append(min_acceleration_y_value)

                group_jerks = jerks[-30:]
                max_jerk_y_value = max(group_jerks, key=lambda x: x[2])[2]
                max_jerk_y.append(max_jerk_y_value)

                min_jerk_y_value = min(group_jerks, key=lambda x: x[2])[2]
                min_jerk_y.append(min_jerk_y_value)

            if len(accelerations) >= window_size:
                acceleration_window = accelerations[-window_size:]
                avg_acceleration_y = sum(item[2] for item in acceleration_window) / window_size

                moving_averages.append(avg_acceleration_y)
                
    X = []
    for i in range(len(max_acceleration_y)):
        x_data = [start_accelerations_y[i], end_accelerations_y[i], max_jerk_y[i], min_jerk_y[i]]
        X.append(x_data)
        
    # Save the extracted features to the result_file_path
    with open(result_file_path, 'w', newline='') as result_file:
        csv_writer = csv.writer(result_file)
        
        # Write the header row
        csv_writer.writerow(['Start Acceleration Y', 'End Acceleration Y', 'Max Jerk Y', 'Min Jerk Y'])
        
        # Write the data
        for x_data in X:
            csv_writer.writerow(x_data)


# In[ ]:


# Example usage of the function
input_file_path = './input/original_coordinates.csv'
result_file_path = './input/features.csv'
btc_extract_features(input_file_path, result_file_path)


# In[3]:


get_ipython().system('jupyter nbconvert --to python btc_feature_extractor.ipynb')


# In[1]:


import os
print(os.getcwd())  # Print the current working directory


# In[ ]:




