
import time

LIMIT_TIME = 5.0

class Timer:
	def __init__(self) -> None:
		self.start_time = None
	
	def start(self) -> None:
		self.start_time = time.time()
	
	def check(self) -> bool:
		now = time.time()
		print('time: ', now - self.start_time)
		if (LIMIT_TIME < now - self.start_time):
			return False
		else:
			return True
