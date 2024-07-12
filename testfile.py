# # import time
import time
from datetime import datetime

# Date string from the Excel cell
# date_string = "Jul 16, 2022"
#
# # Convert the date string to a datetime object
# date_object = datetime.strptime(date_string, '%b %d, %Y')
#
# # Extract the date and year from the datetime object
# date_value = date_object.date()
# year_value = date_object.year
# month_value=date_object.date()
#
# # Print the extracted date and year
# print("Date:", date_value)  # Output: Date: 2022-07-16
# print("Year:", year_value)  # Output: Year: 2022
# print("Month:" ,month_value)
# import time
# # print(time.time())
#
# from datetime import datetime
#
# # Get the current date
# import requests
#
# today = datetime.today()
#
# # Format the date as "mm dd yyyy"
# formatted_date = today.strftime("%m/%d/%Y")
# # today.strftime("%m/%d/%y")
# # today.strftime("%m/%d/%y")
# # today.strftime("%m/%d/%Y")
# # Print the formatted date
# print("Formatted date:", formatted_date)







# # from selenium.webdriver import ActionChains
# #
# # from Pages.Keen_Associate_capture_full_member_details import Associate_Capture_full_Member_details
# from openpyxl import load_workbook
# from selenium.webdriver.common.by import By
#
# from Pages.Keen_account_creation import Keen_Account_creation
# from tests.test_ALogin import Test_login
# # from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
# # # from Pages.Keen_scheduleMeeting import Keen_Scedule_Meeting
# # # from selenium.webdriver import ActionChains
# # # from utilities.action_utils import ActionUtils
# # # class Test_calendly(Test_login):
# # #     def test_meeting(self):
# # #         keen_account=Keen_Account_creation(self.driver)
# # #         action_utils=ActionUtils(self.driver)
# # #         keen=Keen_Scedule_Meeting(self.driver)
# # #         action = ActionChains(self.driver)
# # #         keen_create=Create_capture_member_details(self.driver)
# # #         substring="Test - Calendly"
# # #         lead=keen_create.select_member()
# # #         for members in lead:
# # #             members.text[1].click()
# # #             break
# # #         member_name=keen.schedule_meeting_member()
# # #         print(member_name)
# # #         name=member_name.text
# # #         print(name)
# # #         email_lead = keen_account.validation_of_email()
# # #         phone_lead = keen_account.validation_of_Phone()
# # #         lead_phone = action_utils.convert_string(phone_lead)
# # #         action_utils.wait_for_element((Keen_Scedule_Meeting.meeting))
# # #
# # #         keen.click_schedule_meeting()
# # #         parent_guid = self.driver.current_window_handle
# # #         handle = self.driver.window_handles
# # #         for guid in handle:
# # #             if guid != parent_guid:
# # #                 self.driver.switch_to.window(guid)
# # #                 keen.accept_cookies()
# # #                 title=keen.title_calendly()
# # #                 verify_title=title.is_displayed()
# # #                 if verify_title:
# # #                     assert True
# # #                 else:
# # #                     assert False
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.test))
# # #                 keen.click_test()
# # #                 page=keen.verify_date_sheet()
# # #                 verify_page=page.is_displayed()
# # #                 if verify_page:
# # #                     assert True
# # #                 else:
# # #                     assert False
# # #                 avaliable_dates=keen.pick_dates()
# # #                 dates=(avaliable_dates.get_attribute("aria-label"))
# # #                 split_values = dates.split("-")
# # #                 first_part = split_values[0].strip()
# # #                 date_match = re.search(r"(\d+)", first_part)
# # #                 date=(date_match.group(1))
# # #                 meeting_date=keen.select_dates()
# # #                 for meeting in meeting_date:
# # #                     if meeting.text == date:
# # #                         print("Test Pass")
# # #                         action.move_to_element(meeting).click().perform()
# # #                         break
# # #                 avaliable_time=keen.select_time()
# # #                 for time in avaliable_time:
# # #                     print(time.text)
# # #                     time.text[1].click()
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.next))
# # #                 keen.click_next()
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.test_page))
# # #                 schedule_meeting=keen.Schedule_member_page()
# # #                 if schedule_meeting.is_displayed():
# # #                     assert True
# # #                 else:
# # #                     assert False
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.name))
# # #                 keen.enter_name(name)
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.email))
# # #                 keen.enter_emali(email_lead)
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.phone))
# # #                 keen.enter_phone_number("+1"+' '+lead_phone)
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.schedule_meeting))
# # #                 keen.submit_schedule_meeting()
# # #                 action_utils.wait_for_element((Keen_Scedule_Meeting.confirmed_meeting))
# # #                 success_message=keen.verify_confirmed_meeting()
# # #                 if success_message.is_displayed():
# # #                     assert True
# # #                 else:
# # #                     assert False
# # #                 if guid == guid:
# # #                     self.driver.close()
# # #                 if guid == parent_guid:
# # #                     self.driver.switch_to.window(parent_guid)
# # #                     self.driver.refresh()
# # #                     BD_link = keen.Verify_meeting_link()
# # #                     for BD_activity in BD_link:
# # #                         print(BD_activity.text)
# # #                         if substring in BD_activity.text:
# # #                             assert True
# # #                         else:
# # #                             assert False
# # # import datetime
# # # from datetime import datetime
# # # from dateutil.relativedelta import relativedelta
# # #
# # # def calculate_age(birthdate):
# # #     # Get the current date
# # #     current_date = datetime.now().date()
# # #
# # #     # Convert the birthdate string to a datetime object
# # #     birthdate_obj = datetime.strptime(birthdate, "%m/%d/%Y").date()
# # #
# # #     # Calculate the relativedelta between the current date and the birthdate
# # #     age = relativedelta(current_date, birthdate_obj)
# # #
# # #     # Return the formatted age string
# # #     age_str = f"{age.years} years {age.months} months {age.days} days"
# # #     return age_str
# # # birthdate = "1/7/1998"
# # # age = calculate_age(birthdate)
# # # print(age)
# # from selenium.webdriver.common.by import By
# # #
# # # from tests.test_create_Capture_full_Member_details import Test_create_capture_full_member_details
# # # from utilities.base_test import BaseTest
# # #
# # # number=BaseTest()
# # # row_plan=number.get_random_number("Plans")
# # # row_planassociate=number.get_random_number("Plans_associate")
# # # row_caregivers=number.get_random_number("Caregiver")
# # # row_account=number.get_random_number("Account_Creation")
# # # row_tasks=number.get_random_number("Tasks")
# # # row_hospitals=number.get_random_number("Hospitals")
# # # row_events=number.get_random_number("Events")
# # # row_physicians=number.get_random_number("Physicians")
# # # row_medication=number.get_random_number("Medication")
# # # row_pharmacy=number.get_random_number("Pharmacies")
# # # row_soa_number=number.get_random_number("SOA")
# # #
# # # class Test_anil(Test_login):
# # #     def test_account(self):
# # #         keen_create=Create_capture_member_details(self.driver)
# # #         keen_test_create=Test_create_capture_full_member_details(self.driver)
# # #         keen_account=Keen_Account_creation(self.driver)
# # #         member=keen_account.select_member()
# # #         for member_records in member:
# # #             if member_records.text == "Test Sean Williams":
# # #                 member_records.click()
# # #                 break
# # #         keen_create.Capture_Full_Member()
# # #         keen_create.Medication_option()
# # #         keen_create.click_new()
# # #         keen_test_create.test_create_Medications(row_medication)
# # #         keen_test_create.test_validation_medication(row_medication)
# # #         keen_create.select_physicians()
# # #         # keen_test_create.test_create_physicians(row_physicians)
# #
# # # import datetime
# # #
# # # # Get the date value from the element
# # # # date_element = driver.find_element_by_id("your_date_element_id")
# # # # date_value = date_element.get_attribute("value")
# # # date_vale="1/20/2023"
# # # # Convert the date to the expected format
# # # parsed_date = datetime.datetime.strptime(date_vale, "%m/%d/%Y")
# # # expected_date_format = parsed_date.strftime("%b %d, %Y")
# # # print(expected_date_format)
# # import openpyxl
# #
# # # Load the Excel file
# # # from utilities.base_test import BaseTest
# # #
# # # workbook = openpyxl.load_workbook('C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\test_data\\Keen_Testdata.xlsx')
# # #
# # # # Select the worksheet
# # # worksheet = workbook.active
# # #
# # # # Get the column names from the first row of the worksheet
# # # column_names = []
# # # for cell in worksheet[1]:
# # #     column_names.append(cell.value)
# # #
# # # # Iterate through each row of the worksheet, starting from the second row
# # # for row in worksheet.iter_rows(min_row=2, values_only=True):
# # #     # Create a dictionary to hold the data for this row
# # #     row_data = {}
# # #     for i in range(len(column_names)):
# # #         # Map the column name to the field name in your application
# # #         field_name = column_names[i]
# # #
# # #         # Add the data for this column to the row_data dictionary
# # #         row_data[field_name] = row[i]
# # # import random
# # # number=BaseTest()
# # # path="C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\test_data\\Keen_Testdata.xlsx"
# # # random_index=number.get_random_number("Account_Creation")
# # # random_row = path.iloc[random_index]
# # # for column_name, field_value in random_row.items():
# # #     # Locate the field in your application based on the column name
# # #     field = self.driver.find_element_by_name(column_name)
# # #
# # #     # Fill the field with the corresponding value from the randomly selected row
# # #     field.send_keys(str(field_value)
# # # source_of_creation="Other"
# # #
# # # if source_of_creation == "Provider: Aledade" or "Provider: Archwell" or "Advisor Directory (Aledade)" or "Aledade Call Center" or "Aledade T-65/MAI" or "Provider: ChenM / Ded Call center" or "Source, Provider: ChenM / Ded MCG" or "Source, Provider: Gather" or "Source, Provider: Homeward" or "Source, Provider: IORA" or "Source, Provider: Other":
# # #     print("yes")
# # # else:
# # # #     print("fail")
# # from selenium import webdriver
# # from openpyxl import load_workbook
# # # Load the Excel sheet
# # path=('C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\test_data\\Keen_Testdata.xlsx')
# # workbook = load_workbook(path)
# # worksheet = workbook.active
# # from selenium.webdriver.support import expected_conditions
# # from selenium.webdriver.support.wait import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # from openpyxl import load_workbook
# # from selenium.webdriver.common.keys import Keys
# # from utilities.action_utils import ActionUtils
# # from utilities import logger_utils
# from utilities import logger_utils
# from utilities.base_test import BaseTest
#
# workbook = load_workbook('C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\test_data\\Keen_Testdata.xlsx')
# # from selenium.webdriver.common.by import By
# # sheet_12=workbook['Account_Creation']
# # sheet = workbook['Plans']
# # sheet_practices=workbook['Practices']
# # sheet_medication=workbook['Medication']
# # sheet_hospitals=workbook['Hospitals']
# # sheet_physicians=workbook['Physicians']
# # sheet_pharmacy=workbook['Pharmacies']
# # sheet_event=workbook['Events']
# # sheet_related=workbook['Caregiver']
# # sheet_campaign=workbook['Campaigns']
# # sheet_parent=workbook['Parent_organization']
# # from utilities.base_test import BaseTest
# # from utilities.action_utils import ActionUtils
# # from tests.test_suite import Test_Suit
# # test_all=Test_Suit()
# class Test_data(Test_login):
#     log=logger_utils.get_logger()
#     number=BaseTest()
#     def test_tes(self):
#         action_utils = ActionUtils(self.driver)
#         keen = Keen_Account_creation(self.driver)
#         action_utils.wait_for_element((Keen_Account_creation.new_button))
#         keen.New()
#         action = ActionChains(self.driver)
#         sheet_name = 'Account_Creation'
#         sheet = workbook[sheet_name]
#         row_number = 6
#         data_row = sheet[row_number]
#         column_field_mapping = {
#             # 'first_Name': 'first_Name', 'Middle_Name': 'MiddleName', 'Last_Name': 'Last_Name',
#             # 'DoB': 'DoB',
#             # 'Email': 'Email',
#             # 'PTC': 'PTC', 'SOA': 'SOA', 'Phone': 'Phone',
#             # 'Street_Address': 'Street_Address',
#             # 'Gender': 'Gender',
#             'Source': 'Source',
#             # 'status': 'Status',
#             # 'Origin': 'Origin',
#             # 'Language': 'Language',
#             # 'MedicareID': 'MedicareID', 'MedcaidID': 'MedcaidID',
#             # 'Part_A enrollment date': 'Part_A enrollment date', 'Plan_enrollment date': 'Plan_enrollment date',
#             # 'Part_B enrollment date': 'Part_B enrollment date',
#             # 'Medicaid_status_verification_date': 'Medicaid_status_verification_date',
#             # 'SSN': 'SSN',
#             # 'Zipcode': 'Zipcode', 'City': 'City', 'State_Newcreation': 'State',
#             # 'Member_County': 'Member_County', 'Addressline2': 'Addressline2', 'PTC popup': 'PTC popup',
#             # 'Other_permission': 'Other_permission',
#         }
#         option_field_mappings={
#             'Aledade T-65/MAI': {
#                         'Source: Practice': 'Source: Practice',
#                     },
#             'Campaign': {
#                         'Source: Campaigns': 'Source: Campaigns',
#                     },
#             'Community Event': {
#                         'Source: Community organization': 'Source: Community organization',
#                         'Source: Practice': 'Source: Practice',
#                         'Source: Event': 'Source: Event'
#         }
#             }
#         field_locators = {
#             # 'first_Name': ((Keen_Account_creation.enter_firstName)), 'DoB': (Keen_Account_creation.enter_dob),
#             # 'MiddleName': ((Keen_Account_creation.enter_middleName)),
#             # 'Last_Name': ((Keen_Account_creation.enter_lastName)), 'Email': (Keen_Account_creation.enter_email),
#             # 'PTC': (Keen_Account_creation.enter_PTC),
#             # 'SOA': (Keen_Account_creation.enter_SOA), 'Phone': (Keen_Account_creation.enter_phone),
#             # 'Street_Address': (Keen_Account_creation.enter_address),
#             # 'Gender': (Keen_Account_creation.select_gender),
#             'Source': (Keen_Account_creation.click_source),
#             # 'Origin': (Keen_Account_creation.other_details_icon),
#             # 'MedicareID': (Keen_Account_creation.medication_details_popup),
#             # 'MedcaidID': (Keen_Account_creation.medicaid_id),
#             # 'Part_A enrollment date': (Keen_Account_creation.part_A),
#             # 'Plan_enrollment date': (Keen_Account_creation.enrollment_date),
#             # 'Part_B enrollment date': (Keen_Account_creation.part_B),
#             # 'Medicaid_status_verification_date': (Keen_Account_creation.verification_date),
#             # 'SSN': (Keen_Account_creation.SSN), 'Status': ((Keen_Account_creation.status)),
#             # 'Language': (Keen_Account_creation.options_in_list),
#             # 'Addressline2': (Keen_Account_creation.enter_newcreationaddress_line_2),
#             # 'Member_County': (Keen_Account_creation.enter_county_newcreation),
#             # 'Zipcode': (Keen_Account_creation.enter_zipcode_newcreation),
#             # 'City': (Keen_Account_creation.enter_city_newcreation), 'State': (Keen_Account_creation.click_state),
#             # 'PTC popup': (Keen_Account_creation.ptc_popup),
#             # 'Other_permission': (Keen_Account_creation.other_permission),
#             # 'Source: Practice': (Keen_Account_creation.practice_record),
#             # 'Source: Campaigns': (Keen_Account_creation.campaign_record),
#             'Source: Community organization': (Keen_Account_creation.community_record),
#             'Source: Event': (Keen_Account_creation.event_record)
#         }
#         keen = Keen_Account_creation(self.driver)
#         for cell in data_row:
#             column_name = sheet.cell(row=1, column=cell.column).value
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 self.log.info(field_name)
#                 print("mapping is done")
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'button':
#                     if field_name == 'Source':
#                         element.click()
#                         source = keen.select_source()
#                         for option in source:
#                             if option.get_attribute('title') == column_value:
#                                 print("clickable option:", column_value)
#                                 print("options are present")
#                                 self.driver.execute_script("arguments[0].click();", option)
#                         if column_value == "Community Event":
#                             assert keen.pop_up_sourceType().is_displayed(), "Source popup is not displayed"
#                             option_field = tuple(option_field_mappings[column_value].items())
#                             print("option fields:",option_field)
#                             for field_name, field_value in option_field:
#                                 print("field_name:",field_name)
#                                 print("field_value:",field_value)
#                                 if column_value in option_field_mappings:
#                                     fields_to_fill = option_field_mappings[column_value]
#                                     for field in fields_to_fill:
#                                         column_name = field  # Assuming column names and field names are the same
#                                         # Assuming you have the column value from the Excel sheet stored in a variable called 'column_value'
#                                         column_value = data_row[column_name].value
#                                         print("column value of options:",column_value)
#                                 # field_locator = field_locators[field_value]
#                                 # column_optionsvalue = cell.value
#                                 # if field_name == 'Source: Practice':
#                                 #     print(print("Options column value:", column_optionsvalue))
#                         elif column_value == "Campaign":
#                             assert keen.pop_up_sourceType().is_displayed(), "Source popup is not displayed"
#                             option_field = tuple(option_field_mappings[column_value].items())
#                             print("option fields:", option_field)
#                             for field_name, field_value in option_field:
#                                 field_locator = field_locators[field_value]
#                                 column_optionsvalue = cell.value  # Assuming you have the column value from the Excel sheet
#                                 print("Options column value:", column_optionsvalue)
#
#                 #                 if field_name == 'Source: Community organization':
#                 #                     keen.select_community_organization().send_keys(column_value)
#                 #                     list_community = keen.select_record()
#                 #                     print(len(list_community))
#                 #                     if len(list_community) == 0:
#                 #                         print("It is having 0 records")
#                 #                         keen.select_community_organization().send_keys(Keys.CONTROL + "a")
#                 #                         keen.select_community_organization().send_keys(Keys.BACKSPACE)
#                 #                     elif len(list_community) != 0:
#                 #                         print("Records are present")
#                 #                         for community in list_community:
#                 #                             if community.text == column_value:
#                 #                                 print(community.text)
#                 #                                 print("test Community is created")
#                 #                                 action.move_to_element(community).click().perform()
#                 #                             else:
#                 #                                 input_field = keen.select_community_organization()
#                 #                                 self.driver.execute_script("arguments[0].value = '';", input_field)
#                 #                                 print("test community is not there")
#                 #                                 # keen.select_community_organization().clear()
#                 #                 if field_name == 'Source: Practice':
#                 #                         keen.select_practice_directory().send_keys(column_value)
#                 #                         list_practice = keen.select_directory_records()
#                 #                         print("practice length: ", len(list_practice))
#                 #                         if len(list_practice) == 0:
#                 #                             print("It is having 0 records")
#                 #                             keen.select_practice_directory().clear()
#                 #                         elif len(list_practice) != 0:
#                 #                             print("Records are present")
#                 #                             for select_practice in list_practice:
#                 #                                 print(select_practice.get_attribute('title'))
#                 #                                 if select_practice.get_attribute('title') == column_value:
#                 #                                     print("test practice is created")
#                 #                                     action.move_to_element(select_practice).click().perform()
#                 #                                 else:
#                 #                                     keen.select_practice_directory().clear()
#                 #                                     print("test practice is not created")
#                 #                 if field_name == 'Source: Event':
#                 #                     keen.event().send_keys(column_value)
#                 #                     list_events = keen.select_events_records()
#                 #                     print("events length: ", len(list_events))
#                 #                     if len(list_events) == 0:
#                 #                         print("It is having 0 records")
#                 #                         keen.event().clear()
#                 #                     elif len(list_events) != 0:
#                 #                         print("Records are present")
#                 #                         for events in list_events:
#                 #                             print(events.get_attribute('title'))
#                 #                             if events.get_attribute('title') == column_value:
#                 #                                 print("test event is created")
#                 #                                 action.move_to_element(events).click().perform()
#                 #                                 break
#                 #                             else:
#                 #                                 keen.event().clear()
#                 #                                 print("test event is not created")
#                 #             keen.ok()
#                 #         elif column_value == "Member Referral" or "Source, Referrals from Redesign":
#                 #             action_utils.wait_for_element((Keen_Account_creation.source_popup))
#                 #             assert keen.pop_up_sourceType().is_displayed(),"Source popup is not displayed"
#                 #
#                 #             keen.click_referring_member("Test Member")
#                 #             list_referring_member = keen.select_record()
#                 #             if len(list_referring_member) == 0:
#                 #                 keen.cancel_sourcetype_popup()
#                 #             else:
#                 #                 for associate_member in list_referring_member:
#                 #                     if associate_member.text == "Test Test":
#                 #                         action.move_to_element(associate_member).click().perform()
#                 #                         break
#                 #                     keen.member_relationship()
#                 #                     list_relation = keen.relation_member()
#                 #                     for relation in list_relation:
#                 #                         if relation.text == "Friend":
#                 #                             action.move_to_element(relation).click().perform()
#                 #                             keen.ok()
#                 #                             break
#                 #         elif column_value == "Provider: Aledade" or "Provider: Archwell" or "Advisor Directory (Aledade)" or "Aledade Call Center" or "Aledade T-65/MAI" or "Provider: ChenM / Ded Call center" or "Source, Provider: ChenM / Ded MCG" or "Source, Provider: Gather" or "Source, Provider: Homeward" or "Source, Provider: IORA" or "Source, Provider: Other":
#                 #             if keen.pop_up_sourceType().is_displayed():
#                 #                 assert True
#                 #             else:
#                 #                 assert False
#                 #             keen.select_practice_directory().send_keys(column_value)
#                 #             list_practice = keen.select_record()
#                 #             if len(list_practice) == 0:
#                 #                 keen.cancel_sourcetype_popup()
#                 #             else:
#                 #                 print("select record")
#                 #                 for practice_only in list_practice:
#                 #                     print(practice_only.text)
#                 #                     if practice_only.text == column_value:
#                 #                         action.move_to_element(practice_only).click().perform()
#                 #                         keen.ok()
#                 #                         print("Source is selected")
#                 #                         break
#                 #         elif column_value == "Campaign":
#                 #             keen.select_campaign().send_keys("Test Test")
#                 #             campaign_list = keen.select_record()
#                 #             if len(campaign_list) == 0:
#                 #                 keen.cancel_sourcetype_popup()
#                 #             else:
#                 #                 for campaign in campaign_list:
#                 #                     if campaign.text == "Test test":
#                 #                         action.move_to_element(campaign).click().perform()
#                 #                         keen.ok()
#                 #                         break
#                 #         elif column_value == "Other":
#                 #             keen.Lead_other().send_keys("Test Test")
#                 #             keen.ok()
#                 #         else:
#                 #             print("Continue to Next Field")
#                 #     if field_name == 'Status':
#                 #         if field_name == 'Status':
#                 #             column_value = cell.value
#                 #         element.click()
#                 #         pick_up_status = keen.select_status()
#                 #         for keen_status in pick_up_status:
#                 #             if keen_status.get_attribute('title') == column_value:
#                 #                 print("clickable option:", column_value)
#                 #                 print("options are present")
#                 #                 self.driver.execute_script("arguments[0].click();", keen_status)
#                 #                 break
#                 #     if field_name == 'Gender':
#                 #         element.click()
#                 #         pick_up_gender = keen.select_gender_in_list()
#                 #         for gender in pick_up_gender:
#                 #             if gender.text == column_value:
#                 #                 self.driver.execute_script("arguments[0].click();", gender)
#                 #                 break
#                 #     if field_name == 'State':
#                 #         element.click()
#                 #         states = keen.select_state_newlead()
#                 #         for list_states in states:
#                 #             if list_states.text == column_value:
#                 #                 self.driver.execute_script("arguments[0].click();", list_states)
#                 #                 break
#                 # elif element.tag_name == 'lightning-icon':
#                 #     if field_name == 'MedicareID':
#                 #         print("Medicare detail popup is selecetd")
#                 #         keen.select_medication_details()
#                 #         keen.enter_medicare_ID().send_keys(column_value)
#                 #
#                 #     if field_name == 'PTC popup':
#                 #         keen.click_ptc_popup()
#                 #         assert keen.pop_up_sourceType().is_displayed(), "Source popup is not displayed"
#                 #         keen.click_permission_to_contact_filed()
#                 #         ptc_popup_options = keen.tabs_options()
#                 #         for options_ptc in ptc_popup_options:
#                 #             if options_ptc.text == column_value:
#                 #                 self.driver.execute_script("arguments[0].click();", options_ptc)
#                 #                 break
#                 #         if field_name == 'Other_permission':
#                 #             element.send_keys(column_value)
#                 #     if field_name == 'Origin':
#                 #         keen.other_details()
#                 #         keen.Country_of_origin().click()
#                 #         options = keen.select_Country_of_origin()
#                 #         for option in options:
#                 #             print("conutry:", option.text)
#                 #             if option.text == column_value:
#                 #                 self.driver.execute_script("arguments[0].click();", option)
#                 #                 print("country is selected")
#                 #                 break
#                 #         keen.ok()
#                 # elif element.tag_name == 'span':
#                 #     print("Span tag is present")
#                 #     if field_name == 'Language':
#                 #         print("langauage is present")
#                 #         keen.other_details()
#                 #         language_list = keen.tabs_options()
#                 #         for languages in language_list:
#                 #             if languages.text == column_value:
#                 #                 self.driver.execute_script("arguments[0].click();", languages)
#                 #                 print("Language is selected")
#                 #                 break
#                 #         keen.select_to_chosen()
#                 #         keen.ok()
#                 # else:
#                 #     element.send_keys(column_value)
#                 #     print("Field_names:", field_name)
#                 #     if field_name == 'SSN':
#                 #         keen.Click_Ok()
#                 #         self.log.info("***** Medicaredetails popup is closed *****")
#                 #     elif field_name == 'Other_permission':
#                 #         keen.ok()
#                 #         self.log.info("***** Other permission popup is closed *****")
# #     def test_plans(self,row_number):
# #         keen_associate = Associate_Capture_full_Member_details(self.driver)
# #         action_utils = ActionUtils(self.driver)
# #         action=ActionChains(self.driver)
# #         keen_create=Create_capture_member_details(self.driver)
# #         print("Row number:", row_number)
# #         data_row = sheet[row_number]
# #         column_field_mapping = {
# #             'Members Plan Details Name': 'Members Plan Details Name',
# #             'PlanID': 'PlanID', 'County': 'County', 'Parent Organization': 'Parent Organization',
# #             'Contract_Number': 'Contract_Number', 'PBP': 'PBP', 'Segment': 'Segment',
# #             'Plan_year': 'Plan_year', 'Carrier_name': 'Carrier_name', 'Product_type': 'Product_type', 'State': 'State',
# #         }
# #         field_locators = {
# #             'Members Plan Details Name': (Create_capture_member_details.Field_01),
# #             'PlanID': (Create_capture_member_details.Field_02), 'County': (Create_capture_member_details.Field_04),
# #             'Parent Organization': (Create_capture_member_details.Field_06),
# #             'Contract_Number': (Create_capture_member_details.plan_contractnumber),
# #             'PBP': (Create_capture_member_details.Field_D_03),
# #             'Segment': (Create_capture_member_details.Field_D_04),
# #             'Plan_year': (Create_capture_member_details.Field_D_05),
# #             'Carrier_name': (Create_capture_member_details.plan_carrier),
# #             'Product_type': (Create_capture_member_details.plan_producttype),
# #             'State': (Create_capture_member_details.plan_state),
# #
# #         }
# #         lead=keen_create.select_member()
# #         self.log.info("***** Selecting the member *****")
# #         lead[1].click()
# #         action_utils.wait_for_element((Create_capture_member_details.Member_details))
# #         self.log.info("***** Click on Capture fill members details *****")
# #         keen_create.Capture_Full_Member()
# #         action_utils.wait_for_element((Create_capture_member_details.plans_option))
# #         self.log.info("***** Click on Capture fill members details *****")
# #         keen_create.click_plans()
# #         action_utils.wait_for_element((Create_capture_member_details.new))
# #         self.log.info("***** Click on Capture fill members details *****")
# #         keen_create.click_new()
# #         action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
# #         pop_up = keen_create.pop_up_of_New_Members()
# #         assert pop_up.text == "New Member's plan","New Member plans popup is not matched"
# #         action_utils.wait_for_element((Create_capture_member_details.plans_records))
# #         verify_plans = action_utils.record_verification(row_number, 'Plans', 'Plans_Created')
# #         if verify_plans == 'YES':
# #             self.log.info("***** Account is exists in Salesforce *****")
# #             name = self.number.retrieve_Name(row_number, row_number, "M", 'Plans')
# #             keen_create.click_plan_detail_list().send_keys(name)
# #             list_of_plans = keen_associate.select_existing_records()
# #             for plans in list_of_plans:
# #                 if plans.text == name:
# #                     action.move_to_element(plans).click().perform()
# #                     break
# #         else:
# #             action_utils.wait_for_element((Create_capture_member_details.new_creation))
# #             keen_create.click_new_member()
# #             action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
# #             pop_up_of_detail_list = keen_create.pop_up_Newcreation()
# #             pop = pop_up_of_detail_list.text
# #             assert pop == "New Plan Detail List","popup is not displayed"
# #             self.log.info("****Entering the Plan Details to Create and Assosicate****")
# #             self.log.info("***** Account is not exists in Salesforce *****")
# #             for cell in data_row:
# #                 column_name = sheet.cell(row=2, column=cell.column).value
# #                 print("Column name:", column_name)
# #                 if column_name in column_field_mapping:
# #                     field_name = column_field_mapping[column_name]
# #                     print("mapping is done")
# #                     column_value = cell.value
# #                     print("input:",column_value)
# #                     locator = field_locators[field_name]
# #                     element = self.driver.find_element(*locator)
# #                     if element.tag_name == 'a':
# #                         print("a tag is present in elements")
# #                         if field_name == 'State':
# #                             element.click()
# #                             select_state = keen_create.select_options_in_list()
# #                             print("select state:",len(select_state))
# #                             for states in select_state:
# #                                 print("state name_Sf:", states.text)
# #                                 if states.text == column_value:
# #                                     self.driver.execute_script("arguments[0].click();", states)
# #                                     break
# #                         if field_name == 'Product_type':
# #                             element.click()
# #                             select_plantype = keen_create.select_product_type()
# #                             print("select plan:", len(select_plantype))
# #                             for plan_type in select_plantype:
# #                                 print("plan name_Sf:", plan_type.text)
# #                                 if plan_type.text == column_value:
# #                                     self.driver.execute_script("arguments[0].click();", plan_type)
# #                                     break
# #                         if field_name == 'Carrier_name':
# #                             element.click()
# #                             select_carrier = keen_create.select_options_in_list()
# #                             print("Carrier:",len(select_carrier))
# def test_validation_plans(self,row_number):
#         keen_associate = Associate_Capture_full_Member_details(self.driver)
#         action_utils = ActionUtils(self.driver)
#         action = ActionChains(self.driver)
#         keen_create = Create_capture_member_details(self.driver)
#         print("Row number:", row_number)
#         data_row = self.sheet_plans[row_number]
#         column_field_mapping = {
#             'Members Plan Details Name': 'Members Plan Details Name',
#             'PlanID': 'PlanID', 'County': 'County', 'Parent Organization': 'Parent Organization',
#             'Contract_Number': 'Contract_Number', 'PBP': 'PBP', 'Segment': 'Segment',
#             'Plan_year': 'Plan_year', 'Carrier_name': 'Carrier_name', 'Product_type': 'Product_type', 'State': 'State',
#         }
#         field_locators = {
#             'Members Plan Details Name': (Create_capture_member_details.verify_plan),
#             'PlanID': (Create_capture_member_details.verify_planid), 'County': (Create_capture_member_details.verify_county),
#             'Parent Organization': (Create_capture_member_details.verify_parent_organization),
#             'Contract_Number': (Create_capture_member_details.verify_contract_number),
#             'PBP': (Create_capture_member_details.Field_D_03),
#             'Segment': (Create_capture_member_details.Field_D_04),
#             'Plan_year': (Create_capture_member_details.Field_D_05),
#             'Carrier_name': (Create_capture_member_details.verify_carrier_name),
#             'Product_type': (Create_capture_member_details.verify_product_type),
#             'State': (Create_capture_member_details.verify_state),
#         }
#         for cell in data_row:
#             column_name = self.sheet_plans.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 print("mapping is done")
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 element = self.driver.find_element(*locator)
#                 verify_test_data=element.text
#                 if verify_test_data == column_value:
#                     assert True
#                     self.log.info("***** Test data is matched *****")
#                 else:
#                     self.log.info("***** Test data is not matched *****")
#                     assert False
#
#
# #
# #
# #
# #
# #
# #     def test_practice(self,row_number):
# #         action_utils = ActionUtils(self.driver)
# #         action = ActionChains(self.driver)
# #         keen_create = Create_capture_member_details(self.driver)
# #         print("Row number:", row_number)
# #         data_row = sheet_practices[row_number]
# #         column_field_mapping = {
# #             'Practice_name': 'Practice_name',
# #             'Practice_NPI': 'Practice_NPI', 'TaxID': 'TaxID', 'Phone_practices': 'Phone_practices',
# #             'Practice_email': 'Practice_email', 'Address_1': 'Address_1', 'City': 'City',
# #             'State': 'State', 'Zipcode': 'Zipcode', 'Aledade Practice Type': 'Aledade Practice Type',
# #             'Practice URL':'Practice URL',
# #             'Accepted Carriers': 'Accepted Carriers',
# #             'Status': 'Status'
# #         }
# #         field_locators = {
# #             'Practice_name': (Create_capture_member_details.Field_01),
# #             'Practice_NPI': (Create_capture_member_details.Field_02), 'TaxID': (Create_capture_member_details.Field_03),
# #             'Phone_practices': (Create_capture_member_details.Field_04),
# #             'Practice_email': (Create_capture_member_details.Field_05),
# #             'Address_1': (Create_capture_member_details.Field_D_01),
# #             'City': (Create_capture_member_details.Field_D_03),
# #             'State': (Create_capture_member_details.Field_SD_01),
# #             'Zipcode': (Create_capture_member_details.Field_D_04),
# #             'Aledade Practice Type': (Create_capture_member_details.Field_S_04),
# #             'Practice URL': (Create_capture_member_details.Field_06),
# #             'Accepted Carriers': (Create_capture_member_details.move_carriers),
# #             'Status' : (Create_capture_member_details.Field_S_02)
# #         }
# #         lead = keen_create.select_member()
# #         lead[1].click()
# #         action_utils.wait_for_element((Create_capture_member_details.Member_details))
# #         keen_create.Capture_Full_Member()
# #         action_utils.wait_for_element((Create_capture_member_details.select_practices))
# #         keen_create.click_practices()
# #         action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
# #         pop_of_members_practice = keen_create.pop_up()
# #         if pop_of_members_practice.text == "Member's practices":
# #             assert True
# #         else:
# #             assert False
# #         action_utils.wait_for_element((Create_capture_member_details.new))
# #         keen_create.click_new()
# #         action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
# #         New_Members_practice = keen_create.pop_up_of_New_Members()
# #         if New_Members_practice.text == "New Member's practice":
# #             assert True
# #         else:
# #             assert False
# #         verify_plan_record = action_utils.record_verification(row_number, 'Plans', 'Plans_Created')
# #         if verify_plan_record == 'YES':
# #             self.log.info("***** Account is exists in Salesforce *****")
# #         else:
# #             self.log.info("***** Account is not exists in Salesforce *****")
# #         keen_create.click_practice_directory()
# #         keen_create.click_new_member()
# #         action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
# #         pop_up_of_new_practice_directory = keen_create.pop_up_Newcreation()
# #         if pop_up_of_new_practice_directory.text == "New Practice directory":
# #             assert True
# #         else:
# #             assert False
# #         self.log.info("*****Enter the Test data to Practices*****")
# #         for cell in data_row:
# #             column_name = sheet_practices.cell(row=2, column=cell.column).value
# #             print("Column name:", column_name)
# #             if column_name in column_field_mapping:
# #                 field_name = column_field_mapping[column_name]
# #                 column_value = cell.value
# #                 print("input:",column_value)
# #                 locator = field_locators[field_name]
# #                 element = self.driver.find_element(*locator)
# #                 self.log.info("Finding web element to enter....{}".format(locator))
# #                 if element.tag_name == 'a':
# #                     print("a tag is present in elements")
# #                     if field_name == 'Status':
# #                         element.click()
# #                         list_of_status = keen_create.select_options_in_list()
# #                         for status_options in list_of_status:
# #                             print("statu_Sf:", status_options.text)
# #                             if status_options.text == column_value:
# #                                 self.driver.execute_script("arguments[0].click();", status_options)
# #                                 break
# #                     if field_name == 'State':
# #                         element.click()
# #                         select_state = keen_create.select_options_in_list()
# #                         print("select state:",len(select_state))
# #                         for states in select_state:
# #                             print("state name_Sf:", states.text)
# #                             if states.text == column_value:
# #                                 self.driver.execute_script("arguments[0].click();", states)
# #                                 break
# #                     if field_name == 'Aledade Practice Type':
# #                         element.click()
# #                         list_of_practices = keen_create.select_options_in_list()
# #                         for practice_type in list_of_practices:
# #                             if practice_type.text == column_value:
# #                                 self.driver.execute_script("arguments[0].click();", practice_type)
# #                                 break
# #                     if field_name == 'Accepted Carriers':
# #                         print("Accepted carriers are select")
# #                         list_of_options = keen_create.select_options_type()
# #                         for carriers in list_of_options:
# #                             if carriers.text == column_value:
# #                                 self.driver.execute_script("arguments[0].click();", carriers)
# #                                 keen_create.click_move_to_chosen()
# #                                 print("Accepted carriers are selected")
# #                 else:
# #                     element.send_keys(column_value)
# #         # self.log.info("****Assosicating the Plan to a Member****")
# #         # keen_create.save_button_Add()
# #         # action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
# #         # success_message_of_records = keen_create.success_message()
# #         # assert success_message_of_records.is_displayed(), "Record is not saved"
# #         # self.number.test_write_result_in_to_excel_sheet(row_number, "Plans", "M")
# #
# #
# #     def test_medications(self):
# #         keen = Create_capture_member_details(self.driver)
# #         action = ActionChains(self.driver)
# #         action_utils = ActionUtils(self.driver)
# #         lead = keen.select_member()
# #         lead[1].click()
# #         WebDriverWait(self.driver,20).until(EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
# #         keen.Capture_Full_Member()
# #         keen.Medication_option()
# #         keen.click_new()
# #         time.sleep(3)
# #         keen.medication_search()
# #         self.log.info("***** Click on New Ceration *****")
# #         action_utils.wait_for_element((Create_capture_member_details.new_creation))
# #         keen.click_new_member()
# #         pop_of_new_medication_directory = keen.pop_up_Newcreation()
# #         if pop_of_new_medication_directory.text == "New Medication List":
# #             assert True
# #         else:
#             assert False
#         self.log.info("***** Entering the test data *****")
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_medication[row_number]
#         column_field_mapping = {
#             'Name': 'Name',
#             'Branded Generic': 'Branded Generic',
#             'Drug Form': 'Drug Form',
#             'Strength': 'Strength',
#             'Strength_units': 'Strength_units', 'Packaging': 'Packaging', 'Daily Frequency': 'Daily Frequency',
#             'Daily Quantity': 'Daily Quantity', 'Valid Until': 'Valid Until', 'Refill quantity': 'Refill quantity',
#             'Refill frequency': 'Refill frequency',
#             }
#         field_locators = {
#             'Name': (Create_capture_member_details. Field_01),
#             'Branded Generic': (Create_capture_member_details.Field_S_01),
#             'Drug Form': (Create_capture_member_details.Field_S_02),
#             'Strength': (Create_capture_member_details. Field_02),
#             'Strength_units': (Create_capture_member_details. Field_03),
#             'Packaging': (Create_capture_member_details. Field_04),
#             'Daily Frequency': (Create_capture_member_details. Field_05),
#             'Daily Quantity': (Create_capture_member_details. Field_06),
#             'Valid Until': (Create_capture_member_details.medication_ValidUntil),
#             'Refill quantity': (Create_capture_member_details. Field_08),
#             'Refill frequency': (Create_capture_member_details.Field_S_03),
#         }
#         for cell in data_row:
#             column_name = sheet_medication.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     print("a tag is present in elements")
#                     if field_name == 'Branded Generic':
#                         self.log.info("****** Branded field should be selected *****")
#                         print(field_name,"field is in medications")
#                         element.click()
#                         list_Brand = keen.select_options_in_list()
#                         print("length of list brand:", len(list_Brand))
#                         for brand in list_Brand:
#                             print("list of brands:",brand.get_attribute('title'))
#                             if brand.get_attribute('title') == column_value:
#                                 print("Brand value is matched")
#                                 self.driver.execute_script("arguments[0].click();", brand)
#                                 print("Band value is selected")
#                                 break
#                     if field_name == 'Drug Form':
#                         self.log.info("****** Drug from field should be selected *****")
#                         print(field_name,"field is in medications")
#                         print("Drug column value:", column_value)
#                         element.click()
#                         # action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
#                         WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(Create_capture_member_details.options_in_list))
#                         list_type_drug = keen.select_options_in_list()
#                         print("length of drug:",len(list_type_drug))
#                         for drug in list_type_drug:
#                             print("list of drug:", drug.get_attribute('title'))
#                             if drug.get_attribute('title') == column_value:
#                                 print("drug value is present")
#                                 # self.driver.execute_script("arguments[0].click();", drug)
#                                 action.move_to_element(drug).click().perform()
#                                 print("drug value is Selected")
#                                 break
#                     if field_name == 'Refill frequency':
#                         self.log.info("****** Refill frequency field should be selected *****")
#                         print(field_name,"field is in medications")
#                         element.click()
#                         # action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
#                         WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located(Create_capture_member_details.options_in_list))
#                         list_refill_frequency = keen.select_options_in_list()
#                         print("length of refill:", len(list_refill_frequency))
#                         for refill in list_refill_frequency:
#                             print("list of refill:", refill.get_attribute('title'))
#                             if refill.get_attribute('title') == column_value:
#                                 print("refill value is present")
#                                 self.driver.execute_script("arguments[0].click();",refill)
#                                 print("refill value is selected")
#                                 break
#                 else:
#                     element.send_keys(column_value)
#
#     def test_hospitals(self):
#         keen = Create_capture_member_details(self.driver)
#         action = ActionChains(self.driver)
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.select_hospitals))
#         keen.click_hospitals()
#         action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
#         pop_up_of_Members_hospitals = keen.pop_up()
#         assert pop_up_of_Members_hospitals.text == "Member's hospitals","Member's hospitals popup is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         pop_up_of_New_Members_hospital = keen.pop_up_of_New_Members()
#         assert pop_up_of_New_Members_hospital.text == "New Member's hospital", "New Member's hospital is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.new_hospital))
#         keen.click_Hospital_directory()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
#         pop_up_of_new_hospital_directory = keen.pop_up_Newcreation()
#         print(pop_up_of_new_hospital_directory.text)
#         assert pop_up_of_new_hospital_directory.text == "New Hospital and health system directory","New Hospital and health system directory pop is not matched"
#         self.log.info("***** Entering the test data *****")
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_hospitals[row_number]
#         column_field_mapping = {
#             'Hospital_Name': 'Hospital_Name',
#             'Hospital_location': 'Hospital_location',
#             'Address_line_1': 'Address_line_1',
#             'City': 'City',
#             'State': 'State', 'Zipcode': 'Zipcode', 'NPI': 'NPI',
#             'TaxID': 'TaxID', 'Status': 'Status', 'Phone': 'Phone',
#             'Contact_name': 'Contact_name','Contact_email': 'Contact_email','Contact _phone' : 'Contact _phone',
#             'Website' : 'Website'
#         }
#         field_locators = {
#             'Hospital_Name': (Create_capture_member_details.Field_01),
#             'Hospital_location': (Create_capture_member_details.hospital_location),
#             'Address_line_1': (Create_capture_member_details.hospital_addressline_1),
#             'City': (Create_capture_member_details.hospital_city),
#             'State': (Create_capture_member_details.Field_S_01),
#             'Zipcode': (Create_capture_member_details.hospital_zipcode),
#             'NPI': (Create_capture_member_details.hospital_npi),
#             'TaxID': (Create_capture_member_details.hospital_taxid),
#             'Status': (Create_capture_member_details.Field_S_02),
#             'Phone': (Create_capture_member_details.hospital_phone),
#             'Contact_name': (Create_capture_member_details.hospital_contactname),
#             'Contact_email':(Create_capture_member_details.hospital_contactemail),
#             'Contact _phone': (Create_capture_member_details.hospital_contactphone),
#             'Website' : (Create_capture_member_details.hospital_website)
#         }
#         for cell in data_row:
#             column_name = sheet_hospitals.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     print("a tag is present in elements")
#                     if field_name == 'State':
#                         element.click()
#                         list_of_states = keen.select_options_in_list()
#                         for states in list_of_states:
#                             if states.text == column_value:
#                                 action.move_to_element(states).click().perform()
#                                 break
#                     if field_name == 'Status':
#                         element.click()
#                         list_of_status = keen.select_options_in_list()
#                         for status in list_of_status:
#                             if status.text == column_value:
#                                 action.move_to_element(status).click().perform()
#                                 break
#                 else:
#                     element.send_keys(column_value)
#
#     def test_physicians(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.click_physicians))
#         keen.select_physicians()
#         action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
#         pop_up_of_Members_hospitals = keen.pop_up()
#         assert pop_up_of_Members_hospitals.text == "Member's Physicians", "Member's Physicians popup is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         pop_up_of_New_Members_physicians = keen.pop_up_of_New_Members()
#         assert pop_up_of_New_Members_physicians.text == "New Member's physician","New Member's physician popup is not matched"
#         keen.click_physician_directory()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         pop_up_of_new_physicians = keen.pop_up_Newcreation()
#         assert pop_up_of_new_physicians.text == "New Physician directory","New Physician directory popup is not matched"
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_physicians[row_number]
#         column_field_mapping = {
#             'Last Name': 'Last Name',
#             'First name': 'First name',
#             'Address line': 'Address line',
#             'City': 'City',
#             'State': 'State', 'Zip code': 'Zip code', 'NPI': 'NPI',
#             'TaxID': 'TaxID', 'Status': 'Status', 'Phone': 'Phone',
#             'Specialty': 'Specialty', 'Email': 'Email', 'Sub_Speciality': 'Sub_Speciality',
#         }
#         field_locators = {
#             'Last Name': (Create_capture_member_details.Field_01),
#             'First name': (Create_capture_member_details.Field_02),
#             'NPI': (Create_capture_member_details.Field_03),
#             'Address line': (Create_capture_member_details.Field_D_01),
#             'City': (Create_capture_member_details.Field_D_03),
#             'Phone': (Create_capture_member_details.Field_04),
#             'State': (Create_capture_member_details.Field_SD_01),
#             'Zip code': (Create_capture_member_details.Field_D_04),
#             'TaxID': (Create_capture_member_details.hospital_taxid),
#             'Status': (Create_capture_member_details.Field_S_02),
#             'Specialty': (Create_capture_member_details.moveto_subspecialty),
#             'Email': (Create_capture_member_details.Field_05),
#             'Sub_Speciality': (Create_capture_member_details.moveto_subspecialty),
#         }
#         for cell in data_row:
#             column_name = sheet_physicians.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     if field_name == 'State':
#                         element.click()
#                         action_utils.wait_for_elements((Create_capture_member_details.options_in_list))
#                         list_states = keen.select_options_in_list()
#                         for states in list_states:
#                             print(states.text)
#                             if states.text == column_value:
#                                 states.click()
#                                 # action.move_to_element(states).click().perform()
#                                 break
#                 elif element.tag_name == 'div':
#                     if field_name == 'Specialty':
#                         list_specality = keen.edit_superspecialty()
#                         for specality in list_specality:
#                             if specality.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();",specality)
#                                 break
#                         keen.click_move_to_chosen()
#                     if field_name == 'Sub_Speciality':
#                         list_subspecialty = keen.edit_Subspecialty()
#                         for subspecialty in list_subspecialty:
#                             if subspecialty.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();",subspecialty)
#                                 break
#                         keen.Click_Move_to_choosen_2()
#                 else:
#                     element.send_keys(column_value)
#
#     def test_pharmacies(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.pharmacies))
#         keen.select_pharmacies()
#         action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
#         pop_up_of_Members_hospitals = keen.pop_up()
#         assert pop_up_of_Members_hospitals.text == "Member's Pharmacies", "Member's Pharmacies popup is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         pop_up_pharmacies = keen.pop_up_of_New_Members()
#         print(pop_up_pharmacies.text)
#         assert pop_up_pharmacies.text == "New Member's pharmacy","New Member's pharmacy popup is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.search_pharmacy))
#         keen.pharmacy_directory()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
#         pop_up_New_Pharmacy_directory = keen.pop_up_Newcreation()
#         assert pop_up_New_Pharmacy_directory.text == "New Pharmacy directory","New Pharmacy directory popup is not matched"
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_pharmacy[row_number]
#         column_field_mapping = {
#             'Pharmacy name': 'Pharmacy name',
#             'Address Line1': 'Address Line1',
#             'Phone': 'Phone',
#             'City': 'City',
#             'State': 'State', 'Zipcode': 'Zipcode','Status': 'Status',
#             'Pharmacy chain': 'Pharmacy chain', 'Mail Order': 'Mail Order',
#         }
#         field_locators = {
#             'Pharmacy name': (Create_capture_member_details.Field_01),
#             'Address Line1': (Create_capture_member_details.Field_D_01),
#             'City': (Create_capture_member_details.Field_D_03),
#             'Phone': (Create_capture_member_details.Field_02),
#             'State': (Create_capture_member_details.Field_SD_01),
#             'Zipcode': (Create_capture_member_details.Field_D_04),
#             'Status': (Create_capture_member_details.Field_S_03),
#             'Pharmacy chain': (Create_capture_member_details.Field_S_01),
#             'Mail Order': (Create_capture_member_details.Field_S_02),
#         }
#         for cell in data_row:
#             column_name = sheet_pharmacy.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     if field_name == 'Pharmacy chain':
#                         self.log.info("***** Pharmacy chain field is present *****")
#                         element.click()
#                         self.log.info("***** Pharmacy chain field is selected *****")
#                         list_of_chains = keen.select_options_in_list()
#                         self.log.info("***** Options for pharmacy chains  field *****")
#                         for pharmacy_chains in list_of_chains:
#                             if pharmacy_chains.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();",pharmacy_chains)
#                                 self.log.info("***** Required Option is selected for pharmacy chain field *****")
#                                 break
#                     if field_name == 'Mail Order':
#                         self.log.info("***** Mail order field is present *****")
#                         element.click()
#                         self.log.info("***** Mail order field is selected *****")
#                         list_mail_order = keen.select_options_in_list()
#                         for mail in list_mail_order:
#                             self.log.info("***** Options for Pharmacy chain field *****")
#                             if mail.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();",mail)
#                                 self.log.info("***** Required Option is selected of Pharmacy chain field *****")
#                                 break
#                     if field_name == 'State':
#                         self.log.info("***** State field is present *****")
#                         element.click()
#                         self.log.info("***** State field is selected *****")
#                         states = keen.select_options_in_list()
#                         self.log.info("***** Options for state field *****")
#                         for pharmacy_state in states:
#                             if pharmacy_state.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();",pharmacy_state)
#                                 self.log.info("***** Required Option is selected for State field *****")
#                                 break
#                     if field_name == 'Status':
#                         self.log.info("***** Status field is present *****")
#                         element.click()
#                         self.log.info("***** Status field is selected *****")
#                         status = keen.select_options_in_list()
#                         self.log.info("***** Options for status field *****")
#                         for pharmacy_status in status:
#                             if pharmacy_status.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();",pharmacy_status)
#                                 self.log.info("***** Required Option is selected for Status field *****")
#                                 break
#                 else:
#                     self.log.info("***** Entering the test data to the respected fields *****")
#                     element.send_keys(column_value)
#
#     def test_events(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.select_event))
#         keen.select_events()
#         pop_up_outbound_organization = keen.pop_up()
#         assert pop_up_outbound_organization.text == "Member's Event","Members event popup is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         pop_of_new_outbound = keen.pop_up_of_New_Members()
#         assert pop_of_new_outbound.text == "New Member at event","New Member at Event is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.keen_event))
#         keen.click_keen_event()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
#         pop_up_new_organization_creation = keen.pop_up_Newcreation()
#         assert pop_up_new_organization_creation.text == "New Keen Event","New Keen Event is not matched"
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_event[row_number]
#         column_field_mapping = {
#             'Event_Name': 'Event_Name',
#             'Address Line 1': 'Address Line 1',
#             'Phone': 'Phone',
#             'City': 'City',
#             'State': 'State', 'Zipcode': 'Zipcode', 'Status': 'Status',
#             'Start date': 'Start date', 'Start Time': 'Start Time',
#             'End date' : 'End date','End Time' : 'End Time',
#             'Report date' : 'Report date','Carriers submitted to' : 'Carriers submitted to',
#             'Type': 'Type','Number_of_attendees' : 'Number_of_attendees','RegistrationCost': 'RegistrationCost','FoodCost' : 'FoodCost'
#
#         }
#         field_locators = {
#             'Event_Name': (Create_capture_member_details.Field_01),
#             'Address Line 1': (Create_capture_member_details.Field_D_01),
#             'City': (Create_capture_member_details.Field_D_03),
#             'Phone': (Create_capture_member_details.Field_D_05),
#             'State': (Create_capture_member_details.Field_SD_01),
#             'Zipcode': (Create_capture_member_details.Field_D_04),
#             'Status': (Create_capture_member_details.status_event),
#             'Start date': (Create_capture_member_details.start_date),
#             'Start Time': (Create_capture_member_details.start_time),
#             'End date' : (Create_capture_member_details.End_date),
#             'End Time' : (Create_capture_member_details.End_time),
#             'Report date' : (Create_capture_member_details.reportdate_events),
#             'Carriers submitted to' : (Create_capture_member_details.carrires),
#             'Type' : (Create_capture_member_details.type_avaliable),
#             'Number_of_attendees' : (Create_capture_member_details.Field_02),
#             'RegistrationCost': (Create_capture_member_details.Field_03),
#             'FoodCost' : (Create_capture_member_details.Field_04)
#
#         }
#         for cell in data_row:
#             column_name = sheet_event.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     if field_name == 'State':
#                         self.log.info("***** State field is present *****")
#                         element.click()
#                         self.log.info("***** State field is selected *****")
#                         states = keen.select_options_in_list()
#                         self.log.info("***** Options for state field *****")
#                         for events_state in states:
#                             if events_state.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", events_state)
#                                 self.log.info("***** Required Option is selected for State field *****")
#                                 break
#                     if field_name == 'Status':
#                         self.log.info("***** Status field is present *****")
#                         element.click()
#                         self.log.info("***** Status field is selected *****")
#                         status = keen.select_options_in_list()
#                         self.log.info("***** Options for status field *****")
#                         for event_status in status:
#                             if event_status.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", event_status)
#                                 self.log.info("***** Required Option is selected for Status field *****")
#                                 break
#                 elif element.tag_name == 'div':
#                     if field_name == 'Type':
#                         list_types = keen.select_optionsType()
#                         for types in list_types:
#                             if types.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", types)
#                                 keen.click_type_choosen()
#                                 break
#                     if field_name == 'Carriers submitted to':
#                         list_carriers = keen.select_optionsType()
#                         for carriers in list_carriers:
#                             if carriers.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", carriers)
#                                 break
#                         keen.click_carrier_choosen()
#
#
#                 else:
#                     self.log.info("***** Entering the test data to the respected fields *****")
#                     element.send_keys(column_value)
#
#
#     def test_related_persons(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         action_utils.wait_for_element((Create_capture_member_details.Member_details))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.caregiver))
#         keen.click_caregiver_option()
#         pop_up_caregiver = keen.pop_up()
#         assert pop_up_caregiver.text == "Related Person's List", "Related Person's List popup is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         pop_of_new_caregiver = keen.pop_up_of_New_Members()
#         assert pop_of_new_caregiver.text == "New Related Person", "New Related Person is not matched"
#         action_utils.wait_for_element((Create_capture_member_details.keen_event))
#         keen.click_keen_event()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
#         pop_up_new_caregiver = keen.pop_up_Newcreation()
#         assert pop_up_new_caregiver.text == "New Caregiver Directory", "New Caregiver Directory is not matched"
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_related[row_number]
#         column_field_mapping = {
#             'Caregiver Name': 'Caregiver Name',
#             'Date of Birth': 'Date of Birth',
#             'Email': 'Email',
#             'Phone': 'Phone',
#             'State': 'State', 'Zipcode': 'Zipcode', 'Status': 'Status',
#             'Address line 1': 'Address line 1', 'Relationship': 'Relationship',
#             'City': 'City', 'Phone_type': 'Phone_type',
#             'other_phone': 'other_phone',
#         }
#         field_locators = {
#             'Caregiver Name': (Create_capture_member_details.Field_01),
#             'Date of Birth': (Create_capture_member_details.Field_D_01),
#             'Email': (Create_capture_member_details.Field_D_03),
#             'Phone': (Create_capture_member_details.Field_D_05),
#             'State': (Create_capture_member_details.Field_SD_01),
#             'Zipcode': (Create_capture_member_details.Field_D_04),
#             'Status': (Create_capture_member_details.status_event),
#             'Address line 1': (Create_capture_member_details.start_date),
#             'Relationship': (Create_capture_member_details.start_time),
#             'City': (Create_capture_member_details.End_date),
#             'Phone_type': (Create_capture_member_details.End_time),
#             'other_phone': (Create_capture_member_details.reportdate_events),
#         }
#         for cell in data_row:
#             column_name = sheet_related.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     if field_name == 'Relationship':
#                         element.click()
#                         list_of_relations = keen.select_options_in_list()
#                         for relation in list_of_relations:
#                             if relation.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", relation)
#                                 break
#                     if field_name == 'State':
#                         list_of_states = keen.select_options()
#                         for state in list_of_states:
#                             if state.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", state)
#                                 break
#                     if field_name == 'Phone_type':
#                         list_of_phonetypes = keen.select_options()
#                         for phone_type in list_of_phonetypes:
#                             if phone_type.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", phone_type)
#                                 break
#                 else:
#                     element.send_keys(column_value)
#     def  test_campaigns(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.click_campaigns))
#         keen.select_campaigns()
#         action_utils.wait_for_element((Create_capture_member_details.click_campaigns))
#         pop_up_of_Members_campaigns = keen.pop_up()
#         if pop_up_of_Members_campaigns.text == "Member's Campaign":
#             assert True
#         else:
#             assert False
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
#         pop_up_of_New_Members_campaigns = keen.pop_up_of_New_Members()
#         print(pop_up_of_New_Members_campaigns.text)
#         if pop_up_of_New_Members_campaigns.text == "New Member campaign":
#             assert True
#         else:
#             assert False
#         action_utils.wait_for_element((Create_capture_member_details.campaign))
#         keen.search_keen_campaign()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         pop_up_of_new_campaigns = keen.pop_up_Newcreation()
#         if pop_up_of_new_campaigns.text == "New Keen campaign":
#             assert True
#         else:
#             assert False
#
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_campaign[row_number]
#         column_field_mapping = {
#             'Parent_organization_Name': 'Parent_organization_Name',
#             # 'Available Type': 'Available Type',
#             # 'Available Type1': 'Available Type1',
#             'Available Type2': 'Available Type2',
#             'Start Date': 'Start Date', 'Start Time': 'Start Time', 'End Date': 'End Date',
#             'End Time': 'End Time',
#         }
#         field_locators = {
#             'Parent_organization_Name': (Create_capture_member_details.Field_01),
#             'Available Type': (Create_capture_member_details.type_avaliable),
#             # 'Available Type1': (Create_capture_member_details.type_avaliable),
#             # 'Available Type2': (Create_capture_member_details.type_avaliable),
#             'Start Date': (Create_capture_member_details.Field_SD_01),
#             'Start Time': (Create_capture_member_details.Field_D_04),
#             'End Date': (Create_capture_member_details.status_event),
#             'End Time': (Create_capture_member_details.start_date),
#         }
#         for cell in data_row:
#             column_name = sheet_campaign.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'div':
#                     if field_name == 'Available Type':
#                         list_of_types = keen.select_options_in_list()
#                         for type in list_of_types:
#                             if type.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", type)
#                                 break
#                 else:
#                     element.send_keys(column_value)
#
#
#     def test_organization(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         lead = keen.select_member()
#         lead[1].click()
#         WebDriverWait(self.driver, 20).until(
#             EC.visibility_of_element_located((Create_capture_member_details.Member_details)))
#         keen.Capture_Full_Member()
#         action_utils.wait_for_element((Create_capture_member_details.outbound_organization))
#         keen.select_outbound_organization()
#         action_utils.wait_for_element((Create_capture_member_details.Members_Popup))
#         pop_up_outbound_organization = self.keen.pop_up()
#         if pop_up_outbound_organization.text == "Outbound Referral Organization":
#             assert True
#         else:
#             assert False
#         action_utils.wait_for_element((Create_capture_member_details.new))
#         keen.click_new()
#         action_utils.wait_for_element(())
#         pop_of_new_outbound = keen.pop_up_of_New_Members()
#         if pop_of_new_outbound.text == "New Outbound Referral: Organization":
#             assert True
#         else:
#             assert False
#         action_utils.wait_for_element((Create_capture_member_details.search_community))
#         keen.search_Community_and_senior_organization()
#         action_utils.wait_for_element((Create_capture_member_details.new_creation))
#         keen.click_new_member()
#         action_utils.wait_for_element((Create_capture_member_details.pop_up_creation))
#         pop_up_new_organization_creation = keen.pop_up_Newcreation()
#         print(pop_up_new_organization_creation.text)
#         if pop_up_new_organization_creation.text == "New Community and senior organization":
#             assert True
#         else:
#             assert False
#         row_number = 5
#         print("Row number:", row_number)
#         data_row = sheet_event[row_number]
#         column_field_mapping = {
#             'Parent_organization_Name': 'Parent_organization_Name',
#             'Address Line 1': 'Address Line 1',
#             'Phone': 'Phone',
#             'City': 'City',
#             'State': 'State', 'Zipcode': 'Zipcode', 'Status': 'Status',
#             'TaxID': 'TaxID', 'Email': 'Email',
#             'Website': 'Website',
#
#         }
#         field_locators = {
#             'Parent_organization_Name': (Create_capture_member_details.Field_01),
#             'Address line 1': (Create_capture_member_details.Field_D_01),
#             'City': (Create_capture_member_details.Field_D_03),
#             'Phone': (Create_capture_member_details.Field_D_05),
#             'State': (Create_capture_member_details.Field_SD_01),
#             'Zipcode': (Create_capture_member_details.Field_D_04),
#             'Status': (Create_capture_member_details.status_event),
#             'TaxID': (Create_capture_member_details.start_date),
#             'Email': (Create_capture_member_details.start_time),
#             'Website': (Create_capture_member_details.End_date),
#
#         }
#         for cell in data_row:
#             column_name = sheet_event.cell(row=2, column=cell.column).value
#             print("Column name:", column_name)
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 action_utils.wait_for_element((locator))
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'a':
#                     if field_name == 'State':
#                         list_of_states = keen.select_options_in_list()
#                         for states in list_of_states:
#                             if states.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", states)
#                                 break
#                     if field_name == 'Status':
#                         list_status = keen.select_options_in_list()
#                         for status in list_status:
#                             if status.text == column_value:
#                                 self.driver.execute_script("arguments[0].click();", status)
#                                 break
#                 else:
#                     element.send_keys(column_value)
#
#
#
#     def test_value(self):
#         keen = Create_capture_member_details(self.driver)
#         self.driver.execute_script("scroll(0, 150);")
#         action_utils = ActionUtils(self.driver)
#         keen_account=Keen_Account_creation(self.driver)
#         lead = keen.select_member()
#         # lead[1].click()
#         for leads in lead:
#             if leads.text == 'Wrong Test':
#                 leads.click()
#         action_utils.wait_for_element((Keen_Account_creation.address_details))
#         keen_account.click_address_Details()
#         action_utils.wait_for_element((Keen_Account_creation.enter_county_newcreation))
#         y=keen_account.enter_county_newlead()
#         get_text=y.get_attribute('value')
#         print(get_text)
#
#
#
#
#
#
#
#
#
#
#         # age= BaseTest()
#         # actionutils=ActionUtils(self.driver)
#         # keen=Create_capture_member_details(self.driver)
#         # leads=keen.select_member()
#         # for members in leads:
#         #     if members.text == "Test Williams":
#         #        members.click()
#         # keen_account=Keen_Account_creation(self.driver)
#         # member_age=keen_account.validation_of_DoB()
#         # print("member age:",member_age)
#         # member=age.calculate_age(member_age)
#         # print("Days months years:",member)
#         # list=self.driver.find_element(By.XPATH,"//label[contains(text(),'days')]")
#         # print("SF Memberss age:",list.text)
#         # assert member in  list.text," date of birth is matched"
#         # for elements in list:
#         #     print(elements.text)
# class Test(Test_login):
#     def test_login(self):
#         action_utils=ActionUtils(self.driver)
#         row_number = 4
#         data_row = sheet[row_number]
#         column_field_mapping = {
#             'first_Name': 'first_Name', 'Middle_Name': 'MiddleName', 'Last_Name': 'Last_Name',
#             'DoB': 'DoB', 'Email': 'Email', 'PTC': 'PTC', 'SOA': 'SOA', 'Phone': 'Phone',
#             'Street_Address': 'Street_Address',
#             'Gender': 'Gender', 'Source': 'Source', 'status': 'Status', 'Origin': 'Origin', 'Language': 'Language',
#             'MedicareID': 'MedicareID', 'MedcaidID': 'MedcaidID',
#             'Part_A enrollment date': 'Part_A enrollment date', 'Plan_enrollment date': 'Plan_enrollment date',
#             'Part_B enrollment date': 'Part_B enrollment date',
#             'Medicaid_status_verification_date': 'Medicaid_status_verification_date',
#             'SSN': 'SSN', 'Zipcode': 'Zipcode', 'City': 'City', 'State_Newcreation': 'State',
#             'Member_County': 'Member_County', 'Addressline2': 'Addressline2', 'PTC popup': 'PTC popup',
#             'Other_permission': 'Other_permission',
#         }
#         field_locators = {
#             'first_Name': ((By.XPATH, "//input[@name='FirstName']")), 'DoB': (Keen_Account_creation.enter_dob),
#             'MiddleName': ((By.XPATH, "//input[@name='MiddleName']")),
#             'Last_Name': ((Keen_Account_creation.enter_lastName)), 'Email': (Keen_Account_creation.enter_email),
#             'PTC': (Keen_Account_creation.enter_PTC),
#             'SOA': (Keen_Account_creation.enter_SOA), 'Phone': (Keen_Account_creation.enter_phone),
#             'Street_Address': (Keen_Account_creation.enter_address),
#             'Gender': (Keen_Account_creation.select_gender), 'Source': ((By.XPATH, "//button[@name='AccountSource']")),
#             'Origin': ((By.XPATH, "(//lightning-icon[@title='medicare detail'])[1]")),
#             'MedicareID': ((By.XPATH, "(//lightning-icon[@title='medicare detail'])[2]")),
#             'MedcaidID': (Keen_Account_creation.medicaid_id),
#             'Part_A enrollment date': (Keen_Account_creation.part_A),
#             'Plan_enrollment date': (Keen_Account_creation.enrollment_date),
#             'Part_B enrollment date': (Keen_Account_creation.part_B),
#             'Medicaid_status_verification_date': (Keen_Account_creation.verification_date),
#             'SSN': (Keen_Account_creation.SSN), 'Status': ((By.XPATH, "//button[@name='Status__c']")),
#             'Language': (Keen_Account_creation.options_in_list),
#             'Addressline2': (Keen_Account_creation.enter_newcreationaddress_line_2),
#             'Member_County': (Keen_Account_creation.enter_county_newcreation),
#             'Zipcode': (Keen_Account_creation.enter_zipcode_newcreation),
#             'City': (Keen_Account_creation.enter_city_newcreation), 'State': (Keen_Account_creation.click_state),
#             'PTC popup': (Keen_Account_creation.ptc_popup),
#             'Other_permission': (Keen_Account_creation.other_permission)
#
#         }
#         keen = Keen_Account_creation(self.driver)
#         action_utils.wait_for_element((Keen_Account_creation.new_button))
#         keen.New()
#         time.sleep(10)
#         # action_utils.wait_for_element((Keen_Account_creation.enter_firstName))
#         for cell in data_row:
#             column_name = sheet.cell(row=1, column=cell.column).value
#             if column_name in column_field_mapping:
#                 field_name = column_field_mapping[column_name]
#                 print("mapping is done")
#                 column_value = cell.value
#                 print("input:", column_value)
#                 locator = field_locators[field_name]
#                 element = self.driver.find_element(*locator)
#                 if element.tag_name == 'lightning-icon':
#                     if field_name == 'MedicareID':
#                         print("Medicare detail popup is selecetd")
#                         keen.select_medication_details()
#                         keen.enter_medicare_ID().send_keys(column_value)

    # def test(self):
    #     keen=Keen_Account_creation(self.driver)
    #     action_utils=ActionUtils(self.driver)
    #     action_utils.wait_for_element((Keen_Account_creation.new_button))
    #     keen.New()
    #     workbook = load_workbook(path)
    #
    #     # Access the desired sheet
    #     sheet = workbook['Account_Creation']  # Replace 'Sheet1' with your sheet name
    #
    #     # Define the row number to retrieve (e.g., row 3)
    #     row_number = 3
    #
    #     # Retrieve the data from the specified row
    #     data_row = sheet[row_number]
    #
    #     # Retrieve the mapping data from the Excel file
    #     column_field_mapping = {
    #         'first_Name': 'first_Name',
    #         'Last_Name': 'Last_Name',
    #         'Source': 'Source',
    #         # Add more mappings as needed
    #     }
    #     field_locators={'first_Name': ((By.XPATH, "//input[@name='FirstName']")), 'DoB': (Keen_Account_creation.enter_dob),
    #         'MiddleName': ((By.XPATH, "//input[@name='MiddleName']")),
    #         'Last_Name': ((Keen_Account_creation.enter_lastName)), 'Email': (Keen_Account_creation.enter_email),
    #         'PTC': (Keen_Account_creation.enter_PTC),
    #         'SOA': (Keen_Account_creation.enter_SOA), 'Phone': (Keen_Account_creation.enter_phone),
    #         'Street_Address': (Keen_Account_creation.enter_address),
    #         'Gender': (Keen_Account_creation.select_gender), 'Source': ((By.XPATH, "//button[@name='AccountSource']")),
    #
    #     }
    #
    #     option_field_mapping = {
    #         'Lead': ['Source from', 'Practice from', 'Event from'],
    #         'Option 2': ['Field A', 'Field B', 'Field C'],
    #         # Add more mappings as needed
    #     }
    #
    #     # Step 2: Get the selected option from the Excel sheet
    #     selected_option = sheet.cell(row=row_number, column=status_column).value
    #
    #     # Step 3: Check if the selected option exists in the mapping
    #     if selected_option in option_field_mapping:
    #         # Step 4: Retrieve the associated column names
    #         column_names = option_field_mapping[selected_option]
    #
    #         # Step 5: Fill the additional fields with the retrieved values
    #         for column_name in column_names:
    #             column_value = sheet.cell(row=row_number, column=column_mapping[column_name]).value
    #             # Fill the field with the corresponding column value
    #             element = driver.find_element_by_name(column_name)
    #             element.send_keys(column_value)
    #             # Assuming 'selected_option' contains the selected status option
    #             selected_option = "Lead"
    #
    #             # Retrieve the column names for the selected option from option_field_mapping
    #             column_names = option_field_mapping[selected_option]
    #
    #             # Iterate over the column names and compare with field names
    #             for column_name in column_names:
    #                 # Assuming 'field_name' represents the field name of the form field
    #                 field_name = "Source from"
    #
    #                 if field_name == column_name:
    #                     # Retrieve the test data value for the column name from the Excel sheet or data source
    #                     test_data_value = get_test_data_value(column_name)
    #
    #                     # Fill the form field with the test data value
    #                     fill_form_field(field_name, test_data_value)
        # for cell in data_row:
        #     column_name = sheet.cell(row=1, column=cell.column).value
        #     if column_name in column_field_mapping:
        #         field_name = column_field_mapping[column_name]
        #         self.log.info(field_name)
        #         print("mapping is done")
        #         column_value = cell.value
        #         print("input:", column_value)
        #         locator = field_locators[field_name]
        #         element = self.driver.find_element(*locator)
        #         if element.tag_name == 'button':
        #             if field_name == 'Source':
        #                 element.click()
        #                 source = keen.select_source()
        #                 for option in source:
        #                     if option.get_attribute('title') == column_value:
        #                         print("clickable option:", column_value)
        #                         print("options are present")
        #                         self.driver.execute_script("arguments[0].click();", option)
        #                         break
        #         if column_value in source_options_mapping:
        #             option_mapping = source_options_mapping[column_value]
        #             for field, value in option_mapping.items():
        #                 if value is None:
        #                     # Retrieve the value from the Excel sheet based on the field name
        #                     value_cell = sheet.cell(row=row_number, column=sheet[field].column)
        #                     option_mapping[field] = value_cell.value
        #
        #         # Perform the necessary actions based on the selected option and field-value mapping
        #         if column_value == 'Community Event':
        #             event_field_value = source_options_mapping[column_value]['event_field']
        #             print(event_field_value)
        #             # Use the event_field_value to fill the corresponding field in the popup/form
        #
        #         elif column_value == 'task':
        #             task_field_value = source_options_mapping[column_value]['task_field']
        #             # Use the task_field_value to fill the corresponding field in the popup/form
        #
        #         elif column_value == 'practice':
        #             practice_field_value = source_options_mapping[column_value]['practice_field']
        #             # Use the practice_field_value to fill the corresponding field in the popup/form
        #         else:
        #             element.send_keys(column_value)
        #
        #         # Handle other options as needed


        # keen_Create = Create_capture_member_details(self.driver)
        # member=keen_Create.select_member()
        # member[0].click()
        # action_utils.wait_for_element((Keen_Account_creation.verify_email))
        # for cell in data_row:
        #     column_name = sheet.cell(row=1, column=cell.column).value
        #     if column_name in column_field_mapping:
        #         field_name = column_field_mapping[column_name]
        #         print("Available fields in SF medicare popup:", field_name)
        #         self.log.info(field_name)
        #         # print("mapping is done")
        #         column_value = cell.value
        #         # print("input:", column_value)
        #         locator = field_locators[field_name]
        #         try:
        #             element = self.driver.find_element(*locator)
        #             if element.tag_name == 'lightning-icon':
        #                 print("lightning-icon is present in elements")
        #                 if field_name == 'Origin':
        #                     element.click()
        #                     origin=keen.Country_of_origin().get_attribute('value')
        #                     assert origin == column_value,"Origin value is not matched"
        #                 if element.tag_name == 'div':
        #                     if field_name == 'Language':
        #                         print("Verifing the language value")
        #                         choosen_language=keen.choosen_language()
        #                         for language in choosen_language:
        #                              assert language.text == column_value,"Language is not matched"
        #                              break
        #                 if field_name == 'MedicareID':
        #                     element.click()
        #                     print("MedicareId is present in Sf")
        #                     # keen.select_medication_details()
        #                     try:
        #                         medicare = keen.enter_medicare_ID()
        #                         verify_medicareID = medicare.get_attribute("value")
        #                         assert verify_medicareID == column_value, "MedicareID is not matched"
        #                     except Exception as ex:
        #                         print(ex)
        #             else:
        #                 if element.text == column_value:
        #                      print("Test data is matched")
        #                 else:
        #                     print("Test data is not matched")
        #                 if field_name == 'SSN':
        #                     print("SSN is displayed")
        #                     attribute = self.driver.find_element(*Keen_Account_creation.medicare_popup)
        #                     value = attribute.get_attribute('title')
        #                     print("title value is:",value)
        #                     keen.close_medicaredetails_popup()
        #                 if field_name == 'Language':
        #                     attribute = self.driver.find_element(*Keen_Account_creation.medicare_popup)
        #                     value = attribute.get_attribute('title')
        #                     print("title value of language is:", value)
        #                     keen.close_medicaredetails_popup()
        #         except Exception as ex:
        #             print(ex)
        #             try:
        #                 if field_name == 'MedcaidID':
        #                     output=element.get_attribute('value')
        #                     assert output == column_value,"MedcaidId is not matched"
        #             except Exception as ex:
        #                 print(ex)
        #             try:
        #                 if field_name == 'Part_A enrollment date':
        #                     output_partA=element.get_attribute('value')
        #                     assert output_partA == column_value,"Part_A enrollment date is not matched"
        #             except Exception as ex:
        #                 print(ex)
        #             try:
        #                 if field_name == 'Plan_enrollment date':
        #                     output_plan = element.get_attribute('value')
        #                     assert output_plan == column_value, "Plan enrollment date is not matched"
        #             except Exception as ex:
        #                 print(ex)
        #             try:
        #                 if field_name == 'Part_B enrollment date':
        #                     output_part_B = element.get_attribute('value')
        #                     assert output_part_B == column_value, "Part_B enrollment date is not matched"
        #             except Exception as ex:
        #                 print(ex)
        #             try:
        #                 if field_name == 'Medicaid_status_verification_date':
        #                     output_Medicaid_status_date = element.get_attribute('value')
        #                     assert output_Medicaid_status_date == column_value, "Part_B enrollment date is not matched"
        #             except Exception as ex:
        #                 print(ex)
        #             try:
        #                 if field_name == 'SSN':
        #                     output_Medicaid_status_date = element.get_attribute('value')
        #                     assert output_Medicaid_status_date == column_value, "Part_B enrollment date is not matched"
        #             except Exception as ex:
        #                 print(ex)
