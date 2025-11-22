import csv
import numpy as np

base_file = 'dataset/data_train.csv'
compare_file = 'dataset/output_train_data.csv'

def verify():
	with open(compare_file, 'r') as file:
		reader = csv.reader(file)
		for value in reader:
			theta0 = float(value[0])
			theta1 = float(value[1])
			km_mean = float(value[2])
			km_std = float(value[3])

	with open(base_file, 'r') as file:
		reader = csv.reader(file)

		price = []
		km = []

		next(reader)
		for row in reader:
			price.append(float(row[1]))
			km.append(float(row[0]))

		km_mean = np.mean(km)
		km_normalized = (km - km_mean) / km_std
		# km_std = np.std(km)
		price = np.array(price)
		price_mean = np.mean(price)

		prediction = theta0 + theta1 * km_normalized
		error = np.abs(prediction - price)
		
		mean_absolute_error = np.mean(error)
		return round((mean_absolute_error / price_mean * 100), 1)