import time
from contextlib import contextmanager

# Реализация на основе класса
class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"time: {time.time() - self.start_time}")

# Реализация с использованием contextlib
@contextmanager
def cm_timer_2():
    start_time = time.time()
    yield
    print(f"time: {time.time() - start_time}")



with cm_timer_1():
    time.sleep(5.5)

with cm_timer_2():
    time.sleep(5.5)