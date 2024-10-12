import plot_data
import data_stream_generator
import anomaly_detector

data_stream = data_stream_generator.data_stream_generator()
anomalies = anomaly_detector.anomaly_detector(data_stream= data_stream)
plot_data.plot_data(data_stream=data_stream, anomalies=anomalies)
