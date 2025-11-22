import sys
import csv
import numpy as np

def predict(nb_km: float) -> float:

	data_file = 'dataset/output_train_data.csv'
	theta0 = 0
	theta1 = 0

	with open(data_file, 'r') as file:
		reader = csv.reader(file)
		for row in reader:
			theta0 = float(row[0])
			theta1 = float(row[1])
			km_mean = float(row[2])
			km_std = float(row[3])
		
		nb_km_normalized = (float(nb_km) - km_mean) / km_std
		return round(theta0 + theta1 * nb_km_normalized, 2)