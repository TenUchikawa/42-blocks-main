
import time

LIMIT_TIME = 4.0

class Timer:
	def __init__(self) -> None:
		self.start_time = None
	
	def start(self) -> None:
		self.start_time = time.time()
	
	def check(self) -> bool:
		now = time.time()
		if (LIMIT_TIME < now - self.start_time):
			return False
		else:
			return True
