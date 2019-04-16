import yaml
import os

class Config:
	def __init__(self):
		self.cached = 0
		self.file="config.yaml"
		self.config = {}

	def getConfig(self):
		stamp = os.stat(self.file).st_mtime
		if stamp != self.cached:
			self.cached = stamp
			f = open(self.file)
			self.config = yaml.safe_load(f)
			f.close()
			return self.config
		return self.config