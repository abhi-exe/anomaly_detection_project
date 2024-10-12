import matplotlib.pyplot as plt

def plot_data(data_stream, anomalies):
    plt.figure(figsize=(15, 6))
    
    # Plot the entire data stream
    plt.plot(data_stream, label='Data Stream', color='blue', linewidth=1)

    # Highlight anomalies in red
    if anomalies:
        anomaly_indices, anomaly_values = zip(*anomalies)
        plt.scatter(anomaly_indices, anomaly_values, color='red', label='Anomalies', zorder=5)

    # Add title, legend, and labels
    plt.title('Data Stream with Anomaly Detection')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.legend()
    plt.grid(True)
    plt.show()
