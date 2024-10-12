import random

def data_stream_generator(num_points=1000, anomaly_probability =5):

    data_stream = []

    for _ in range(num_points):
        # Generate a random number between 0 and 100
        if random.randint(0, 100) < anomaly_probability:  # 2% chance of anomaly
            value = random.gauss(100, 5)  # Anomaly with mean 100, std_dev 5
        else:
            value = random.gauss(50, 5)  # Normal data with mean 50, std_dev 5

        data_stream.append(value)

    return data_stream