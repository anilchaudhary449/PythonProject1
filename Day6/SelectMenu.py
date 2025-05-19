from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

try:
    driver: WebDriver = webdriver.Firefox()
    driver.get("https://demoqa.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)

    wait = WebDriverWait(driver, 10)

    # Navigate to Select Menu
    WidgetBtn = driver.find_element(By.XPATH, "//h5[text()='Widgets']")
    driver.execute_script("arguments[0].scrollIntoView(true);", WidgetBtn)
    WidgetBtn.click()

    SelectMenu = driver.find_element(By.XPATH, "//span[text()='Select Menu']")
    driver.execute_script("arguments[0].scrollIntoView(true);", SelectMenu)
    SelectMenu.click()

    # 1. Select Value Dropdown
    select_value_dropdown = driver.find_element(By.XPATH, "//div[contains(@id,'withOptGroup')]")
    select_value_dropdown.click()
    value_option = driver.find_element(By.XPATH, "//div[text()='Group 1, option 2']")
    value_option.click()

    selected_value = driver.find_element(By.CSS_SELECTOR, "#withOptGroup .css-1uccc91-singleValue")
    assert selected_value.text == "Group 1, option 2", f"Expected 'Group 1, option 2' but got '{selected_value.text}'"
    print("✅ PASS: 'Group 1, option 2' selected successfully.")

    # 2. Select One
    select_one_dropdown = driver.find_element(By.ID, "selectOne")
    select_one_dropdown.click()
    select_title = driver.find_element(By.CSS_SELECTOR, "#react-select-3-input")
    select_title.send_keys("Mr.")
    select_title.send_keys(Keys.ENTER)

    selected_title = driver.find_element(By.CSS_SELECTOR, "#selectOne .css-1uccc91-singleValue")
    assert selected_title.text == "Mr.", f"Expected 'Mr.' but got '{selected_title.text}'"
    print("✅ PASS: 'Mr.' selected successfully.")

    # 3. Old Style Select Menu
    old_select_menu = Select(driver.find_element(By.ID, "oldSelectMenu"))
    old_select_menu.select_by_visible_text("Green")
    selected_old = old_select_menu.first_selected_option.text
    assert selected_old == "Green", f"Expected 'Green' but got '{selected_old}'"
    print("✅ PASS: 'Green' selected in old style select.")

    # 4. Multiselect Dropdown (custom)
    multiselect_drop = driver.find_element(By.XPATH, "//*[contains(text(),'Select...')]")
    driver.execute_script("arguments[0].scrollIntoView(true)", multiselect_drop)
    multiselect_drop.click()

    multiselect_opt = driver.find_element(By.XPATH, "//input[@id='react-select-4-input']")
    for color in ["Green", "Black", "Red"]:
        multiselect_opt.send_keys(color)
        multiselect_opt.send_keys(Keys.ENTER)

    # Check if 3 tags are visible
    multiselect_tags = driver.find_elements(By.CSS_SELECTOR, "#selectMenuContainer .css-12jo7m5")
    assert len(multiselect_tags) >= 3, "Expected at least 3 multiselect options"
    print("✅ PASS: Multiselect options selected successfully.")

    # 5. Standard Multi-Select
    multi_select_drop = Select(driver.find_element(By.ID, "cars"))
    multi_select_drop.select_by_value("volvo")
    multi_select_drop.select_by_visible_text("Audi")
    multi_select_drop.select_by_index(2)  # Saab

    selected_options = [option.text for option in multi_select_drop.all_selected_options]
    expected = {"Volvo", "Audi", "Saab"}
    assert expected.issubset(set(selected_options)), f"Expected selections {expected} but got {selected_options}"
    print("✅ PASS: Multi-select standard menu selected correctly.")

except AssertionError as e:
    print(f"❌ FAIL: {e}")

except Exception as e:
    print(f"❌ ERROR: Unexpected exception occurred - {e}")

finally:
    driver.quit()
