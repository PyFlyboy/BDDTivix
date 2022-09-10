from behave import step
import random
from datetime import datetime, date, timedelta


@step("Open the Rent Car Search Page")
def go_to_rent_car_page(context):
    context.sb.open("http://qalab.pl.tivixlabs.com/")

@step("User select the country")
def select_country(context):
    # get all countries and save them in the list
    countries_locator = "//select[@id='country']//option"
    find_all_countries_attr = context.sb.find_elements(countries_locator)
    countries_value = []
    for val in find_all_countries_attr:
        countries_value.append(val.get_attribute("value"))
    # file the form with random country from the list
    random_country_locator = "//select[@id='country']//option[@value='{}']".format(random.choice(countries_value))
    context.sb.click(random_country_locator)

@step("User select the city")
def select_city(context):
    # get all cities and save them in the list
    cities_locator = "//select[@id='city']//option"
    find_all_cities_attr =  context.sb.find_elements(cities_locator)
    cities_value = []
    for val in find_all_cities_attr:
        cities_value.append(val.get_attribute("value"))

       # file the form with random country from the list
    random_city_locator = "//select[@id='city']//option[@value='{}']".format(random.choice(cities_value))
    context.sb.click(random_city_locator)

@step("User select the pick up date")
def select_pick_up_date(context):
    # generate random date for pick_up field
    today = datetime.now()
    pick_up_date = today.strftime("%m-%d-%Y")
    context.sb.type("//input[@name='pickup']", pick_up_date)

@step("User select the drop off date")
def select_drop_off_date(context):
    # generate random date for drop_off field
    today = datetime.now()
    number_of_days = random.randint(1, 10)  # get random number of rent days
    rent_date = today + timedelta(days=number_of_days)
    drop_off_date = rent_date.strftime("%m-%d-%Y")
    context.sb.type("//input[@name='dropoff']", drop_off_date)

@step("User click on the search btn")
def click_serach_btn(context):
    # click search btn
    context.sb.click("//button[@type='submit']")

@step("User see the result")
def verify_search_result(context):
    context.sb.wait_for_element_visible("#search-results", timeout=10)
    context.sb.assert_elements_visible("#search-results")
    context.sb.save_screenshot("search_results", "./screenshots", "#search-results")

@step("User select drop off date < pick up date")
def select_wrong_drop_off_date(context):
    # generate random date for drop_off field
    today = datetime.now()
    number_of_days = random.randint(1, 10)  # get random number of rent days
    rent_date = today - timedelta(days=number_of_days)
    drop_off_date = rent_date.strftime("%m-%d-%Y")
    context.sb.type("//input[@name='dropoff']", drop_off_date)

@step('User see the alert "{message}"')
def verify_message_search_result(context, message):
    alert_text_locator = "//h3[@class='alert alert-danger']"
    context.sb.wait_for_element_visible(alert_text_locator, timeout=5)
    context.sb.assert_text_visible(message, alert_text_locator)
    context.sb.save_screenshot("alert_message", "./screenshots", alert_text_locator)
