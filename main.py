from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the WebDriver
driver = webdriver.Firefox()

try:
    # Open the target website
    url = "https://www.lerugbynistere.fr/"  # Replace with your target website
    driver.get(url)

    # Define your keywords
    keywords = ["toulouse", "toulousain"]

    # Find all <h2> elements
    h2_elements = driver.find_elements(By.CLASS_NAME, "title")

    # Filter and get href of parent <a> tags
    results = []
    for result in h2_elements:
        if any(keyword.lower() in result.text.lower() for keyword in keywords):
            results.append(result)


    # Print the results
    for idx, element in enumerate(results, start=1):
        print(f"{idx}: {element.text} -> {element.get_attribute("href")}")

finally:
    # Close the WebDriver
    driver.quit()
