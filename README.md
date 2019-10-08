# Real_Time_Stress_Assessment

## Introduction
Wearable devices are very common in our life nowadays such as Apple watch, and Samsung galaxy gear. The characteristic of wearable devices enables them to collect and exchange data between devices or platforms automatically. In terms of the application of wearable devices in health, there is still room for development. The advantage of wearable devices is that it can easily and automatically collect data, such as heart rate, body temperature, and physical information. However, current wearable devices such as Apple Watch are mainly used for information. They don’t analyze or make conclusions based on those data. Today, there is a growing interest to use wearables not only for individual self-tracking but also within corporate health and wellness programs.

## Data
The dataset is obtained from UCI, Wearable Stress and Affect Detection (https://archive.ics.uci.edu/ml/datasets/WESAD+%28Wearable+Stress+and+Affect+Detection%29#).
It contains 15 subjects (people), and each person’s data size is around 1GB. The total size of our raw data is 17.84GB.  The label of the data (ground-truth) is from self-report of the subjects.

## Technical Details
The first step is data preprocessing. We process the data and split the data into two data set before feed them into the model. One for training and the other one for testing. The second step is building the model, we train our data in Spark, using the random forest. In the third step, we build a streaming system. There are three python files in the system, Streaming Data, Producer, and Consumer. The Streaming Data file reads from the processed data set and sends data to the producer. The Producer file sends data to Kafka at the same rate of every 5 seconds. The Consumer file extracts data from Kafka and uses the model to detect the stress level of users. The last step is to display the result on the web page for information. 

![technical](https://github.com/jingan0514/Real_Time_Stress_Assessment/blob/master/images/Streaming.png)

## Machine Learning Model
Based on the analysis, random forest and AdaBoost are suitable for this task. Since the random forest multiclass classification algorithm is already implemented in Spark Machine Learning Library and easier to use for our system, we choose random forest as our  model/

## Result
Here is the screenshot of the system:

![screenshot](https://github.com/jingan0514/Real_Time_Stress_Assessment/blob/master/images/Real-time%20Stress%20Assessment.png)
