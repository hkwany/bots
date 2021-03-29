# from scapy.all import IP, TCP, send

from threading import Thread
import time
import requests


def scheduleHttpUpload(args):
	jobs = []
	for i in range(1, args.worker[0] + 1):
		params = {
			'url': args.url[0],
			'upload_file': args.upload_file[0]
		}

		jobs.append(Thread(target=doHttpUpload(params),
		                   name=(f"Upload #{i}")))

	print(f"Starting all {len(jobs)} upload(s)....")
	for job in jobs:  # Start all job threads
		job.start()

def scheduleHttpDownload(args):
	jobs = []
	for i in range(1, args.worker[0] + 1):
		params = {
			'url': args.url[0],
			'download_file': args.download_file[0]
		}

		jobs.append(Thread(target=doHttpDownload(params),
		                   name=(f"Download #{i}")))

	print(f"Starting all {len(jobs)} download(s)....")
	for job in jobs:  # Start all job threads
		job.start()

def scheduledoHttpsUpload(args):
	jobs = []
	for i in range(1, args.worker[0] + 1):
		params = {
			'url': args.url[0],
			'upload_file': args.upload_file[0],
			'token': args.token[0]
		}

		jobs.append(Thread(target=doHttpsUpload(params),
		                   name=(f"Upload #{i}")))

	print(f"Starting all {len(jobs)} upload(s)....")
	for job in jobs:  # Start all job threads
		job.start()
	pass

def scheduledoHttpsDownload(args):
	jobs = []
	for i in range(1, args.worker[0] + 1):
		params = {
			'url': args.url[0],
			'download_file': args.download_file[0],
			'token': args.token[0]
		}

		jobs.append(Thread(target=doHttpsDownload(params),
		                   name=(f"Download #{i}")))

	print(f"Starting all {len(jobs)} download(s)....")
	for job in jobs:  # Start all job threads
		job.start()

def doHttpUpload(params):
	files = {'upload_file': open(params['upload_file'], 'rb')}
	print("uploading to")
	print(params['url'])
	with requests.post(params['url'], stream=True, files=files) as r:
		r.raise_for_status()
		print(r.text)
		print(r.status_code)

def doHttpDownload(params):
	local_file_name = params['download_file'] + str(time.time())
	print("Downloading from:")
	print(params['url'] + '/' + params['download_file'])
	with requests.get(params['url'] + '/' + params['download_file'], stream=True) as r:
		r.raise_for_status()
		with open(local_file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)
                
def doHttpsUpload(params):
	files = {'upload_file': open(params['upload_file'], 'rb')}
	print("uploading to")
	print(params['url'])
	with requests.post(params['url'], stream=True, files=files) as r:
		r.raise_for_status()
		print(r.text)

def doHttpsDownload(params):
	local_file_name = params['download_file'] + str(time.time())
	print("Downloading from:")
	print(params['url'] + '/' + params['download_file'] + '?token=' + params['token'])
	with requests.get(params['url'] + '/' + params['download_file'] + '?token=' + params['token'], stream=True) as r:
		r.raise_for_status()
		with open(local_file_name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				f.write(chunk)


