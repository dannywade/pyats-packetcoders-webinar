from pyats import aetest
import logging

logger = logging.getLogger("pyats.aetest")


class Testcase(aetest.Testcase):
    pass


class TestcaseTwo(aetest.Testcase):
    pass


class TestcaseThree(aetest.Testcase):
    pass


if __name__ == "__main__":
    # Randomize testcase execution order
    aetest.main(random=True)
