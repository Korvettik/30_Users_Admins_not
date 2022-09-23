import csv
import json


def csv_to_json(csv_file: str, json_file: str, model: str) -> None:
	with open(csv_file, 'r', encoding='utf-8') as file:
		data = list(csv.reader(file, delimiter=','))

	item = [dict(zip(data[0], line)) for line in data[1:]]

	fixture = []
	for elem in item:
		for k in elem:
			try:
				elem[k] = eval(elem[k].title())
			except (NameError, SyntaxError):
				elem[k] = elem[k]
		fixture.append({
			'model': model,
			'pk': elem['id'],
			'fields': elem
		})

	with open(json_file, 'w', encoding='utf-8') as file:
		json.dump(fixture, file, ensure_ascii=False, indent=2)


csv_to_json(csv_file='datasets/ad.csv', json_file='fixtures/ad.json', model='ad.ad')
csv_to_json(csv_file='datasets/category.csv', json_file='fixtures/category.json', model='category.category')
csv_to_json(csv_file='datasets/location.csv', json_file='fixtures/location.json', model='user.location')
csv_to_json(csv_file='datasets/user.csv', json_file='fixtures/user.json', model='user.user')