#         # import openpyxl
#         # import random
#         workbook = openpyxl.load_workbook(path)
#         sheet = workbook['Account_Creation']
#         column_name = 'account_creation'
#         row_number = 6
# #                             for carrier in select_carrier:
#                                 print("Carrier name_Sf:",carrier.text)
#                                 if carrier.text == column_value:
#                                     ### For normal i.click() we got error like "Element-Intercepted Expection"
#                                     ## So that's why uisng Actions
#                                     self.driver.execute_script("arguments[0].click();", carrier)
#                                     break
#
#                     else:
#                         element.send_keys(column_value)
#         self.log.info("****Assosicating the Plan to a Member****")
#         keen_create.save_button_Add()
#         action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
#         success_message_of_records = keen_create.success_message()
#         assert success_message_of_records.is_displayed(),"Record is not saved"
#         self.number.test_write_result_in_to_excel_sheet(row_number,"Plans","M")

# from selenium.webdriver import ActionChains, Keys
# from Pages.Keen_Associate_capture_full_member_details import Associate_Capture_full_Member_details
# from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
# #         #
# #         # # Find the column index based on the column name
# #         # column_index = None
# #         # for column in sheet.iter_cols(min_row=1, max_row=1):
# #         #     print("column printing:",column)
# #         #     if column[0].value == column_name:
# #         #         column_index = column[0].column
# #         #         print("column _index:",column_index)
# #         #         break
# #         #
# #         # if column_index is None:
# #         #     print(f"Column '{column_name}' not found in the sheet.")
# #         # else:
# #         #     # Get the value from the specified row and column
# #         #     cell = sheet.cell(row=row_number, column=column_index)
# #         #     cell_value = cell.value
# #         #     print(f"Value in row {row_number}, column '{column_name}': {cell_value}")
# #         #     if cell_value == 'Yes':
# #         #         self.log.info("***** Account exists in Salesforce *****")
# #         #         self.driver.close()
# #         #         self.log.info("***** Closing the driver *****")
# #         #     else:
# #         #         self.log.info("***** New Account is creating *****")
# #         #         print("Record in not exists")
# #
# #
# #         # Close the workbook
# #         # workbook.close()
# #         # workbook = openpyxl.load_workbook(path)
# #         # worksheet = workbook[sheet]
# #         # column = 'AP'
# #         # print("account column is present")
# #         # account_creation_value = 'account_creation'  # Replace with the actual account_creation value
# #         # self.log.info("***** account_creation_value is present in column*****")
# #         # # Iterate over the rows in the account_creation column
# #         # for row in worksheet.iter_rows(min_row=2, values_only=True):  # Start from row 2, assuming headers are in row 1
# #         #     if row[0] == account_creation_value:  # Check if the account_creation value matches
# #         #         # Update the cell with 'yes'
# #         #         cell = worksheet.cell(row=row[row_account - 1].row,
# #         #                               column=worksheet[account_creation_column].column + 1)  # Next column
# #         #         cell.value = 'yes'
# #         #         self.log.info("***** writing yes in excell sheet*****")
# #         #         break
# #         #
# #         # # Save the changes to the workbook
# #         # workbook.save(path)
# #
# #     # option_field_mapping = {
# #     #     'Lead': ['Source from', 'Practice from', 'Event from'],
# #     #     'Option 2': ['Field A', 'Field B', 'Field C'],
# #     #     # Add more mappings as needed
# #     # }
# #     #
# #     # # Step 2: Get the selected option from the Excel sheet
# #     # selected_option = sheet.cell(row=row_number, column=status_column).value
# #     #
# #     # # Step 3: Check if the selected option exists in the mapping
# #     # if selected_option in option_field_mapping:
# #     #     # Step 4: Retrieve the associated column names
# #     #     column_names = option_field_mapping[selected_option]
# #     #
# #     #     # Step 5: Fill the additional fields with the retrieved values
# #     #     for column_name in column_names:
# #     #         column_value = sheet.cell(row=row_number, column=column_mapping[column_name]).value
# #     #         # Fill the field with the corresponding column value
# #     #         element = driver.find_element_by_name(column_name)
# #     #         element.send_keys(column_value)
# #     def test_parent_organization(self,row_number):
# #         keen=Create_capture_member_details(self.driver)
# #         print("Row number:", row_number)
# #         data_row = sheet_parent[row_number]
# #         column_field_mapping = {
# #             'Name': 'Name',
# #             'Address line 1': 'Address line 1',
# #             'TaxID': 'TaxID',
# #             'Email': 'Email',
# #             'City': 'City', 'Phone': 'Phone', 'State': 'State',
# #             'Zip code': 'Zip code', 'Website': 'Website', 'Status': 'Status',
# #             }
# #         field_locators = {
# #             'Name': (Create_capture_member_details.Field_01),
# #             'Address line 1': (Create_capture_member_details.Field_S_01),
# #             'TaxID': (Create_capture_member_details.Field_S_02),
# #             'Email': (Create_capture_member_details.Field_02),
# #             'City': (Create_capture_member_details.Field_03),
# #             'Phone': (Create_capture_member_details.Field_04),
# #             'State': (Create_capture_member_details.Field_05),
# #             'Zip code': (Create_capture_member_details.Field_06),
# #             'Website': (Create_capture_member_details.medication_ValidUntil),
# #             'Status': (Create_capture_member_details.Field_08),
# #
# #         }
# #         for cell in data_row:
# #             column_name = sheet_parent.cell(row=1, column=cell.column).value
# #             if column_name in column_field_mapping:
# #                 field_name = column_field_mapping[column_name]
# #                 print("Available fields in SF medicare popup:", field_name)
# #                 # self.log.info(field_name)
# #                 # print("mapping is done")
# #                 column_value = cell.value
# #                 # print("input:", column_value)
# #                 locator = field_locators[field_name]
# #                 element = self.driver.find_element(*locator)
# #                 if element.tag_name == 'a':
# #                     if field_name == 'State':
# #                         element.click()
# #                         self.log.info("***** Status field is clicked")
# #                         state_list=keen.select_options_in_list()
# #                         for states in state_list:
# #                             if states.text == column_value:
# #                                 self.driver.execute_script("arguments[0].click();", states)
# #                                 break
# #                     if field_name == 'Status':
# #                         element.click()
# #                         self.log.info("***** Status field is clicked")
# #                         status_list = keen.select_options_in_list()
# #                         for status in status_list:
# #                             if status.text == column_value:
# #                                 self.driver.execute_script("arguments[0].click();", status)
# #                                 self.log.info(column_value, ":***** is selected")
# #                                 break
# #                 else:
# #                     element.clear()
# #                     element.send_keys(column_value)
# import openpyxl
# path = 'C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\test_data\\Keen_Testdata.xlsx'
# workbook = openpyxl.load_workbook(path)
# sheet_name='Plans'
# class Test():
#     def retrieve_value(self,row_number,column_name,):
#         sheet_parent=workbook[sheet_name]
#         print("Row number:", row_number)
#         data_row = sheet_parent[row_number]
#         for cell in data_row:
#             if cell.column_letter== column_name and cell.value == "YES":
#                 print("column name retrieving the value:", cell.column_letter)
#                 Name = data_row[0].value
#                 print("Name:", Name)
#                 return Name
#     def one_retrieve_value(self, row_number, column_name, sheet_name,column_number):
#         sheet_parent = workbook[sheet_name]
#         print("Row number:", row_number)
#         data_row = sheet_parent[row_number]
#         for cell in data_row:
#             if cell.column_letter == column_name and cell.value == "YES":
#                 Name = data_row[column_number].value
#                 return Name
#     def record_verification(self, row_number, sheet_name, column_name):
#         workbook = openpyxl.load_workbook(path)
#         sheet = workbook[sheet_name]
#         # Find the column index based on the column name
#         column_index = None
#         for row in sheet.iter_rows(min_row=2, max_row=2):
#             for cell in row:
#                 if cell.value == column_name:
#                     column_index = cell.column_letter
#                     break
#             if column_index is not None:
#                 break
#
#         if column_index is None:
#             print(f"Column '{column_name}' not found in the sheet.")
#         else:
#             # Get the value from the specified row and column
#             cell = sheet[column_index + str(row_number)]
#             cell_value = cell.value
#             print(f"Value in row {row_number}, column '{column_name}': {cell_value}")
#             return cell_value
#     def test_accout(self):
#         row_account_number = 10
#         verify_account = self.record_verification(row_account_number, 'Account_Creation', 'Member_Created')
#         if verify_account == 'YES':
#             existing_account = self.one_retrieve_value(row_account_number,'AV','Account_Creation',2)
#             print("existing_account in sf:",existing_account)
#             # self.log.info("***** Member record is already in Salesforce *****")
#     def test_plans(self):
#         row_account_number = 10
#         verify_account = self.record_verification(row_account_number, 'Plans', 'Plans_Created')
#         if verify_account == 'YES':
#             existing_account = self.one_retrieve_value(row_account_number, 'Y','Plans',0)
#             print("existing_account in sf:", existing_account)

    # def test_validation_plans(self):
    #     import openpyxl
    #
    #     # Load the Excel file
    #     workbook = openpyxl.load_workbook('C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\test_data\\Keen_Testdata.xlsx')
    #
    #     # Specify the sheet name
    #     sheet_name = 'Plans'
    #
    #     # Specify the column letter where the organizations are located
    #     column_letter = 'D'
    #
    #     # Specify the organization you want to find
    #     organization_name = 'Test Organization'
    #
    #     # Access the sheet and the specified column
    #     sheet = workbook[sheet_name]
    #     column = sheet[column_letter]
    #
    #     # Iterate through the cells in the column and find the matching organization
    #     for row, cell in enumerate(column, start=1):
    #         if cell.value == organization_name:
    #             print(f"The organization '{organization_name}' is found at row {row}.")
    #             break
    #     else:
    #         print(f"The organization '{organization_name}' is not found in the Excel sheet.")


