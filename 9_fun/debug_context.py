import logging
from contextlib import contextmanager

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())

logger.setLevel(logging.INFO)


@contextmanager
def debug_context():
    level = logger.level
    try:
        logger.setLevel(logging.DEBUG)
        yield
    finally:
        logger.setLevel(level)


def main():
    logger.info('Before: info log')
    logger.debug('Before: debug log')

    with debug_context():
        logger.info('inside the block: info log')
        logger.debug('inside the block debug log')

    logger.info('after: info log')
    logger.debug('after: debug log')


if __name__ == '__main__':
    main()
