# pyATS Tips and Tricks - PacketCoders Webinar
This repository contains reference code used in the pyATS Tips and Tricks PacketCoders webinar (July 25, 2024). The code examples will focus on the AEtest test infrastructure provided by pyATS.

## Testcase Execution Tips/Tricks

The following code examples showcases the many ways to control test execution in the AEtest test infrastructure provided by pyATS. Some of the execution flow controls used in the examples include:

- Skip certain test sections based on results of another test section
- Jump to a specific test section based on the results of a test section
- Grouping testcases in a datafile and selectively executing testcases based on assigned group names
- Create and execute pre, post, and exception processors on test sections
- Randomize testcase execution
- Mark specific testcases as "must pass" and fail script execution if the testcase(s) fails


### Code Examples
- `tc_flow_control.py`: Skip test sections based on specific conditions.
- `tc_goto.py`: If a test section fails, jump to a specific test section.
- `tc_grouping.py`: Only execute specific testcases that belong to a group.
- `tc_processors.py`: Processors can execute before (pre) and after (post) testcase execution. Exception processors can run when an exception is raised.
- `tc_random.py`: Testcase execution can be randomized.
- `tc_vip.py`: Important testcases can be marked as "must pass". If the identified testcase(s) fail, the testscript blocks execution of other testcases and jumps to the `CommonCleanup` section (essentially aborting script execution).

### Additional Files
- `datafile.yml`: Provides input data to testscripts to allow dynamic execution with different test parameters, groups, etc.