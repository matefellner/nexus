"""
Future for multithreading
"""


import logging
import time
import threading
import random
from concurrent.futures import ThreadPoolExecutor


workers = 5


def test_future(name):
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    time.sleep(random.randrange(1, 5))
    logging.info(f"Finished: {threadname}")
    ret = f"Hello {name} your random number is: {str(random.randrange(1,100))}"
    return ret


def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1, 5)
            future = ex.submit(test_future, "Mate-" + str(x))
            ret.append(future)
    logging.info("Do something in the main thread")
    for r in ret:
        logging.info(f"Returned: {r.result()}")


def main():
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
    logging.info("App start")
    pooled()


if __name__ == "__main__":
    main()
