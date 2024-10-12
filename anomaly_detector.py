import numpy as np

class StreamingStats:
    def __init__(self):
        self.mean = 0.0  # Current mean of the stream
        self.m2_sum = 0.0  # Sum of squared differences from the mean
        self.count = 0  # Number of elements processed

    def update_stats(self, new_value):
        self.count += 1
        delta = new_value - self.mean
        self.mean += delta / self.count
        delta2 = new_value - self.mean
        self.m2_sum += delta * delta2

    def get_variance(self):
        if self.count < 2:
            return float('nan')  # Not enough data to compute variance
        return self.m2_sum / (self.count - 1)  # Unbiased variance estimate

def z_score(value, mean, variance):
    stddev = np.sqrt(variance) if variance > 0 else 1e-9
    return (value - mean) / stddev

def anomaly_detector(data_stream, threshold=3):
    stats = StreamingStats()
    anomalies =[]

    for index, value in enumerate(data_stream):
        variance = stats.get_variance()
        score = z_score(value, stats.mean, variance)

        if abs(score) > threshold:
            print(f"Outlier detected at index {index}: value={value}, Z-score={score}")
            anomalies.append((index, value))

        stats.update_stats(value)
    return anomalies