from utilities.action_utils import ActionUtils
from datetime import datetime


# def convert_date_to_string(date_str):
#     # Convert the input string to a datetime object
#     date = datetime.strptime(date_str, "%d/%m/%Y")
#
#     # Define the mappings for converting numbers and month names to words
#     numbers_mapping = {
#         "0": "zero",
#         "1": "one",
#         "2": "two",
#         "3": "three",
#         "4": "four",
#         "5": "five",
#         "6": "six",
#         "7": "seven",
#         "8": "eight",
#         "9": "nine"
#     }
#
#     month_mapping = {
#         1: "january",
#         2: "february",
#         3: "march",
#         4: "april",
#         5: "may",
#         6: "june",
#         7: "july",
#         8: "august",
#         9: "september",
#         10: "october",
#         11: "november",
#         12: "december"
#     }
#
#     # Extract the day, month, and year components from the date
#     day = numbers_mapping(date.strftime("%d")[0])+numbers_mapping[dat]
#     month = month_mapping[date.month]
#     year = numbers_mapping[date.strftime("%Y")[0]] + numbers_mapping[date.strftime("%Y")[3]]
#     print("year:",year)
#
#     # Construct the string in the desired format
#     result = day + month + year
#
#     return result


# Example usage
# date_string = "16/7/2033"
# result_string = convert_date_to_string(date_string)
# print(result_string)  # Out

