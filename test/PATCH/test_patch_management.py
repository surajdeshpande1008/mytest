import datetime
import os
import time

import allure
import pytest


@pytest.fixture(autouse=True,scope="module")
def setup():
    print("================= setup() ================")
    
    
@pytest.fixture(autouse=True,scope='function')
def cleanup():
    print("================= cleanup() ================")
    
    
@pytest.mark.Agent_Patch
@pytest.mark.Agent_Regression
def test_QAG_18249():
    print("================= test_QAG_18249() ================")


@pytest.mark.Agent_Regression
@pytest.mark.Agent_EDR
def test_QAG_17589():
    print("================= test_QAG_17589() ================")
    

@pytest.mark.Agent_FIM
@pytest.mark.Agent_Regression
def test_QAG_12341():
    print("================= test_QAG_12341() ================")


@pytest.mark.Agent_Regression
@pytest.mark.Agent_CMD
def test_QAG_14312():
    print("================= test_QAG_14312() ================")
 
    
