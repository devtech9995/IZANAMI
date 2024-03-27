from urllib.parse import urlparse
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# Initialize variables
main_ulr = 'https://www.hotpepper.jp/strJ003625270/'
driver = webdriver.Chrome()
driver.get(main_ulr)  # Assuming main_url is defined
a_tag_list_ = []  # List for unique URLs
mail_tag_list_ = []  # List for URLs containing inquiry-related keywords
toiawase_domain = ["contact", "inquiry", "form", "faq", "information"]
start_time = time.time()

print("サイト内タグ検索")

while True:
    # Break the loop if it runs more than 5 seconds
    if time.time() - start_time > 5:
        break

    elements = driver.find_elements(By.XPATH, "//a")
    if elements:
        for element in elements:
            try:
                url = element.get_attribute("href")
                if url is None or url in a_tag_list_:  # Skip if URL is None or already processed
                    continue

                parsed_url = urlparse(main_ulr)
                domain = parsed_url.netloc.replace("www.", "")  # Simplify domain
                
                # Check if URL matches any inquiry-related keyword and is not already in mail_tag_list_
                if any(keyword in url for keyword in toiawase_domain) and url not in mail_tag_list_:
                    mail_tag_list_.append(url)
                
                # Add URL to a_tag_list_ if not already present (for unique tracking)
                if url not in a_tag_list_ and domain in url:
                    a_tag_list_.append(url)

            except Exception as e:
                # Optionally handle the exception, e.g., logging
                continue

print("==================================================")
print(domain)
print('a_tag_list_: ', a_tag_list_)
print('mail_tag_list_: ', mail_tag_list_)