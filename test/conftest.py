import pytest

def pytest_configure():
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.

    Changes permissions for Qualys Agent folder
    """
    print("=======================================================")
    print("                          Configure Scope Started      ")
    print("=======================================================")


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """

    print("=======================================================")
    print("                          Session Scope Started         ")
    print("=======================================================")
   
def pytest_sessionfinish():
    """
    Called after whole test run finished, right before
    returning the exit status to the system.

    Logging report of execution and getting duration of execution.
    """
    print("=======================================================")
    print("                          Session Scope Ended         ")
    print("=======================================================")


def pytest_unconfigure():
    """
    called before test process is exited.
    Upload result to Zephyr
    """
    print("========================================================")
    print("               Starting Unconfigure                      ")
    print("========================================================")
    
    print("========================================================")
    print("               Unconfigure  Ended                       ")
    print("========================================================")


    