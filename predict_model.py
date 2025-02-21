import sys
import csv
import numpy as np

data_file = 'dataset/output_train_data.csv'

if len(sys.argv) < 2:
	print("Usage: python modele.py <Car data kilometrage>")
	sys.exit(1)

nb_km = sys.argv[1]
theta0 = 0
theta1 = 0
with open(data_file, 'r') as file:
	reader = csv.reader(file)
	for value in reader:
		theta0 = float(value[0])
		theta1 = float(value[1])
		km_mean = float(value[2])
		km_std = float(value[3])
	
	nb_km = (float(nb_km) - km_mean) / km_std
	print("Estimated price: ", round(theta0 + (theta1 * float(nb_km)), 2))