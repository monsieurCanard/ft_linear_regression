import csv
import numpy as np

with open('train_coef.csv', 'r') as file:
	reader = csv.reader(file)
	for value in reader:
		theta0 = float(value[0])
		theta1 = float(value[1])
		km_mean = float(value[2])
		km_std = float(value[3])

with open('data_train.csv', 'r') as file:
	reader = csv.reader(file)

	price = []
	km = []

	next(reader)
	for row in reader:
		price.append(float(row[1]))
		km.append(float(row[0]))
	km_mean = np.mean(km)
	km_std = np.std(km)
	km = (km - km_mean) / km_std
	price_mean = np.mean(price)

	sum_error = 0
	for i in range(0, len(km)):
		prediction = theta0 + theta1 * km[i]
		error = prediction - price[i]
		sum_error += np.abs(error)
	
	mean_absolute_error = sum_error / len(km)
	print("Your model have a differences of: ", round(mean_absolute_error / price_mean * 100, 1), "% with the real price")