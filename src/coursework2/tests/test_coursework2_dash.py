import requests
from dash.testing.application_runners import import_app
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

def test_server_live(dash_duo):
    """
    GIVEN the app is running
    WHEN a HTTP request to the home page is made
    THEN the HTTP response status code should be 200
    """
    
    # Start the app in a server
    app = import_app(app_file="census.coursework2_dash")
    dash_duo.start_server(app)

    # Delay to wait 2 seconds for the page to load
    dash_duo.driver.implicitly_wait(2)

    # Get the url for the web app root
    url = dash_duo.driver.current_url

    # Requests is a python library and here is used to make a HTTP request to the sever url
    response = requests.get(url)

    # Finally, use the pytest assertion to check that the status code in the HTTP response is 200
    assert response.status_code == 200

def test_home_h1textequals(dash_duo):
    
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading text should be "2011 and 2021 Census Data Analytics"
    """

    # Start the app in a server
    app = import_app(app_file="census.coursework2_dash")
    dash_duo.start_server(app)

    # Wait for the H1 heading to be visible, timeout if this does not happen within 4 seconds
    dash_duo.wait_for_element("h1", timeout=4)

    # Find the text content of the H1 heading element
    h1_text = dash_duo.find_element("h1").text

    # Check the heading has the text we expect
    assert h1_text == "2011 and 2021 Census Data Analytics"


def test_pie_chart_selection(dash_duo):
    
    """
    GIVEN the app is running
    WHEN the dropdown is set to "Camden"
    THEN the pie chart title should contain "Camden"
    """

    # Start the app in a server
    app = import_app(app_file="census.coursework2_dash")
    dash_duo.start_server(app)

    # Wait for the dropdown element to be visible, timeout if this does not happen within 4 seconds
    dropdown_locator = "#dropdown-pie-2011"
    WebDriverWait(dash_duo.driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_locator)))

    # Add a delay to ensure the dropdown is fully loaded and visible
    time.sleep(2)

    # Scroll to the dropdown element to ensure it is fully visible
    dropdown_element = WebDriverWait(dash_duo.driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, dropdown_locator)))
    ActionChains(dash_duo.driver).move_to_element(dropdown_element).perform()

    # Click the dropdown element to open the dropdown
    dropdown_element.click()

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Select Croydon in the dropdown
    dash_duo.select_dcc_dropdown("#dropdown-pie-2011", "Camden")

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Check the chart title contains "Camden"
    css_selector = '#pie_2011 > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.g-gtitle > text'
    chart_title = dash_duo.find_element(css_selector)
    assert ("Camden" in chart_title.text), "'Camden' should appear in the chart title"

def test_second_pie_chart_selection(dash_duo):

    """
    GIVEN the app is running
    WHEN the dropdown is set to "Bexley"
    THEN the pie chart title should contain "Bexley"
    """

    # Start the app in a server
    app = import_app(app_file="census.coursework2_dash")
    dash_duo.start_server(app)

    # Wait for the dropdown element to be visible, timeout if this does not happen within 4 seconds
    dropdown_locator = "#dropdown-pie-2021"
    WebDriverWait(dash_duo.driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_locator)))

    # Add a delay to ensure the dropdown is fully loaded and visible
    time.sleep(2)

    # Scroll to the dropdown element to ensure it is fully visible
    dropdown_element = WebDriverWait(dash_duo.driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, dropdown_locator)))
    ActionChains(dash_duo.driver).move_to_element(dropdown_element).perform()

    # Click the dropdown element to open the dropdown
    dropdown_element.click()

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)
    
    # Select Bexley in the dropdown
    dash_duo.select_dcc_dropdown("#dropdown-pie-2021", "Bexley")

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Check the chart title contains "Bexley"
    css_selector = '#pie_2021 > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.g-gtitle > text'
    chart_title = dash_duo.find_element(css_selector)
    assert ("Bexley" in chart_title.text), "'Bexley' should appear in the chart title"

def test_bar_chart_selection(dash_duo):
    
    """
    GIVEN the app is running
    WHEN the dropdown is used to select "16 to 30 hours"
    THEN the bar chart information should contain "16 to 30 hours"
    """

    # Start the app in a server
    app = import_app(app_file="census.coursework2_dash")
    dash_duo.start_server(app)

    # Wait for the dropdown element to be visible, timeout if this does not happen within 4 seconds
    dropdown_locator = "#dropdown-bar-2011"
    WebDriverWait(dash_duo.driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_locator)))

    # Add a delay to ensure the dropdown is fully loaded and visible
    time.sleep(2)

    # Scroll to the dropdown element to ensure it is fully visible
    dropdown_element = WebDriverWait(dash_duo.driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, dropdown_locator)))
    ActionChains(dash_duo.driver).move_to_element(dropdown_element).perform()

    # Click the dropdown element to open the dropdown
    dropdown_element.click()

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Select the "16 to 30 hours" option in the dropdown
    option_locator = "//div[@id='dropdown-bar-2011']//div[contains(text(), '16 to 30 hours')]"
    option_element = WebDriverWait(dash_duo.driver, 4).until(EC.visibility_of_element_located((By.XPATH, option_locator)))

    # Click the option
    option_element.click()

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Check the chart information contains "16 to 30 hours"
    css_selector = '#bar_2011 > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.legend > g > g:nth-child(3) > g > text'
    chart_info = dash_duo.find_element(css_selector)
    assert ("16 to 30 hours" in chart_info.text), "'16 to 30 hours' should appear in the chart information"

def test_second_bar_chart_selection(dash_duo):
    
    """
    GIVEN the app is running
    WHEN the dropdown is used to select "16 to 30 hours"
    THEN the bar chart information should contain "16 to 30 hours"
    """

    # Start the app in a server
    app = import_app(app_file="census.coursework2_dash")
    dash_duo.start_server(app)

    # Wait for the dropdown element to be visible, timeout if this does not happen within 4 seconds
    dropdown_locator = "#dropdown-bar-2021"
    WebDriverWait(dash_duo.driver, 4).until(EC.visibility_of_element_located((By.CSS_SELECTOR, dropdown_locator)))

    # Add a delay to ensure the dropdown is fully loaded and visible
    time.sleep(2)

    # Scroll to the dropdown element to ensure it is fully visible
    dropdown_element = WebDriverWait(dash_duo.driver, 4).until(EC.element_to_be_clickable((By.CSS_SELECTOR, dropdown_locator)))
    ActionChains(dash_duo.driver).move_to_element(dropdown_element).perform()

    # Click the dropdown element to open the dropdown
    dropdown_element.click()

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Select the "16 to 30 hours" option in the dropdown
    option_locator = "//div[@id='dropdown-bar-2021']//div[contains(text(), '16 to 30 hours')]"
    option_element = WebDriverWait(dash_duo.driver, 4).until(EC.visibility_of_element_located((By.XPATH, option_locator)))

    # Click the option
    option_element.click()

    # Wait for 2 seconds to allow the page to update
    time.sleep(2)

    # Check the chart information contains "16 to 30 hours"
    css_selector = '#bar_2021 > div.js-plotly-plot > div > div > svg:nth-child(3) > g.infolayer > g.legend > g > g:nth-child(3) > g > text'
    chart_info = dash_duo.find_element(css_selector)
    assert ("16 to 30 hours" in chart_info.text), "'16 to 30 hours' should appear in the chart information"