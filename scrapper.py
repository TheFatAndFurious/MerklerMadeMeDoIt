import json
from selenium import webdriver
from selenium.webdriver.common.by import By

with open("teams_config.json", "r") as f:
    team_config = json.load(f)

with open("websites_config.json", "r") as f:
    websites_config = json.load(f)


def scrape_website(team_name, keywords, site_config):
    driver = webdriver.Firefox()
    results = []

    try:
        driver.get(site_config["url"])
        titles = driver.find_elements(By.CLASS_NAME, site_config["class_name"])

        for title in titles:
            text = title.text
            if any(keyword.lower() in text.lower() for keyword in keywords):
                try:
                    link = title.get_attribute("href")
                except:
                    link = None

                results.append({"team":team_name, "title": text, "link": link})

    finally:
        driver.quit()

    return results


if __name__ == "__main__":
    all_results = []

    for team_name, keywords in team_config.items():
        print(f"Scraping for team {team_name}")

        for site_name, site_config in websites_config.items():
            print(f" Scraping site: {site_name}")
            results = scrape_website(team_name, keywords, site_config)
            all_results.extend(results)

    for result in all_results:
        print(f"Team: {result['team']} | Title: {result['title']} | Link:{result['link']}")


