from pyats import aetest
import logging

logger = logging.getLogger("pyats.aetest")


# Print section uid
def print_uid(section):
    print("Current section: ", section.uid)


# Print section result
def print_result(section):
    print("Section result: ", section.result)


# Print the exception message and suppress the exception
def print_exception_message(section, exc_type, exc_value, exc_traceback):
    print(f"Exception in test section {section.uid}: {exc_type}, {exc_value}")
    # Returning True will make current section still "pass"
    return True


@aetest.processors(
    pre=[print_uid], post=[print_result], exception=[print_exception_message]
)
class BGPTestcase(aetest.Testcase):
    @aetest.test
    def bgp_test_one(self):
        logger.info("BGP test #1 in progress...")

    @aetest.test
    def bgp_test_two(self):
        logger.info("BGP test #2 in progress...")


@aetest.processors(
    pre=[print_uid], post=[print_result], exception=[print_exception_message]
)
class ExternalConnectivity(aetest.Testcase):
    @aetest.test
    def ext_test_one(self):
        logger.info("Checking external connectivity...")

    @aetest.test
    def ext_test_two(self):
        logger.info("Checking external connectivity again...")
        raise Exception("Exception raised during testing... ")


if __name__ == "__main__":
    aetest.main()
