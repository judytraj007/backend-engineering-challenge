import os
import json
import click
from datetime import datetime, timedelta


def validate_file_path(file_path: str):
	''' Check if file exists '''
	if not os.path.isfile(file_path):
		raise FileNotFoundError(f'File path {file_path} does not exist!')


def read_json_file(filename: str) -> list:
	''' Parse json file into a list of dicts '''

	try:
		with open(filename) as file:
			data = [json.loads(line) for line in file]
		return data
	except Exception as e:
		raise e

def cast_timestamp_to_datetime(time_data: list) -> list:
	''' Convert timestamp field to datetime '''

	for entry in time_data:
		entry['timestamp'] = datetime.strptime(entry['timestamp'], '%Y-%m-%d %H:%M:%S.%f')

	return time_data

def get_moving_avg(
	time_data: list,
	window_size: int,
	top_limit_time: datetime) -> float:
	''' Calculate average of duration values within a window '''

	durations = []
	for entry in time_data:
		if (entry['timestamp'] > (top_limit_time - timedelta(minutes=window_size))
				and entry['timestamp'] <= top_limit_time):
			durations.append(entry['duration'])
	avg = 0 if len(durations) == 0 else sum(durations)/len(durations)

	return avg

def calculate_moving_avg(input_file: str, window_size: int):
	''' Processes input file and calculates moving average '''

	input_data = read_json_file(input_file)
	time_data = cast_timestamp_to_datetime(input_data)

	timestamps = [entry['timestamp'] for entry in time_data]
	min_time =  min(timestamps)
	min_time = min_time.replace(second=0, microsecond=0) # set start time to the beginning of the lowest time entry
	max_time =  max(timestamps) + timedelta(minutes=1) # set end time to a minute after the highest time entry

	while min_time <= max_time:
		curr_avg = get_moving_avg(time_data, window_size, min_time)
		print({"date": min_time.strftime('%Y-%m-%d %H:%M:%S'), "average_delivery_time":'%g'%(curr_avg)})
		min_time += timedelta(minutes=1)


@click.command()
@click.option('--input_file', help='json file containing stream data to calculate moving average.', required=True)
@click.option('--window_size', type=int, help='size of the window for which the average is to be calculated.', required=True)
def main(input_file, window_size):
	validate_file_path(input_file)
	calculate_moving_avg(input_file, window_size)




	