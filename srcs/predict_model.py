import csv


def predict(nb_km: float) -> float:
    data_file = "dataset/output_train_data.csv"
    theta0 = 0
    theta1 = 0

    try:
        with open(data_file, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                theta0 = float(row[0])
                theta1 = float(row[1])
                km_mean = float(row[2])
                km_std = float(row[3])

    except Exception as e:
        print(f"Error: Unable to read prediction file: {e}")
        return None

    nb_km_normalized = (float(nb_km) - km_mean) / km_std
    prediction = theta0 + theta1 * nb_km_normalized
    return max(0, round(prediction, 2))
