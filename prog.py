from trainer_model import train
from predict_model import predict
from verifyer_model import verify
from interface_prog import prog_header, train_header, predict_header, verify_header


import argparse

def init_argparser():
	parser = argparse.ArgumentParser(
		description="Linear Regression Program",
		usage="prog.py || prog.py [--train] [--verify] [--vizualize] [--predict N]"
	)

	parser.add_argument(
		'--vizualize',
		action='store_true',
		help='Display the regression graph'
	)

	parser.add_argument(
		"--predict",
		type=float,
		help="Predict the price for the given kilometers"
	)

	parser.add_argument(
		'--train',
		action='store_true',
		help='Train the model with the training dataset'
	)

	parser.add_argument(
		'--verify',
		action='store_true',
		help='Verify the model accuracy with the training dataset'
	)

	return parser


def main():
	parser = init_argparser()
	args = parser.parse_args()

	match args:
		case _ if args.train:
			train()
		case _ if args.verify:
			verify()
		case _ if args.predict is not None:
			predicted_price = predict(args.predict)
			print(f"Predicted price for {args.predict} km: {predicted_price} ")
		case _ if args.vizualize:
			train(visualize=True)
			predicted_price = predict( args.predict) if args.predict is not None else None
			if predicted_price is not None:
				print(f"Predicted price for {args.predict} km: {predicted_price} ")
			verify()
		case _:
			run_all_steps()

def run_all_steps():
	prog_header()

	import sys

	line = sys.stdin.readline().strip()
	km = float(line)
	train_header()
	train(visualize=True)
	predicted_price = predict(km)
	predict_header(predicted_price)
	verify_header(verify(), predicted_price, km)


if __name__ == "__main__":
		main()