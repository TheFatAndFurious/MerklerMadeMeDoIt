from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

try:
    url = "https://www.lerugbynistere.fr/"
    driver.get(url)

    headlines = driver.find_elements(By.TAG_NAME, "h2")

    keywords = ["toulousain", "toulouse", "dupont"]

    filteredResults = []
    for result in headlines:
        if any(keyword.lower() in result.text.lower() for keyword in keywords):
            filteredResults.append(result)
finally:
    for idy, headlineTest in enumerate(headlines, start=1):
        print(f" coucou {idy}: {headlineTest.parent}")

    # results = []
    #
    # for headline in filteredResults:
    #     parent = headline.find_element(By.XPATH, './ancestor::a[@href]')
    #     href = parent.get_attribute("href")
    #     results.append((headline.text, href))
    #
    # for idx, (text, link) in enumerate(results, start=1):
    #     print(f"{idx}: {text} -> {link}")
    driver.quit()
