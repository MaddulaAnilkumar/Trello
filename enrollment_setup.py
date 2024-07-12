from get_credentials import advcredentials
from get_enrollments_sunfire import SunfireProcessor
from awssensible import SensibleAPIs
from logger_utils import get_logger
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import os
import json
log = get_logger()
if __name__ == '__main__':
    print("amdetails processing")
    log.info("amdetails process initiated")
    amdetails_obj = amdetails()
    log.info("amd data processing")
    print("amd data processing")
    amendments_list = amdetails_obj.get_amendments()
    print("get amd data processed")
    log.info("get_amdetails processed")
    # Initialize SunfireProcessor
    sunfire_processor = SunfireProcessor()
    log.info("sunfire process initiated")
    # Initialize the driver
    options = Options()
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36")
    driver = webdriver.Chrome(options=options)
    for entry in amendments_list:
        if len(entry) >= 5:
            first_name, last_name, mem_dob, mem_id, advisor_name, email = entry
            log.info("for loop for amdetails started", first_name, last_name, mem_id, email)
            try:
                # Create a credential instance for each entry
                get_credentials = advcredentials("keen_libs", "CJ63GZcbIp4EIkm")
                # Retrieve credentials using KeenService
                retrieved_username, retrieved_password = get_credentials.get_credentials(email)
                log.info("get_credentials for", email)
                if retrieved_username is not None and retrieved_password is not None:
                    print("Retrieved Username:", retrieved_username)
                    print("Retrieved Password:", retrieved_password)
                    # Call login_to_sunfire to log in
                    sunfire_processor.login_to_sunfire(retrieved_username, retrieved_password)
                    log.info("sunfire login processed for", retrieved_username)
                        # Call process_search_page with retrieved details
                    sunfire_processor.process_search_page(first_name, last_name, mem_dob)
                            # PDF directory path
                    pdf_directory = 'C:/keen/sunfire/Enrolment_cleanup'
                    try:
                                # Initialize the SensibleAPIs class with mem_id and pdf_directory
                        sensible_client = SensibleAPIs(mem_id, pdf_directory)
                        print("sensibleapi started for", mem_id)
                        log.info("sensibleapi started for", mem_id)
                                # Call the method to extract PDF and save to CSV
                        sensible_client.extract_pdf_and_save_to_csv()
                    except Exception as e:
                        print(f"Error process pdf for:{mem_id}")
                        log.error(f"Error process pdf for:{mem_id}")
                else:
                    print("Credentials not found for email:", email)
                    log.error("Credentials not found for email:", email)
            except Exception as e:
                print(f"Error processing entry: {entry}")
                log.error(f"Error processing entry: {entry}")
                print("Error message:", str(e))
                log.error(f"Error processing entry: {entry}")
        else:
            print("Entry does not contain enough values:", entry)
            log.error("Entry does not contain enough values:", entry)