from datetime import datetime

# from datetime import datetime
#
# def convert_date_to_string(date):
#     # Define mappings for converting numbers to words
#     numbers_mapping = {0:"zero",
#         1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
#         7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth",
#         13: "thirteenth", 14: "fourteenth", 15: "fifteenth", 16: "sixteenth", 17: "seventeenth",
#         18: "eighteenth", 19: "nineteenth", 20: "twentieth", 21: "twenty-first", 22: "twenty-second",
#         23: "twenty-third", 24: "twenty-fourth", 25: "twenty-fifth", 26: "twenty-sixth", 27: "twenty-seventh",
#         28: "twenty-eighth", 29: "twenty-ninth", 30: "thirtieth", 31: "thirty-first"
#     }
#
#     # Define mappings for converting month numbers to words
#     month_mapping = {
#         1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
#         7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"
#     }
#
#     # Extract the day, month, and year components from the date
#     day = numbers_mapping[date.day]
#     month = month_mapping[date.month]
#     year = numbers_mapping[date.year // 1000] + numbers_mapping[(date.year % 1000) // 100] + \
#            numbers_mapping[(date.year % 100) // 10] + numbers_mapping[date.year % 10]
#
#     # Construct the string in the desired format
#     result = day + " " + month + " " + year
#
#     return result
#
# # Get the current date
# current_date = datetime.today().date()
# print("current_date:",current_date)
#
# # Convert the current date to the desired string format
# date_string = convert_date_to_string(current_date)

