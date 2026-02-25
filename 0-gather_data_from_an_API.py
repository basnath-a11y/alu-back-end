#!/usr/bin/python3
"""0-gather_data_from_an_API.py
Fetch TODO list progress for a given employee id from JSONPlaceholder API.
"""
import json
import sys
import urllib.request


def fetch_json(url):
	with urllib.request.urlopen(url) as resp:
		return json.load(resp)


def main():
	if len(sys.argv) != 2:
		return
	try:
		user_id = int(sys.argv[1])
	except Exception:
		return
	user = fetch_json('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
	todos = fetch_json('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
	name = user.get('name')
	completed = [t for t in todos if t.get('completed') is True]
	print('Employee {} is done with tasks({}/{}):'.format(name, len(completed), len(todos)))
	for task in completed:
		print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
	main()

#!/usr/bin/python3
"""0-gather_data_from_an_API.py
Fetch TODO list progress for a given employee id from JSONPlaceholder API.
"""
import json
import sys
import urllib.request


def fetch_json(url):
	with urllib.request.urlopen(url) as resp:
		return json.load(resp)


def main():
	if len(sys.argv) != 2:
		return
	try:
		user_id = int(sys.argv[1])
	except Exception:
		return
	user = fetch_json('https://jsonplaceholder.typicode.com/users/{}'.format(user_id))
	todos = fetch_json('https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
	name = user.get('name')
	completed = [t for t in todos if t.get('completed') is True]
	print('Employee {} is done with tasks({}/{}):'.format(name, len(completed), len(todos)))
	for task in completed:
		print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
	main()

