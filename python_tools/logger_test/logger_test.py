"""
Test script for logger
"""

import sys

from logger import logger

if __name__ == "__main__":
    logger.debug("Program started.")
    try:
        ticker = sys.argv[1]
        logger.info(f"Will find summary for {ticker}.")
        logger.debug("Program ended with success.")
    except BaseException:
        logger.error("Error happened!", exc_info=True)
