import time
from urllib.parse import urlparse
import re

st = time.time()
a_tag_list_ = []
mail_tag_list_ = []

while True:
    now = time.time() - st
    if now > 5:
        break

    els = driver.find_elements(By.XPATH, "//a")
    if els:
        for el in els:
            try:
                url = el.get_attribute("href")
                parsed_url = urlparse(url)
                domain = re.sub("^www\.", "", parsed_url.netloc)  # Remove 'www.' if exists

                # Check if URL is not already processed
                if url not in a_tag_list_ and domain in url:
                    a_tag_list_.append(url)

                # Check for specific domains in 'toiawase_domain' list and ensure no duplication
                if any(toiawase_domain in url for toiawase_domain in toiawase_domain_list) and url not in mail_tag_list_:
                    mail_tag_list_.append(url)

            except Exception as e:
                # Optionally, log the exception e
                continue

print("==================================================")
