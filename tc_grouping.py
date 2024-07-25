from pyats import aetest
from pyats.datastructures.logic import And, Not
import logging

logger = logging.getLogger('pyats.aetest')

class BGPTestcase(aetest.Testcase):
    
    @aetest.test
    def bgp_test_one(self):
        logger.info("BGP testing in progress...")

class ExternalConnectivity(aetest.Testcase):
    
    @aetest.test
    def ext_test_one(self):
        logger.info("Checking external connectivity...")

class SpanningTree(aetest.Testcase):

    @aetest.test
    def stp_test_one(self):
        logger.info("Running L2 testing...")

if __name__ == '__main__':
    # Allows testcases in "L3" and not in "L2" group to execute
    aetest.main(datafile="datafile.yml", groups=And("L3", Not("L2")))