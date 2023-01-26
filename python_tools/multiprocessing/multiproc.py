"""
Multiprocessing tutorial
"""

import logging
import multiprocessing
from multiprocessing import process
import time


def run(num):
    """
    Process
    """
    name = process.current_process().name
    logging.info(f"Running {name} as {__name__}")
    time.sleep(num * 2)
    logging.info(f"Finished {name}")


def main():
    """
    main
    """
    name = process.current_process().name
    logging.info(f"Running {name} as {__name__}")

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run, args=[x], daemon=True)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    logging.info(f"Finished {name}")


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
if __name__ == "__main__":
    main()
