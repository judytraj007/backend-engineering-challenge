import click

@click.command()
@click.option('--input_file', help='json file containing stream data to calculate moving average.', required=True)
@click.option('--window_size', help='size of the window for which the average is to be calculated.', required=True)
def parse_input(input_file, window_size):
	'''
	Entry point to the moving average calculation app.
	'''
	pass