# Print the date string
# print(date_string)
# from datetime import datetime
#
# def convert_date_to_string(date):
#     # Define mappings for converting numbers to words
#     numbers_mapping = {0:'zero',
#         1: "first", 2: "second", 3: "third", 4: "fourth", 5: "fifth", 6: "sixth",
#         7: "seventh", 8: "eighth", 9: "ninth", 10: "tenth", 11: "eleventh", 12: "twelfth",
#         13: "thirteenth", 14: "fourteenth", 15: "fifteenth", 16: "sixteenth", 17: "seventeenth",
#         18: "eighteenth", 19: "nineteenth", 20: "twentieth", 21: "twentyfirst", 22: "twentysecond",
#         23: "twenty-third", 24: "twentyfourth", 25: "twentyfifth", 26: "twentysixth", 27: "twentyseventh",
#         28: "twentyeighth", 29: "twentyninth", 30: "thirtieth", 31: "thirtyfirst",
#         20: "twenty", 21: "twentyfirst", 22: "twentysecond", 23: "twentythird", 24: "twentyfourth",
#         25: "twentyfifth", 26: "twentysixth", 27: "twentyseventh", 28: "twentyeighth",
#         29: "twentyninth", 30: "thirtieth", 31: "thirtyfirst"
#     }
#
#     # Define mappings for converting month numbers to words
#     month_mapping = {
#         1: "january", 2: "february", 3: "march", 4: "april", 5: "may", 6: "june",
#         7: "july", 8: "august", 9: "september", 10: "october", 11: "november", 12: "december"
#     }
#     day = numbers_mapping[date.day]
#     month = month_mapping[date.month]
#     result = day+month
#     return result
#
# # Get the current date
# current_date=datetime.today().date()
# # Convert the current date to the desired string format
# date_string = convert_date_to_string(current_date)
#
# # Print the date string
# print(date_string)
# def convert_year_to_string(year):
#     # Define mappings for converting numbers to words
#     digit_mapping = {
#         '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
#     }
#
#     # Convert each digit of the year to its corresponding word
#     digit_words = [digit_mapping[digit] for digit in str(year)]
#
#     # Join the digit words and return the result
#     result = ''.join(digit_words)
#
#     return result
#
# # Example usage
# year = 1999
# year_string = convert_year_to_string(year)
# print("yearof string:",year_string)


