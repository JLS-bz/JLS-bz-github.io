# this converts a zst files to csv

# argument is a txt file containing subreddit names
# call this like
# python to_csv.py mentalhealth_SUBS.txt

import zstandard
import os
import json
import sys
import csv
from datetime import datetime
import logging.handlers


log = logging.getLogger("bot")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())


def read_and_decode(reader, chunk_size, max_window_size, previous_chunk=None, bytes_read=0):
	chunk = reader.read(chunk_size)
	bytes_read += chunk_size
	if previous_chunk is not None:
		chunk = previous_chunk + chunk
	try:
		return chunk.decode()
	except UnicodeDecodeError:
		if bytes_read > max_window_size:
			raise UnicodeError(f"Unable to decode frame after reading {bytes_read:,} bytes")
		return read_and_decode(reader, chunk_size, max_window_size, chunk, bytes_read)


def read_lines_zst(file_name):
	with open(file_name, 'rb') as file_handle:
		buffer = ''
		reader = zstandard.ZstdDecompressor(max_window_size=2**31).stream_reader(file_handle)
		while True:
			chunk = read_and_decode(reader, 2**27, (2**29) * 2)
			if not chunk:
				break
			lines = (buffer + chunk).split("\n")

			for line in lines[:-1]:
				yield line, file_handle.tell()

			buffer = lines[-1]
		reader.close()

def filter_and_process_ndjson(file_name, fields, writer):
    for line in read_lines_zst(file_name):
        if isinstance(line, tuple):
            line = line[0]
        data = json.loads(line)
        filtered_data = {field: data[field] for field in fields if field in data}
        post = filtered_data.get('title', '') + '' + filtered_data.get('selftext', '')
        filtered_data['post'] = post
        filtered_data.pop('title', None)
        filtered_data.pop('selftext', None)
        writer.writerow(filtered_data)

def read_and_process_files(folders, file_list, fields, cols):
    output_file_name = file_list.replace("_SUBS.txt", "_combined")
    with open(file_list) as file_names_file:
        file_list = [line.strip().split(',') for line in file_names_file.readlines()]
        file_list = [item.strip() for sublist in file_list for item in sublist]

    with open(f"Datasets/{output_file_name}.csv", "w", newline="") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=cols)
        writer.writeheader()
        for folder in folders:
            for file_name in file_list:
                file = f'{folder}/{file_name}_submissions.zst'
                try:
                    filter_and_process_ndjson(file, fields, writer)
                except FileNotFoundError:
                    # Skip over the missing file
                    continue


if __name__ == "__main__":
	input_file_path = sys.argv[1]
	fields = ['subreddit','title','selftext','score','num_comments','created_utc']
	cols = ['subreddit', 'post','score','num_comments','created_utc']
	folders = ['Datasets/P1Clean', 'Datasets/P2Clean', 'Datasets/P3Clean', 'Datasets/P4Clean', 'Datasets/P5Clean']
	read_and_process_files(folders, input_file_path, fields, cols)

	
