Hey! This is a project for anomaly detection intended as a research project for my application for a Graduate Software Engineer at Cobblestone Energy.

There are 6 files in this project.
data_stream_generator.py
anomaly_detector.py
plot_data.py
main.py
README.md
requirements.txt

In order to run this project, first you need to install the required python packages from requirements.txt, and then run main.py.

data_stream_generator -> This file contains the function to generate data stream, which takes two inputs, number of points, probability of having an anomaly, and returns an array of the data points.

anomaly_detector.py -> This approach of detection of anomaly is inspired from this research article https://towardsdatascience.com/easy-outlier-detection-in-data-streams-3089bfefe528 , where the author follows this.
1. First assume the mean and std dev to be 0.
2. Whenever a data point comes in we first check if it falls in the std dev within our mean, if not we declare it as an outlier.
3. We update our mean and std dev with reference to our latest entry point.

My optimization - Instead of just taking the mean and the standard deviation, a much better approach is to calculate the z-score, which basically measures how many standard deviations far our current value is from mean. Since in a normal distribution, 99.7% of the values lie atmost 3 standard deviations, any value lying outside it is declared as an anomaly.

plot_data.py -> This file contains the function to visualize the data stream using a matplotlib graph.

main.py -> It has the code to run the project.
