from pyats import aetest
import logging

logger = logging.getLogger("pyats.aetest")


class TestcaseOne(aetest.Testcase):
    # Must pass testcases will jump to CommonCleanup if they fail
    must_pass = True
    logger.info("This testcase must pass, or else...")

    @aetest.test
    def test(self):
        self.failed("Uh-oh... we ran into a problem!")


class TestcaseTwo(aetest.Testcase):
    logger.info("Testcase two executing...")
    pass


class CommonCleanup(aetest.CommonCleanup):
    @aetest.subsection
    def subsection(self):
        logger.info("Cleaning up testing...")
        pass


if __name__ == "__main__":
    aetest.main()
