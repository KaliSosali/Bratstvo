import json, sys

class Config:
	def __init__(self, filename):
		try:
			with open(filename, 'r') as cfg:
				self.data = json.load(cfg, strict=False)
		except FileNotFoundError:
			print(f"No config finded({filename}).")
			sys.exit(1)

	def get(self, name):
		try:
			return self.data[name]
		except KeyError:
			print(f"KeyError: {name}")
			sys.exit(1)

