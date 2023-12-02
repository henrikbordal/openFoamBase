import matplotlib.pyplot as plt
import pandas as pd
import os

# Function to read and parse the data file
def read_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Extracting data lines (skipping the initial header lines)
    data_lines = [line.strip() for line in lines if line[0].isdigit()]

    # Parsing the data
    data = {'Time': []}
    for i in range(3):  # for each location
        data[f'Location_{i}_hL'] = []

    for line in data_lines:
        values = line.split()
        data['Time'].append(float(values[0]))
        for i in range(3):  # for each location
            data[f'Location_{i}_hL'].append(float(values[2 + 2 * i]))

    return pd.DataFrame(data)


# Function to plot the data
def plot_data(df, file_path):
    plt.figure(figsize=(10, 6))

    # Plotting hL for all locations
    for i in range(3):
        plt.plot(df['Time'], df[f'Location_{i}_hL'], label=f'Location {i} hL')
    plt.title('hL for all Locations')
    plt.xlabel('Time')
    plt.ylabel('hL')
    plt.legend()

    
    if os.path.exists(os.path.join(os.getcwd(), 'postProcessing/plots')) is False:
        os.makedirs(os.path.join(os.getcwd(), 'postProcessing/plots'))

    plt.tight_layout()
    plt.savefig(os.path.join(os.getcwd(), 'postProcessing/plots/height.png'))

# Main function to read and plot the data
def main(file_path):
    df = read_data(file_path)
    plot_data(df, file_path)

# Replace 'height.dat' with your file path
main('postProcessing/interfaceHeight1/0/height.dat')