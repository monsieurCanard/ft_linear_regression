import csv
import numpy as np
import matplotlib.pyplot as plt

train_file = "dataset/data_train.csv"
result_file = "dataset/output_train_data.csv"


def train_loop(theta0, theta1, km: np.array, price: np.array):
    learning_rate = 0.1

    prediction = theta0 + theta1 * km
    error = prediction - price

    tmp_theta0 = learning_rate * (1 / len(km)) * np.sum(error)
    tmp_theta1 = learning_rate * (1 / len(km)) * np.sum(error * km)

    theta0 -= tmp_theta0
    theta1 -= tmp_theta1
    return theta0, theta1


def train(visualize=False):
    price = []
    km = []

    try:
        with open(train_file, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                price.append(float(row[1]))
                km.append(float(row[0]))

    except Exception as e:
        print(f"Error: Unable to read training file: {e}")
        exit(1)

    price = np.array(price)
    km = np.array(km)

    km_mean = np.mean(km)
    km_std = np.std(km)

    km = (km - km_mean) / km_std

    theta1 = 0
    theta0 = 0
    for i in range(0, 10000):
        theta0, theta1 = train_loop(theta0, theta1, km, price)

    try:
        with open(result_file, "w") as file:
            writer = csv.writer(file)
            writer.writerow([theta0, theta1, km_mean, km_std])
    except Exception as e:
        print(f"Error: Unable to write result file: {e}")
        exit(1)

    if visualize:
        plt.title("Linear Regression")
        plt.scatter(km, price, color="blue")
        plt.plot(km, theta0 + theta1 * km, color="red")
        plt.legend(["Data", "Regression Line"])
        plt.xlabel("Km (standardized)")
        plt.ylabel("Price")
        plt.show()
