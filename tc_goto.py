from pyats import aetest
import logging

logger = logging.getLogger("pyats.aetest")


class Testcase(aetest.Testcase):
    pass


class TestcaseOne(aetest.Testcase):

    @aetest.test
    def test_one(self):
        logger.info("Testcase 2 - Test One running...")
        # Testcase fails and jumps to testcase cleanup section
        self.failed("Test failed.", goto=["cleanup"])

    @aetest.test
    def test_two(self):
        # Will be blocked because of test_one failing and jumping to cleanup section
        pass

    @aetest.test
    def test_three(self):
        # Will be blocked because of test_one failing and jumping to cleanup section
        pass

    @aetest.test
    def test_four(self):
        # Will be blocked because of test_one failing and jumping to cleanup section
        pass

    @aetest.test
    def test_five(self):
        # Will be blocked because of test_one failing and jumping to cleanup section
        pass

    @aetest.test
    def test_six(self):
        # Will be blocked because of test_one failing and jumping to cleanup section
        pass

    @aetest.cleanup
    def cleanup(self):
        # will be skipped because of test_three
        pass

class TestcaseThree(aetest.Testcase):
    pass

if __name__ == "__main__":
    aetest.main()