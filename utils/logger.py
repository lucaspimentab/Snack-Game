import logging

logging.basicConfig(
    level   = logging.INFO,
    format  = '[%(levelname)s] %(asctime)s - %(message)s',
    datefmt = '%H:%M:%S'
)

logger = logging.getLogger("SnakeGame")
