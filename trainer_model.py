import csv
import numpy as np
import matplotlib.pyplot as plt

train_file = 'dataset/data_train.csv'
result_file = 'dataset/output_train_data.csv'

def train(theta0, theta1, km, price):
	learning_rate = 0.01
	prediction = theta0 + theta1 * km
	error = prediction - price
	tmp_theta0 = learning_rate * (1/len(km)) * np.sum(error)
	tmp_theta1 = learning_rate * (1/len(km)) * np.sum(error * km)
	
	theta0 -= tmp_theta0
	theta1 -= tmp_theta1
	return theta0, theta1

with open(train_file, 'r') as file:
	reader = csv.reader(file)

	price = []
	km = []

	next(reader)
	for row in reader:
		price.append(float(row[1]))
		km.append(float(row[0]))
	
	price = np.array(price)
	km = np.array(km)
	km_mean = np.mean(km)
	km_std = np.std(km)
	km = (km - km_mean) / km_std
	
	# Initialize theta0 and theta1 at Zero ! MANDATORY
	theta1 = 0
	theta0 = 0
	for i in range(0, 100000):
		theta0, theta1 = train(theta0, theta1, km, price)
	
	with open (result_file, 'w') as file:
		writer = csv.writer(file)
		writer.writerow([theta0, theta1, km_mean, km_std])
	
	plt.scatter(price, km, color='blue')
	plt.plot(theta0 + theta1 * km, km, color='red')
	plt.legend(['Data', 'Regression'])
	plt.xlabel('Price')
	plt.ylabel('Km (standardized)')
	plt.show()