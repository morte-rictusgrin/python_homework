# Task 1: Writing and Testing a Decorator
import logging

logger = logging.getLogger(__name__ + " _parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))


def logger_decorator(func):
    def func_logger(*args, **kwargs):
        value = func(*args, **kwargs)
        log_message = f"function: {func.__name__}\npositional parametes: {list(args) if args else "None"}\nkeyword parameters: {kwargs if kwargs else "None"}\nreturn: {value}"
        logger.info(log_message)
        return value
    return func_logger


@logger_decorator
def hello():
    print("Hello!")
    return "hello executed"

hello()

@logger_decorator
def positional(*args):
    message = ""
    for arg in args: 
        message = message + str(arg) + " "
    message = message.strip()
    print(message)
    return "True"


positional("Bally Jerry", "pranged", "his kite", "caught his can in the Bertie")

@logger_decorator
def keywords(**kwargs):
    message_2 = ""
    for key, value in kwargs.items():
        message_2 = message_2 + str(key) + ":" + " " + str(value) + ";" + " "
    message_2 = message_2.strip(";")
    print(message_2)
    return "logger_decorator" 

keywords(name="Bob", action = "listens")
        

