Feature: SeleniumBase scenarios for the Rent Car Search App

  Background:
    Given Open the Rent Car Search Page

  Scenario: User can search cars for rent
    When User select the country
    Then User select the city
    And User select the pick up date
    And User select the drop off date
    And User click on the search btn
    Then User see the result

  Scenario Outline: User can not search cars for rent if drop off date < pick up date
    When User select the country
    Then User select the city
    And User select the pick up date
    And User select drop off date < pick up date
    And User click on the search btn
    Then User see the alert "<message>"
    Examples:
       | message                      |
       | Please enter a valid date! |