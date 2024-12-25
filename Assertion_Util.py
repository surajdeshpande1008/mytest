me codefrom hamcrest import equal_to
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

import allure
adsed some code

@allure.step("Assert {0} and {1} are equal")
def assert_equal(val1, val2, custom_error_msg="Both val are not equal"):
    assert_that(val1, equal_to(val2), custom_error_msg)


@allure.step("Assert {0} has length {1}")
def assert_length(val, val_len, custom_error_msg="Length not matched"):
    assert_that(val, has_length(val_len), custom_error_msg)


# Number


@allure.step("Assert {0} is greater than : {1}")
def assert_greaterThan(val, val2, custom_error_msg="Value is not greater"):
    assert_that(val, greater_than(val2), custom_error_msg)


@allure.step("Assert {0} is greater than or equal : {1}")
def assert_greaterThanOrEqual(val, val2, custom_error_msg="Value is not greater or equal"):
    assert_that(val, greater_than_or_equal_to(val2), custom_error_msg)


@allure.step("Assert {0} is less than : {1}")
def assert_lessThan(val, val2, custom_error_msg="Value is more then defined number"):
    assert_that(val, greater_than(val2), custom_error_msg)


@allure.step("Assert {0} is less than or equal : {1}")
def assert_lessThanOrEqual(val, val2, custom_error_msg="Value is more then defined number"):
    assert_that(val, less_than_or_equal_to(val2), custom_error_msg)


# Text


@allure.step("Assert {0} has SubString : {1}")
def assert_subString(val, sub_str, custom_error_msg="Substring not present"):
    assert_that(val, contains_string(sub_str), custom_error_msg)


@allure.step("Assert {val} ends with String : {sub_str}")
def assert_endWith(val, sub_str, custom_error_msg="String doesn't end with required pattern"):
    assert_that(val, ends_with(sub_str), custom_error_msg)


@allure.step("Assert {0} start with String : {1}")
def assert_startWith(val, sub_str, custom_error_msg="Value do not start with defined text"):
    assert_that(val, starts_with(sub_str), custom_error_msg)


@allure.step("Assert {0} equals : {1}")
def assert_equalIgnoreCase(val, val2, custom_error_msg="Values are not equal"):
    assert_that(val, assert_equalIgnoreCase(val2), custom_error_msg)


# Collection

@allure.step("Assert {collections} is empty")
def assert_collectionEmpty(collections):
    assert_that(collections, empty(), "Collection is not empty")


@allure.step("Assert {0} has element {1}")
def assert_collectionHasElement(collections, element):
    assert_that(collections, has_item(element), "Collection do not have element :" + str(element))


@allure.step("Assert {0} do not have element {1}")
def assert_collectionDoNotHaveElement(collections, element):
    assert_that(collections, not (has_item(element)), "Collection has element :" + str(element))


@allure.step("Assert {0} have elements {1}")
def assert_collectionWithOrder(collections, element):
    assert_that(collections, contains(element),
                "Collection do not have all/some elements " + str(element))


@allure.step("Assert {0} have elements {1}")
def assert_collectionWithAnyOrder(collections, element):
    assert_that(collections, contains_inanyorder(element), "Collection do "
                                                           "not have all/some elements " + str(element))


# Dictionary
@allure.step("Assert {0} dictionary have item {1}")
def assert_entry(dictionary, entry_elem, custom_error_message="Value not present in dictionary"):
    assert_that(dictionary, has_entry(entry_elem), custom_error_message)


@allure.step("Assert {0} dictionary have items {1}")
def assert_entryList(dictionary, entryList_elem, custom_error_message="Values not present in dictionary"):
    assert_that(dictionary, has_entries(entryList_elem), custom_error_message)


@allure.step("Assert {0} dictionary have key {1}")
def assert_dictionaryHasKey(dictionary, key, custom_error_message="key not present in dictionary"):
    assert_that(dictionary, has_key(key), custom_error_message)


@allure.step("Assert {0} dictionary have value {1}")
def assert_dictionaryHasValue(dictionary, value, custom_error_message="Value not present in dictionary"):
    assert_that(dictionary, has_value(value), custom_error_message)


# Logical
@allure.step("Assert {val1} is not {val2}")
def assert_isNot(val1, val2, custom_error_message="Values are same "):
    assert_that(val1, is_not(val2), custom_error_message)
