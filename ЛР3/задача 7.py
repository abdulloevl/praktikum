
import time

class Timer:
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print("Время выполнения:", end - self.start, "сек")

with Timer():
    for i in range(1_000_000):
        pass

