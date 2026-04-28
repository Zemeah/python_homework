import logging
from functools import wraps

# Task 1
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        pos_params = list(args) if args else "none"
        kw_params = dict(kwargs) if kwargs else "none"

        logger.info(f"function: {func.__name__}")
        logger.info(f"positional parameters: {pos_params}")
        logger.info(f"keyword parameters: {kw_params}")
        logger.info(f"return: {result}")
        logger.info("-----")

        return result

    return wrapper


@logger_decorator
def hello_world():
    print("Hello, World!")


@logger_decorator
def positional_args(*args):
    return True


@logger_decorator
def keyword_args(**kwargs):
    return logger_decorator


if __name__ == "__main__":
    hello_world()
    positional_args(1, 2, 3, "test")
    keyword_args(name="Zemeah", age=20)