# def convert_year_to_string(year):
#     # Define mappings for converting numbers to words
#     digit_mapping = {
#         '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
#         '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'
#     }
#
#     tens_mapping = {
#         '0': '', '1': 'ten', '2': 'twenty', '3': 'thirty', '4': 'forty',
#         '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'
#     }
#
#     special_mapping = {
#         '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
#         '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'
#     }
#
#     # Convert each digit of the year to its corresponding word
#     digit_words = []
#
#     if year >= 1000:
#         digit_words.append(digit_mapping[str(year // 1000)])
#         digit_words.append("thousand")
#
#     if year >= 100:
#         digit_words.append(digit_mapping[str((year // 100) % 10)])
#         digit_words.append("hundred")
#
#     if year % 100 >= 20:
#         digit_words.append(tens_mapping[str((year // 10) % 10)])
#         digit_words.append(digit_mapping[str(year % 10)])
#     elif year % 100 >= 10:
#         digit_words.append(special_mapping[str(year % 100)])
#     else:
#         digit_words.append(digit_mapping[str(year % 10)])
#
#     # Join the digit words and return the result
#     result = ''.join(digit_words)
#
#     return result
#
#
# # Example usage
# year = 1999
# year_string = convert_year_to_string(year)
# print("string year:",year_string)


