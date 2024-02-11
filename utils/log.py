import functools
import time

class Timer:
  def __init__(self):
    self.start_time = None
    self.end_time = None
    self.elapsed_time = None

  def start(self):
    self.start_time = time.time()

  def stop(self):
    if self.start_time is not None:
      self.end_time = time.time()
      self.elapsed_time = self.end_time - self.start_time

      print(f"Finished in {self.elapsed_time:.2f} seconds")


def timer(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    timer = Timer()
    timer.start()

    res = func(*args, **kwargs)

    timer.stop()

    return res

  return wrapper