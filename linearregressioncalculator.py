import numpy as np

# data input provision

X = []
y = []

# array allowing  for infinite variables to be calculated

num_inputs = int(input("Enter the number of data points: "))
for i in range(num_inputs):
    x_value = float(input(f"Enter X{i+1}: "))
    y_value = float(input(f"Enter y{i+1}: "))
    X.append(x_value)
    y.append(y_value)

X = np.array(X)
y = np.array(y)

# Calculating the mean of X and y

mean_x = np.mean(X)
mean_y = np.mean(y)

# Calculating the difference and product of each data point with the means
diff_x = X - mean_x
diff_y = y - mean_y
prod = diff_x * diff_y

# Calculating the sum of squared differences
ssd_x = np.sum(diff_x ** 2)

# Calculating the regression coefficients
slope = np.sum(prod) / ssd_x
intercept = mean_y - (slope * mean_x)

# Printing the calculated coefficients
print("Intercept:", intercept)
print("Slope:", slope)

# linear regression prediction
num_predictions = int(input("Enter the number of predictions: "))
X_new = []
for i in range(num_predictions):
    value = float(input(f"Enter X{i+1} for prediction: "))
    X_new.append(value)

X_new = np.array(X_new)
predictions = intercept + slope * X_new

# Print the predictions
print("Predictions:", predictions)
