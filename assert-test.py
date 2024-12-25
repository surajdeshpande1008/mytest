from hamcrest import equal_to
from hamcrest import assert_that
from hamcrest import has_item
from hamcrest import contains
from hamcrest import contains_inanyorder
from hamcrest import has_key
from hamcrest import has_value
from hamcrest import is_not
from hamcrest import greater_than
from hamcrest import ends_with
from hamcrest import contains_string
from hamcrest import empty
from hamcrest import has_length
from hamcrest import starts_with
from hamcrest import has_entry
from hamcrest import has_entries
from hamcrest import greater_than_or_equal_to
from hamcrest import less_than_or_equal_to

from configparser import ConfigParser


import allure


CONFIG_DATA = {}

def test_QAG_24723():
    try:
        logs=get_Logs('"3u5": Information: Patch: No active deployment jobs to schedule.',getConfigValue('AGENT', 'log_file_path'))
        print("logs = ", logs)
        if len(logs)!=0:
            print("Logs OK")
        else:
            print("Unexpected Error pls check logs in Backlog Folder")

    finally:
        pass


def getConfigValue(section, key):
    print("******* getConfigValue() ********")
    if len(CONFIG_DATA) == 0:
        loadConfig()
    val = CONFIG_DATA[section + "." + key]
    print("Val = " , val)
    return val

def get_Logs(logtype, filename, encoding_format='utf-16'):
    print("**********  get_logs() ***************")
    print("filename = ", filename)
    filteredlog = []
    try:
        with open(filename, encoding=encoding_format) as f:

            lines = f.readlines()
            #print("======> ", lines)
            for line in lines:
                if logtype in line:
                    filteredlog.append(line)
            if len(filteredlog) == 0:
                print("No logs for given string : {} ".format(logtype))
            else:
                print(filteredlog)
    except Exception as E:
        print("In exception......", E)
        print(E.__cause__)
        AssertionError(E.__cause__)
    return filteredlog


def loadConfig():
    try:
        config = ConfigParser()
        config.read("config.ini")
        for section in config.sections():
            for key in config.items(section):
                CONFIG_DATA[section + "." + key[0]] = key[1]
        print("Config.ini read successfully")
    except Exception as e:
        print(e.__cause__)



test_QAG_24723()