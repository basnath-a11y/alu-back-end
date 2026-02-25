#!/usr/bin/python3
"""2-export_to_JSON.py
Export all tasks for a given employee to JSON (USER_ID.json).
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
	username = user.get('username')
	data = {str(user_id): []}
	for t in todos:
		data[str(user_id)].append({
			'task': t.get('title'),
			'completed': t.get('completed'),
			'username': username
		})
	with open('{}.json'.format(user_id), 'w', encoding='utf-8') as f:
		json.dump(data, f)


if __name__ == "__main__":
	main()

