#!/usr/bin/python3
"""
Fetch TODO list progress for a given employee id from JSONPlaceholder API.
"""
import json
import sys
import urllib.request


def fetch_json(url):
	"""Fetch JSON data from a given URL."""
	with urllib.request.urlopen(url) as resp:
		return json.load(resp)


def main():
	"""Main function to display employee TODO progress."""
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

