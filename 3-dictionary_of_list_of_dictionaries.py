#!/usr/bin/python3
"""3-dictionary_of_list_of_dictionaries.py
Export all todos for all employees into todo_all_employees.json.
"""
import json
import urllib.request


def fetch_json(url):
	with urllib.request.urlopen(url) as resp:
		return json.load(resp)


def main():
	users = fetch_json('https://jsonplaceholder.typicode.com/users')
	todos = fetch_json('https://jsonplaceholder.typicode.com/todos')
	users_map = {u.get('id'): u.get('username') for u in users}
	out = {}
	for t in todos:
		uid = str(t.get('userId'))
		out.setdefault(uid, [])
		out[uid].append({
			'username': users_map.get(t.get('userId')),
			'task': t.get('title'),
			'completed': t.get('completed')
		})
	with open('todo_all_employees.json', 'w', encoding='utf-8') as f:
		json.dump(out, f)


if __name__ == "__main__":
	main()

