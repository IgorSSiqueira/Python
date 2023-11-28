# %%
from abc import ABC, abstractmethod
from string import Formatter


class Logger(ABC):
    def header(self, **args):
        self.log_argument = args

    @abstractmethod
    def log(self, **args):
        pass

class FormatterLogger(Logger):
    ...

class PrintLogger(FormatterLogger):
    # def header(self, **args):
    #     super().header(**args)
    #     self.log(**args)

    # def log(self, **args):
    #     out = "| "
    #     for k, v in args.items():
    #         out += str(v).rjust(6)
    #         out += " | "
    #     print(out)


class NullLogger(Logger):
    def log(self, **args):
        pass


class FileLogger(FormatterLogger):
    def __init__(self, filepath):
        self.filepath = filepath

    # def header(self, **args):
    #     super().header(**args)
    #     self.log(**args)

    # def log(self, **args):
    #     out = "| "
    #     for k, v in args.items():
    #         out += str(v).rjust(6)
    #         out += " | "
    #     with open(self.filepath, "a") as f:
    #         f.write(out)
    #         f.write("\n")


# Create a abstract class logger that creates formatter loggers
# 1. PrintLogger and FileLogger should inherit from this class

# %%
# My code
import math


def bissection(f, a, b, logger=NullLogger()):
    fa = f(a)
    fb = f(b)
    if fa * fb >= 0:
        raise Exception("Interval needs to change f changing sign")
    x = (a + b) / 2
    fx = f(x)
    close_to_zero = math.fabs(fx) < 1e-6
    small_interval = b - a < 1e-6
    time_to_stop = close_to_zero or small_interval

    logger.header(x="x", fx="f(x)")
    logger.log(x=x, fx=fx)

    while not time_to_stop:
        if fa * fx < 0:
            b = x
            fb = fx
        else:
            a = x
            fa = fx

        x = (a + b) / 2
        fx = f(x)
        close_to_zero = math.fabs(fx) < 1e-6
        small_interval = b - a < 1e-6
        time_to_stop = close_to_zero or small_interval

        logger.log(x=x, fx=fx)

    return x


# %%