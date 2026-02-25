#!/usr/bin/python3
"""1-export_to_CSV.py
Export all tasks for a given employee to CSV (USER_ID.csv).
"""
import csv
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
	filename = '{}.csv'.format(user_id)
	with open(filename, 'w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f, quoting=csv.QUOTE_ALL)
		for t in todos:
			writer.writerow([str(user_id), username, str(t.get('completed')), t.get('title')])


if __name__ == "__main__":
	main()

