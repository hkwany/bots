import argparse
import threading

from os import system
from http_generator import scheduledoHttpsDownload
from http_generator import scheduledoHttpsUpload
from http_generator import scheduleHttpUpload
from http_generator import scheduleHttpDownload


def main():
	# Prepare arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--url", help="remote url", required=True, nargs='+', default=None)
	parser.add_argument("--token", help="specify your token", required=False, nargs='+', default=None)
	parser.add_argument("--worker", help="specify your worker", type=int, required=True, nargs='+', default=None)
	parser.add_argument("--function", help="specify your function(download/upload)", required=True, nargs='+', default=None)
	parser.add_argument("--upload_file", help="local file to be uploaded", required=False, nargs='+', default='upload_file')
	parser.add_argument("--download_file", help="remote file to be downloaded", required=False, nargs='+', default='download_file')
	parser.add_argument("--protocol", help="specify your protocol(http/https)", required=True, nargs='+', default=None)

	args = parser.parse_args()
	# print(args)
	# print(type(args.filename[0]))
	# print(type(args.url[0]))
	# print(type(args.token[0]))
	# print(type(args.worker[0]))
	if args.protocol[0] == 'http':
		if args.function[0] == 'upload':
			scheduleHttpUpload(args)
		elif args.function[0] == 'download':
			scheduleHttpDownload(args)
	elif args.protocol[0] == 'https':
		if args.function[0] == 'upload':
			scheduledoHttpsUpload(args)
		elif args.function[0] == 'download':
			scheduleHttpsDownload(args)
	else:
		parser.print_help()

	# # Use Scapy Interactive Console
	# if args.interactive:
	#     system("scapy")
	#
	# if args.target is not None and args.target_port is not None:
	#     scheduleSynFlood(args)
	# else:
	#     parser.print_help()


if __name__ == '__main__':
	main()
