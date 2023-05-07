import serial
import argparse

# Function to calculate the moving average
def moving_average(data, window_size):
    if len(data) < window_size:
        return sum(data) / len(data)
    else:
        return sum(data[-window_size:]) / window_size

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--port', help='Serial port to read from')
args = parser.parse_args()

# Initialize lists to store probabilities
prob_ambulance_values = []
prob_firetruck_values = []
prob_traffic_values = []

# Connect to the Arduino via serial port
ser = serial.Serial(args.port, 9600)

while True:
    try:
        # Read a line from the serial port
        line = ser.readline().decode().strip()
        
        # Check if the line contains the expected probability values
        if ',' in line:
            # Extract probability values as floats
            values = line.split(',')
            if len(values) == 3:
                try:
                    prob_ambulance = float(values[0])
                    prob_firetruck = float(values[1])
                    prob_traffic = float(values[2])
                    
                    # Add probabilities to the lists
                    prob_ambulance_values.append(prob_ambulance)
                    prob_firetruck_values.append(prob_firetruck)
                    prob_traffic_values.append(prob_traffic)
                    
                    # Calculate moving averages
                    window_size = 10
                    prob_ambulance_avg = moving_average(prob_ambulance_values, window_size)
                    prob_firetruck_avg = moving_average(prob_firetruck_values, window_size)
                    prob_traffic_avg = moving_average(prob_traffic_values, window_size)
                    
                    # Print raw values and moving averages as percentage values
                    print(f"Raw: Ambulance: {prob_ambulance*100:3.1f}%  |  Firetruck: {prob_firetruck*100:3.1f}%  |  Traffic: {prob_traffic*100:3.1f}% || Avg: Ambulance: {prob_ambulance_avg*100:3.1f}%  |  Firetruck: {prob_firetruck_avg*100:3.1f}%  |  Traffic: {prob_traffic_avg*100:3.1f}%", end="\r")
                    
                except ValueError:
                    pass

    except KeyboardInterrupt:
        # Close the serial connection and exit
        ser.close()
        break
