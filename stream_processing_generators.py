import random

def sensor_stream():
    """Simulate a data stream of sensor readings."""
    while True:
        # Generate a random sensor reading between 0 and 100
        yield random.randint(0, 100)

def moving_average(window_size, data_stream):
    """Calculate the moving average of sensor readings."""
    window = []
    for value in data_stream:
        window.append(value)
        if len(window) > window_size:
            window.pop(0)
        average = sum(window) / len(window)
        yield average

# Create a sensor data stream generator
sensor_data = sensor_stream()

# Calculate moving average of sensor readings
window_size = 5
averages = moving_average(window_size, sensor_data)

# Simulate processing the stream for a certain number of iterations
iterations = 10
for _ in range(iterations):
    print(next(averages))