# self.log.info("***** Medicare Advantage plan is selected*****")
# action_utils.wait_for_element((Keen_Quote_Generation.medicare_label))
# medicare_label = keen_GQ.verify_medicare_label()
# assert medicare_label.is_displayed(), "Medicare Options are displayed"
# action_utils.wait_for_element((Keen_Quote_Generation.doctors_vist_yes))
# keen_GQ.click_doctor_yes()
# keen_GQ.select_Doctors_Generate()
# keen_testcreate.test_physicians(row_number_physicians)
# action_utils.wait_for_elements((Keen_Quote_Generation.doctor_visit_or_receive_medicalcare))
# doctor_visit = keen_GQ.member_doctor_vist()
# for doctor_visit_receive in doctor_visit:
#     if doctor_visit_receive.text == doctor_visit_medicalcare:
#         action.move_to_element(doctor_visit_receive).click().perform()
#         break


# def test_aws(sample_body):
#     import requests
#     ##sample_body = {{"from_email": "engineering@choosekeen.com","to_email": ["engineering@choosekeen.com","anil.maddula@choosekeen.com"],"subject":"GenerateQuote Automation status is pass","body":"Automation Execusion results"}}
#     method = "POST"
#     api_url = "https://service.choosekeentech.com"
#     auth_user = "keen_libs"
#     auth_password = "CJ63GZcbIp4EIkm"
#     path = "/aws/send_email"
#     url = api_url + path
#     response = requests.request(
#         method,
#         url,
#         auth=(auth_user, auth_password),
#         json=sample_body,
#     )
#     if response.status_code == 200:
#         data = response.json()
#         print("Response data:", data)
#     else:
#         print("API request failed with status code:", response.status_code)
#         print("Response content:", response.text)
# t





