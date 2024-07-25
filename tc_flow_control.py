from dataclasses import dataclass
import ipaddress
from pyats import aetest
import logging

logger = logging.getLogger("pyats.aetest")


# Custom data model used for testing
@dataclass
class NetworkDevice:
    manufacturer: str
    device_type: str
    role: str
    mgmt_ip: ipaddress.IPv4Address

# Mocks a Cisco router device
router1 = NetworkDevice(
    manufacturer="Cisco",
    device_type="8000v",
    role="Router",
    mgmt_ip=ipaddress.IPv4Address("10.254.1.1"),
)


# Skip testcase intentionally
@aetest.skip("Skipping regardless")
class Testcase(aetest.Testcase):
    pass


class TestcaseTwo(aetest.Testcase):
    # Skip unless device is a router
    @aetest.skipIf(router1.role != "Router", "Only run this test for routers")
    @aetest.test
    def test_one(self):
        pass

    # Skip unless device is a switch
    @aetest.skipUnless(router1.role == "Switch", "Only run this test for switches")
    @aetest.test
    def test_two(self):
        pass

    @aetest.test
    def test_three(self):
        # Will skip a test based on the results of this testcase
        aetest.skip.affix(
            section=TestcaseTwo.test_four, reason="Skip because test 3 told you so!"
        )
        # Skip the given section if the condition is set to True (can be boolean or a callable)
        aetest.skipIf.affix(
            section=TestcaseTwo.test_five,
            condition=True,
            reason="Skips since the condition is set to True",
        )
        # Skip the given section *unless* the condition is True (which fails in this case)
        aetest.skipUnless.affix(
            section=TestcaseThree,
            condition=False,
            reason="Skip since condition is set to False and needs to be set to True",
        )

    @aetest.test
    def test_four(self):
        # Will be skipped because of test_three
        pass

    @aetest.test
    def test_five(self):
        # Will be skipped because of test_three
        pass

    @aetest.test
    def test_six(self):
        # Will pass - no reason to skip
        pass


class TestcaseThree(aetest.Testcase):
    # will be skipped because of TestcaseTwo.test_three
    pass


if __name__ == "__main__":
    aetest.main()