#
# import json
# import requests
# import pandas as pd
# class sensible_apis:
#     def __init__(self, endpointurl= 'https://api.sensible.so/v0/extract/enrollment?environment=production', token= '41526e211c78212dc2df040bacdab2d6ca33851222fdeb282a44a777860af96d7ea1eb6295311148b1552c85ea432882122551c64ed9298da145e823a4438aef'):
#         self.endpoint = endpointurl
#         self.headers = {'Content-Type': 'application/pdf',
#                    'Authorization': 'Bearer {}'.format(token)}
#     def extract_pdf(self, local_file_name):
#         res = requests.post(self.endpoint, headers=self.headers, files={'file': open(local_file_name, 'rb')})
#         return res
# if __name__ == '__main__':
#     sensible_client = sensible_apis()
#     #  local file name of the PDF
#     pdf_file_name = 'C:\\Users\\amaddula\\Downloads\\Enrolment.pdf'
#     # Call the extract_pdf method and print the response
#     response = sensible_client.extract_pdf(pdf_file_name)
#     print("Response:")
#     print(response.text)
#     # response_text = response.content.decode('utf-8')
#
#     response_json = sensible_client.extract_pdf(pdf_file_name)
#     # Flatten the JSON response using pandas DataFrame
    # df=pd.DataFrame.from_dict(response_text)
    # response_dict = json.loads(response_text)
    # # Flatten the JSON response using json_normalize
    # df = pd.json_normalize(response_dict)
    # df.to_csv('output.csv', index=False)
    # response_dict = json.loads(response_text)  # Parse JSON string into dictionary
    # df = pd.DataFrame.from_dict(response_dict)  # Create DataFrame from dictionary
    # print(data)
from selenium import webdriver
from tests.test_ALogin import Test_login
from Pages.Keen_SOA import Create_SOA_Form
from utilities.Webdriver import WebDriverFactory
# from tests import conftest
# browser=conftest()
class Test_Email(Test_login):
    def test_email_login(self):
        keen_soa=Create_SOA_Form(self.driver)
        self.driver.get("https://gmail.com")
                # self.log.info("***** Login in to Gmail to verify docusign *****")
        keen_soa.enter_mail_user_name("testkeenmember@gmail.com")
        print("email entered")
        keen_soa.click_next_button()
        self.driver.refresh()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)
        self.driver.refresh()
        keen_soa.enter_mail_password("InnoKeen@123")
        print("gmail is logged")
    def calulation(a):
       b=6
       c=a+b
       print(c)
t=Test_Email()
t.calilation(3)
##############################
# pages ki class
#     kavalsina (Xpaths, click , enter)
#     tests module
#     test_scrit
#     login
#     functionality(import pages)
