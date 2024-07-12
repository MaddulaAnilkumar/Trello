# import allure
# import pytest
# from tests.test_ALogin import Test_login
# from selenium.common import TimeoutException
# from Pages.Keen_Login import Keen_login
# from Pages.aws import keen_aws_session
# from selenium.webdriver import ActionChains
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from Pages.Keen_account_creation import Keen_Account_creation
# from Pages.Keen_create_Capture_full_Member_details import Create_capture_member_details
# from utilities.XLUtilities import Excel_data
# from Pages.Keen_GenerateQuote import Keen_Quote_Generation
# from utilities import logger_utils
# from utilities.action_utils import ActionUtils
# from tests.test_create_Capture_full_Member_details import Test_create_capture_full_member_details
# from utilities.base_test import BaseTest
# from datetime import datetime
# class Test_test_GenerateQuote():
#     log = logger_utils.get_logger()
#     path = "../test_data/Keen_Testdata.xlsx"
#     readdata_account = Excel_data(path, "Account_Creation")
#     readdata_medications = Excel_data(path, "Medication")
#     readdata_physicians = Excel_data(path, "Physicians")
#     readdata_pharmacies = Excel_data(path, "Pharmacies")
#     sheet=BaseTest()
#     def __init__(self,driver):
#         self.driver=driver
#     def test_examplegeneratequote_newaccount(self, row_number_account):
#         doctor_visit_medicalcare = self.readdata_account.readdata(row_number_account, 33)
#         physician = self.readdata_account.readdata(row_number_account, 31)
#         medication = self.readdata_account.readdata(row_number_account, 32)
#         pharmacy = self.readdata_account.readdata(row_number_account, 35)
#         Extra_help = self.readdata_account.readdata(row_number_account, 42)
#         drug_pay = self.readdata_account.readdata(row_number_account, 43)
#         Medicare_supplimetary = self.readdata_account.readdata(row_number_account, 39)
#         tobacco_use = self.readdata_account.readdata(row_number_account, 40)
#         household_discount = self.readdata_account.readdata(row_number_account, 41)
#         keen = Keen_Account_creation(self.driver)
#         keen_create = Create_capture_member_details(self.driver)
#         keen_testcreate = Test_create_capture_full_member_details(self.driver)
#         keen_GQ = Keen_Quote_Generation(self.driver)
#         action = ActionChains(self.driver)
#         action_utils = ActionUtils(self.driver)
#         self.log.info("***** Validating the leads data to generate quote data *****")
#         action_utils.wait_for_element((Keen_Account_creation.verify_field_01))
#         lead_dob = keen.validation_of_DoB()
#         email_lead = keen.validation_of_email()
#         phone_lead = keen.validation_of_Phone()
#         lead_phone = action_utils.convert_string(phone_lead)
#         action_utils.wait_for_element((Keen_Account_creation.address_details))
#         keen.click_address_Details()
#         action_utils.wait_for_element((Keen_Account_creation.verify_streetaddress))
#         time.sleep(5)
#         member_street_address=keen.validation_of_street().get_attribute('value')
#         self.log.info("***** Retrieve 'Street' value in Keen Member *****")
#         time.sleep(5)
#         member_city=keen.validation_of_city().get_attribute('value')
#         self.log.info("***** Retrieve 'City' value in Keen Member *****")
#         time.sleep(5)
#         member_addressline_two=keen.validation_of_addressline_2().get_attribute('value')
#         self.log.info("***** Retrieve 'addressline_2' value in Keen Member *****")
#         time.sleep(5)
#         member_state=keen.validation_of_state().get_attribute('data-value')
#         self.log.info("*****Retrieve 'State' value in Keen Member *****")
#         time.sleep(5)
#         member_county=keen.validation_of_county().get_attribute('value')
#         self.log.info("*****Retrieve 'County' value in Keen Member *****")
#         time.sleep(5)
#         member_zipcode=keen.validation_of_zipcode().get_attribute('value')
#         self.log.info("*****Retrieve 'Zipcode' value in Keen Member *****")
#         print("member zipcode:",member_zipcode)
#         keen.Click_close_popup()
#         # action_utils.wait_for_element((Keen_Account_creation.medication_details_popup))
#         # keen.select_medication_details()
# #         # self.log.info("***** Medicare popup is selected *****")
# #         # action_utils.wait_for_element((Keen_Account_creation.part_A))
# #         # self.log.info("***** Part A date is displayed *****")
# #         # part_A_date=keen.enter_Part_A_enrollment_date().get_attribute('value')
# #         # self.log.info("***** Part_A_enrollment_date is taken *****")
# #         # action_utils.wait_for_element((Keen_Account_creation.part_B))
# #         # part_B_date=keen.enter_Part_B_enrollment_date().get_attribute('value')
# #         # self.log.info("***** Part_B_enrollment_date is taken *****")
# #         # keen.Click_close_popup()
# #         self.log.info("***** popup is closed *****")
# #         action_utils.wait_for_element((Keen_Account_creation.edit_record))
# #         keen.click_on_edit()
# #         action_utils.wait_for_element((Keen_Account_creation.verify_firstName))
# #         lead_first_name=keen.verify_first_name().get_attribute("value")
# #         print("lead_firstname:",lead_first_name)
# #         action_utils.wait_for_element((Keen_Account_creation.verify_LastName))
# #         lead_last_name=keen.verify_last_name().get_attribute("value")
# #         print("Generate:", lead_last_name)
# #         action_utils.wait_for_element((Keen_Account_creation.cancel_in_member_page))
# #         keen.click_cancel_keen_page()
# #         time.sleep(5)
# #         action_utils.wait_for_element((Keen_Quote_Generation.generate_quote))
# #         keen_GQ.click_GenerateQuote()
# #         self.log.info("***** Compare the data in memebers record is reflected to 'Generate Quote' *****")
# #         time.sleep(16)
# #         try:
# #             action_utils.wait_for_element((Keen_Quote_Generation.first_name))
# #             first_name = keen_GQ.firstName_Generate_Quote().get_attribute('value')
# #             print("Generate first name:",first_name)
# #             assert first_name == lead_first_name,"First name is not matched"
# #         except Exception as ex:
# #             print(ex)
# #         try:
# #             last_name_generate = keen_GQ.enter_lastname_GenerateQuote().get_attribute('value')
# #             print("Generate last name:", last_name_generate)
# #             # entered_value = self.driver.execute_script("return arguments[0].value;", last_name_generate)
# #             assert lead_last_name == last_name_generate,"Last name is not matched"
# #         except Exception as ex:
# #             print(ex)
# #         dob = keen_GQ.DoB_GenerateQuote()
# #         generate_dob = dob.get_attribute("value")
# #         print("Generate:", generate_dob)
# #         assert lead_dob == generate_dob,"DOB is not matched"
# #         email_generate=keen_GQ.Email_GenerateQuote().get_attribute("value")
# #         print("Generate:", email_generate)
# #         assert email_lead == email_generate,"Email is not matched"
# #         keen_GQ.Phone_GenerateQuote()
# #         phone_generate=keen_GQ.Phone_GenerateQuote().get_attribute("value")
# #         generate_phone=action_utils.convert_string(phone_generate)
# #         assert generate_phone == lead_phone,"Phone number is not matched"
# #         generate_zipcode=keen_GQ.zipcode_GenerateQuote().get_attribute("value")
# #         print("generate zipcode:",generate_zipcode)
# #         assert generate_zipcode == member_zipcode,"Zipcode is not matched"
# #         street_address=keen_GQ.street_address().get_attribute("value")
# #         assert street_address == member_street_address,"Street address is not matched"
# #         generate_address_line2=keen_GQ.enter_addressline2().get_attribute("value")
# #         assert member_addressline_two == generate_address_line2,"Address line is not matched"
# #         generate_city=keen_GQ.enter_city().get_attribute("value")
# #         assert member_city == generate_city,"City is not matched"
# #         generate_county=keen_GQ.Member_county().get_attribute("value")
# #         assert member_county == generate_county,"county is not matched"
# #         generate_state=keen_GQ.select_generate_state().get_attribute("data-value")
# #         assert member_state == generate_state,"State is not matched"
# #         time.sleep(5)
# #         self.log.info("***** Click on sunfire button *****")
# #         keen_GQ.click_TransferToSunfire()
# #         action_utils.wait_for_element((Keen_Quote_Generation.data_failure_message))
# #         toast_message = keen_GQ.verify_toast_message()
# #         print("Toast message:", toast_message.text)
# #         self.log.info("***** Verifing the quote is already generated *****")
# #         if "Error!" in toast_message.text:
# #             self.log.info("***** Quote is not generated *****")
# #             self.log.info("***** Filling the inputdata *****")
# #             action_utils.wait_for_elements((Keen_Quote_Generation.plans_types_name))
# #             plans_to_discuss = keen_GQ.click_plan_types()
# #             for plans in plans_to_discuss:
# #                 time.sleep(2)
# #                 plans.click()
# #             self.log.info("***** Medicare Advantage/Part D or Special Needs plan is selected*****")
# #             action_utils.wait_for_element((Keen_Quote_Generation.medicare_label))
# #             medicare_label = keen_GQ.verify_medicare_label()
# #             assert medicare_label.is_displayed(), "Medicare Options are displayed"
# #             action_utils.wait_for_element((Keen_Quote_Generation.doctors_vist_yes))
# #             keen_GQ.click_doctor_yes()
# #             keen_GQ.select_Doctors_Generate()
# #             action_utils.wait_for_element((Create_capture_member_details.pop_up_new_members))
# #             pop_up_of_New_Members_physicians = keen_create.pop_up_of_New_Members()
# #             assert pop_up_of_New_Members_physicians.text == "New Member's physician", "New Member's physician popup is not matched"
# #             keen_create.click_physician_directory().send_keys("NATASA")
# #             self.log.info("***** Associating existing 'physician' record to member  *****")
# #             action_utils.wait_for_elements((Create_capture_member_details.physicians_records))
# #             self.log.info("***** Options are displayed *****")
# #             list_of_physicians = keen_create.select_physicians_records()
# #             time.sleep(6)
# #             print("physicians:", len(list_of_physicians))
# #             keen_create.click_physician_record()
# #             # self.log.info("***** Physician record are present in SF *****")
# #             # for physicians in list_of_physicians:
# #             #     self.log.info("***** Physicians records are available *****")
# #             #     print("physician_value:",physician)
# #             #     print("physicians_records:",physicians.get_attribute('title'))
# #             #     if physicians.get_attribute('title').strip() == physician.strip():
# #             #         print("physician is matched")
# #             #         self.driver.execute_script("arguments[0].click();", physicians)
# #             #         self.log.info("***** Existing record is selected *****")
# #             #         break
# #             keen_create.click_Is_Primary_Care_Physician()
# #             keen_create.save_button_Add()
# #             action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
# #             success_message_of_records = keen_create.success_message()
# #             assert success_message_of_records.is_displayed(), "Record is saved"
# #             action_utils.wait_for_elements((Keen_Quote_Generation.doctor_visit_or_receive_medicalcare))
# #             doctor_visit = keen_GQ.member_doctor_vist()
# #             self.log.info("***** doctor visit option should be selected*****")
# #             for doctor_visit_receive in doctor_visit:
# #                 if doctor_visit_receive.text == doctor_visit_medicalcare:
# #                     self.driver.execute_script("arguments[0].click();", doctor_visit_receive)
# #                     self.log.info("***** doctor visit option is selected*****")
# #                     break
# #             action_utils.wait_for_element((Keen_Quote_Generation.search_mediaction_field))
# #             scroll_to_medication = keen_GQ.move_to_medication()
# #             self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_medication)
# #             self.log.info("***** Medications option *****")
# #             time.sleep(3)
# #             action_utils.wait_for_element((Keen_Quote_Generation.medication_add))
# #             keen_GQ.select_medication_GenerateQuote()
# #             pop_up_of_New_Members_medication = keen_create.pop_up_of_New_Members()
# #             assert pop_up_of_New_Members_medication.text == "New Member Medication", "New Member Medication is not matched"
# #             keen_create.medication_search().send_keys(medication)
# #             self.log.info("***** Associate existing medication record to member  *****")
# #             action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
# #             list_of_medication = keen_create.select_existing_records()
# #             for medications in list_of_medication:
# #                 if medications.text == medication:
# #                     self.driver.execute_script("arguments[0].click();", medications)
# #                     self.log.info("***** Existing record is selected *****")
# #                     break
# #             keen_create.save_button_Add()
# #             self.log.info("***** Medication record is existing in SalesForce *****")
# #             action_utils.wait_for_element((Create_capture_member_details.Success_message_Added))
# #             success_message_of_records = keen_create.success_message()
# #             assert success_message_of_records.is_displayed(), "Record is not saved"
# #             time.sleep(3)
# #             # action_utils.wait_for_element((Keen_Quote_Generation.pharmacy_add))
# #             scroll_to_pharmacy = keen_GQ.move_to_pharmacy()
# #             self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_pharmacy)
# #             action_utils.wait_for_element((Keen_Quote_Generation.pharmacy_add))
# #             keen_GQ.click_pharamcy()
# #             action_utils.wait_for_element((Create_capture_member_details.search_pharmacy))
# #             keen_create.pharmacy_directory().send_keys(pharmacy)
# #             self.log.info("***** Associating existing 'Pharmacies' record to member  *****")
# #             action_utils.wait_for_elements((Create_capture_member_details.available_list_options))
# #             list_of_pharmacies = keen_create.select_existing_records()
# #             print("len of pharmacies:", len(list_of_pharmacies))
# #             time.sleep(5)
# #             for pharmacies in list_of_pharmacies:
# #                 if pharmacies.text == pharmacy:
# #                     self.driver.execute_script("arguments[0].click();", pharmacies)
# #                     self.log.info("***** Existing record is selected *****")
# #                     break
# #             keen_create.save_button_Add()
# #             self.log.info("***** Associated existing 'Pharmacies' record to member *****")
# #             element = WebDriverWait(self.driver, 200).until(
# #                 EC.presence_of_element_located((By.XPATH, "//div[contains(@id,'toastDescription')]//span")) or
# #                 EC.presence_of_element_located((By.XPATH, "//div[text()='Complete this field.']")))
# #             if element.tag_name == "span":
# #                 success_message_of_records = keen_create.success_message()
# #                 assert success_message_of_records.is_displayed(), "Record is not saved"
# #             else:
# #                 keen_create.click_cancel_pharcmacy()
# #             scroll_to_subsidy = keen_GQ.move_to_extra_help_subsidy()
# #             self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_subsidy)
# #             options_help = keen_GQ.click_extra_help_or_subsidy()
# #             for subsidy in options_help:
# #                 if subsidy.text == Extra_help:
# #                     self.log.info("***** Extra help option is selcted *****")
# #                     self.driver.execute_script("arguments[0].click();", subsidy)
# #                     break
# #             if Extra_help == "Yes":
# #                 self.log.info("***** Extra help option is 'Yes' *****")
# #                 drug_cost = keen_GQ.verify_drug_pay()
# #                 assert drug_cost.is_displayed(), "Drug_pay filed is not displayed"
# #                 self.log.info("***** Drug pay option is to be selected *****")
# #                 options_pay = keen_GQ.select_drug_pay()
# #                 for drug_cost in options_pay:
# #                     if drug_cost.text == drug_pay:
# #                         self.driver.execute_script("arguments[0].click();", drug_cost)
# #                         self.log.info("***** Drug pay option is selected *****")
# #                         break
# #             pick_options_member = keen_GQ.select_important_to_patient()
# #             self.log.info("***** Patients needs should be selected *****")
# #             for choose_options in pick_options_member:
# #                 action.move_to_element(choose_options).click().perform()
# #                 self.log.info("***** Patient needs are selected *****")
# #             assert keen_GQ.verify_medicare_supplimentary().is_displayed(), "Medicare supplimetary is not selected"
# #             if Medicare_supplimetary == "Yes":
# #                 self.log.info("***** Medicare supplimetary should be selecet as yes *****")
# #                 medicare_options = keen_GQ.click_supplement()
# #                 for medicare in medicare_options:
# #                     time.sleep(6)
# #                     if medicare.text == Medicare_supplimetary:
# #                         print(print("input option:", ), Medicare_supplimetary)
# #                         print("medicare options yes text:", medicare.text)
# #                         time.sleep(6)
# #                         self.driver.execute_script("arguments[0].click();", medicare)
# #                         self.log.info("***** Medicare supplimetary is selected as Yes ******")
# #                         break
# #                 self.log.info("***** Medicare supplimetary is selected as Yes ******")
# #                 assert keen_GQ.verify_medicare_yes().is_displayed(), "Medicare supplimentary option is not selected"
# #                 action_utils.wait_for_element((Keen_Quote_Generation.effective_date))
# #                 keen_GQ.click_Effective_Date()
# #                 action_utils.wait_for_element((Keen_Quote_Generation.pick_effectivedate))
# #                 keen_GQ.select_effective_date()
# #                 # month, year = self.sheet.extract_month_and_year(part_A_date)
# #                 # print("Month:",month)
# #                 # print("year:",year)
# #                 # generate_medicare_date = keen_GQ.select_PratA_enrollment_date()
# #                 # assert generate_medicare_date.text == month, "PartA Month is not matched"
# #                 # action_utils.wait_for_element((Keen_Quote_Generation.PartA_year))
# #                 # generate_medicare_year = keen_GQ.select_PartA_enrollment_year()
# #                 # print(generate_medicare_year.text)
# #                 # assert generate_medicare_year.text == year, "PartA Year is matched"
# #                 # month_patrB, year_partB = self.sheet.extract_month_and_year(part_B_date)
# #                 # action_utils.wait_for_element((Keen_Quote_Generation.PartB_year))
# #                 # generate_partB_date = keen_GQ.select_PartB_enrollment_month()
# #                 # assert generate_partB_date.text == month_patrB, "PartB month is not matched"
# #                 # generate_partB_year = keen_GQ.select_PartB_enrollment_year()
# #                 # assert generate_partB_year.text == year_partB, "PartB month is not matched"
# #                 action_utils.wait_for_elements((Keen_Quote_Generation.tobacco_use))
# #                 tobacco_options = keen_GQ.select_medicare_Tobacco_use()
# #                 for tobaccco in tobacco_options:
# #                     if tobaccco.text == tobacco_use.strip():
# #                         action.move_to_element(tobaccco).click().perform()
# #                         self.log.info("***** tobacoo use option is selected *****")
# #                         break
# #                 action_utils.wait_for_elements((Keen_Quote_Generation.household_discount))
# #                 discount_options = keen_GQ.select_Household_Discount()
# #                 for discount in discount_options:
# #                     if discount.text == household_discount:
# #                         print("household value:", household_discount)
# #                         action.move_to_element(discount).click().perform()
# #                         self.log.info("***** House hold option is selected *****")
# #                         break
# #                 keen_GQ.click_TransferToSunfire()
# #                 self.log.info("***** Quote is initiated *****")
# #                 try:
# #                     self.log.info("***** Waiting for the Quote response *****")
# #                     elements = WebDriverWait(self.driver, 180).until(
# #                         EC.presence_of_element_located((By.XPATH, "//div[text()='Error!']")) or
# #                         EC.presence_of_element_located((By.XPATH,"//h2[text()='Quote transfered to sunfire']"))
# #                     )
# #                     error=None
# #                     for element in elements:
# #                         if element.tag_name == "div":
# #                             errors = keen_GQ.verify_error_toast_message()
# #                             for error_toast in errors:
# #                                 if error_toast.text == "Please enter a valid phone number (xxx-xxx-xxxx)":
# #                                     error = error_toast.text
# #                                     if error_toast is not None:
# #                                         if error:
# #                                            self.log.info("Phone neumber format is not matched")
# #                                 elif error_toast.text == "You must select at least one choice from this set.":
# #                                     error = error_toast.text
# #                                     if error is not None:
# #                                         if error:
# #                                             self.log.info("***** Plans are not selected *****")
# #                                 elif error_toast.text == "Please enter a valid phone number (xxx-xxx-xxxx)" and "Error!":
# #                                     error = error_toast.text
# #                                     if error is not None:
# #                                         if error:
# #                                             self.log.info("Quote generation is failed")
# #                 except Exception as ex:
# #                     print(ex)
# #             else:
# #                 self.log.info("***** Medicare supplimentary is should be select as 'NO' *****")
# #                 medicare_options = keen_GQ.click_supplement()
# #                 time.sleep(6)
# #                 for medicare_no in medicare_options:
# #                     if medicare_no.text == "No":
# #                         print("medicare options no text:", medicare_no.text)
# #                         print("input option:", "No")
# #                         time.sleep(6)
# #                         self.driver.execute_script("arguments[0].click();", medicare_no)
# #                         self.log.info("***** Medicare supplimentary is  selected as 'NO' *****")
# #                         break
# #                 keen_GQ.click_TransferToSunfire()
# #                 self.log.info("***** Quote is initiated *****")
# #                 try:
# #                     self.log.info("***** Waiting for the Quote response *****")
# #                     elements = WebDriverWait(self.driver, 180).until(
# #                         EC.presence_of_all_elements_located((By.XPATH, "//div[text()]"))
# #                     )
# #                     error = None
# #                     for element in elements:
# #                         if element.tag_name == "div":
# #                             errors = keen_GQ.verify_error_toast_message()
# #                             for error_toast in errors:
# #                                 if error_toast.text == "Please enter a valid phone number (xxx-xxx-xxxx)":
# #                                     error = error_toast.text
# #                                     if error_toast is not None:
# #                                         if error:
# #                                             self.log.info("Phone neumber format is not matched")
# #                                 elif error_toast.text == "You must select at least one choice from this set.":
# #                                     error = error_toast.text
# #                                     if error is not None:
# #                                         if error:
# #                                             self.log.info("***** Plans are not selected *****")
# #                                 elif error_toast.text == "Please enter a valid phone number (xxx-xxx-xxxx)" and "Error!":
# #                                     error = error_toast.text
# #                                     if error is not None:
# #                                         if error:
# #                                             self.log.info("Quote generation is failed")
# #                         else:
# #                             self.log.info("***** Quote is generated*****")
# #                             if keen_GQ.verify_success_quote().is_displayed():
# #                                 self.log.info("***** Quote generation popup is displayed *****")
# #                                 keen_GQ.Quote_close()
# #                                 self.log.info("***** Quote generation popup is closed *****")
# #                                 # email_sent = keen_aws_session()
# #                                 # email_sent.send_email("anil.maddula@choosekeen.com", ["anil.maddula@choosekeen.com"],
# #                                 #                       "GenerateQuote Automation testing status is passed")
# #
# #                         # email_sent = keen_aws_session()
# #                         # email_sent.send_email("anil.maddula@choosekeen.com", ["anil.maddula@choosekeen.com"],"GenerateQuote Automation testing status is passed")
# #                 except TimeoutException:
# #                     self.log.info("***** Quote generation is failed *****")
# #         else:
# #             try:
# #                 self.log.info("***** Waiting for the Quote response *****")
# #                 elements = WebDriverWait(self.driver, 180).until(
# #                     EC.presence_of_element_located((By.XPATH, "//div[text()='Error!']"))
# # #                     or EC.presence_of_element_located((By.XPATH,"//h2[text()]='Quote is generated in sunfire']"))
# # #                 )
# # #                 error = None
# # #                 for element in elements:
# # #                     if element.tag_name == "div":
# # #                         errors = keen_GQ.verify_error_toast_message()
# # #                         for error_toast in errors:
# # #                             if error_toast.text == "Please enter a valid phone number (xxx-xxx-xxxx)":
# # #                                 error = error_toast.text
# # #                                 if error_toast is not None:
# # #                                     if error:
# # #                                         self.log.info("Phone neumber format is not matched")
# # #                             elif error_toast.text == "You must select at least one choice from this set.":
# # #                                 error = error_toast.text
# # #                                 if error is not None:
# # #                                     if error:
# # #                                         self.log.info("***** Plans are not selected *****")
# # #                             elif error_toast.text == "Please enter a valid phone number (xxx-xxx-xxxx)" and "Error!":
# # #                                 error = error_toast.text
# # #                                 if error is not None:
# # #                                     if error:
# # #                                         self.log.info("Quote generation is failed")
# # #                     else:
# # #                         self.log.info("***** Quote is generated*****")
# # #                         if keen_GQ.verify_success_quote().is_displayed():
# # #                             self.log.info("***** Quote generation popup is displayed *****")
# # #                             keen_GQ.Quote_close()
# # #                             self.log.info("***** Quote generation popup is closed *****")
# # #                             # email_sent = keen_aws_session()
# # #                             # email_sent.send_email("anil.maddula@choosekeen.com", ["anil.maddula@choosekeen.com"],
# # #                             #                       "GenerateQuote Automation testing status is passed")
# # #
# # #                     # email_sent = keen_aws_session()
# # #                     # email_sent.send_email("anil.maddula@choosekeen.com", ["anil.maddula@choosekeen.com"],"GenerateQuote Automation testing status is passed")
# # #             except TimeoutException:
# # #                 self.log.info("***** Quote generation is failed *****")
# # import time
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # driver = webdriver.Chrome("C:\\Users\\amaddula\\PycharmProjects\\Salesforce_Keen\\chromedriver_win32 (7)\\chromedriver.exe")
# # driver.maximize_window()
# # driver.implicitly_wait(10)
# # driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+\
# #     'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
# #     '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
# # driver.find_element(By.XPATH,"//input[@name='identifier']").send_keys("anilkumarmaddula05@gmail.com")
# # time.sleep(3)
# # next_button=driver.find_element(By.XPATH,"//div[@id='identifierNext']//button")
# # next_button.click()
# # # print("hi")
# # import time
# #
# # # def test_ex():
# # #     import datetime
# # #     now = datetime.datetime.now()
# # #     timestamp = (now - datetime.timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%SZ")
# # #     print(timestamp)
# #     # doctor_visit_medicalcare = self.readdata_account.readdata(row_number_account, 33)
# #     # physician = self.readdata_account.readdata(row_number_account, 31)
# #     # medication = self.readdata_account.readdata(row_number_account, 32)
# #     # pharmacy = self.readdata_account.readdata(row_number_account, 35)
# #     # drug_pay = self.readdata_account.readdata(row_number_account, 43)
# #     # Medicare_supplimetary = self.readdata_account.readdata(row_number_account, 39)
# #     # tobacco_use = self.readdata_account.readdata(row_number_account, 40)
# #     # household_discount = self.readdata_account.readdata(row_number_account, 41)
# #     # print("physicians:", len(list_of_physicians))
# #     # keen_create.click_physician_record()
# #     # for physicians in list_of_physicians:
# #     #     print("physicians:",physicians.get_attribute('title'))
# #     #     print("physician_value:",physician)
# #     #     if physicians.get_attribute('title').strip() == physician.strip():
# #     #         print("physician matched")
# #     #         self.driver.execute_script("arguments[0].click();", list_of_physicians[1])
# #     #         self.log.info("***** Existing record is selected *****")
# #     #         break
# # ########################################## GenerateQuote #####################################
# #     # pick_options_member = keen_GQ.select_important_to_patient()
# #     # self.log.info("***** Patients needs should be selected *****")
# #     # for choose_options in pick_options_member:
# #     #     action.move_to_element(choose_options).click().perform()
# #     #     self.log.info("***** Patient needs are selected *****")
# #     # assert keen_GQ.verify_medicare_supplimentary().is_displayed(), "Medicare supplimetary is not selected"
# #     # if Medicare_supplimetary == "Yes":
# #     #     self.log.info("***** Medicare supplimetary should be selecet as yes *****")
# #     #     medicare_options = keen_GQ.click_supplement()
# #     #     for medicare in medicare_options:
# #     #         WebDriverWait(self.driver, 5)
# #     #         if medicare.text == Medicare_supplimetary:
# #     #             print(print("input option:", ), Medicare_supplimetary)
# #     #             print("medicare options yes text:", medicare.text)
# #     #             WebDriverWait(self.driver, 5)
# #     #             self.driver.execute_script("arguments[0].click();", medicare)
# #     #             self.log.info("***** Medicare supplimetary is selected as Yes ******")
# #     #             break
# #     #     self.log.info("***** Medicare supplimetary is selected as Yes ******")
# #     #     assert keen_GQ.verify_medicare_yes().is_displayed(), "Medicare supplimentary option is not selected"
# #     #     action_utils.wait_for_element((Keen_Quote_Generation.effective_date))
# #     #     keen_GQ.click_Effective_Date()
# #     #     action_utils.wait_for_element((Keen_Quote_Generation.pick_effectivedate))
# #     #     keen_GQ.select_effective_date()
# #     #     month, year = self.sheet.extract_month_and_year(part_A_date)
# #     #     print("Month:", month)
# #     #     print("year:", year)
# #     #     generate_medicare_date = keen_GQ.select_PratA_enrollment_date()
# #     #     assert generate_medicare_date.text == month, "PartA Month is not matched"
# #     #     action_utils.wait_for_element((Keen_Quote_Generation.PartA_year))
# #     #     generate_medicare_year = keen_GQ.select_PartA_enrollment_year()
# #     #     print(generate_medicare_year.text)
# #     #     assert generate_medicare_year.text == year, "PartA Year is matched"
# #     #     month_patrB, year_partB = self.sheet.extract_month_and_year(part_B_date)
# #     #     action_utils.wait_for_element((Keen_Quote_Generation.PartB_year))
# #     #     generate_partB_date = keen_GQ.select_PartB_enrollment_month()
# #     #     assert generate_partB_date.text == month_patrB, "PartB month is not matched"
# #     #     generate_partB_year = keen_GQ.select_PartB_enrollment_year()
# #     #     assert generate_partB_year.text == year_partB, "PartB month is not matched"
# #     #     action_utils.wait_for_elements((Keen_Quote_Generation.tobacco_use))
# #     #     tobacco_options = keen_GQ.select_medicare_Tobacco_use()
# #     #     for tobaccco in tobacco_options:
# #     #         if tobaccco.text.strip() == tobacco_use.strip():
# #     #             action.move_to_element(tobaccco).click().perform()
# #     #             self.log.info("***** tobacoo use option is selected *****")
# #     #             break
# #     #     action_utils.wait_for_elements((Keen_Quote_Generation.household_discount))
# #     #     discount_options = keen_GQ.select_Household_Discount()
# #     #     for discount in discount_options:
# #     #         if discount.text.strip() == household_discount.strip():
# #     #             print("household value:", household_discount)
# #     #             action.move_to_element(discount).click().perform()
# #     #             self.log.info("***** House hold option is selected *****")
# #     #             break
# # ############### Part A/B details  ######################
# # # action_utils.wait_for_element((Keen_Account_creation.medication_details_popup))
# # # keen.select_medication_details()
# # # self.log.info("***** Medicare popup is selected *****")
# # # action_utils.wait_for_element((Keen_Account_creation.part_A))
# # # self.log.info("***** Part A date is displayed *****")
# # # part_A_date=keen.enter_Part_A_enrollment_date().get_attribute('value')
# # # self.log.info("***** Part_A_enrollment_date is taken *****")
# # # action_utils.wait_for_element((Keen_Account_creation.part_B))
# # # part_B_date=keen.enter_Part_B_enrollment_date().get_attribute('value')
# # # self.log.info("***** Part_B_enrollment_date is taken *****")
# # # keen.Click_close_popup()
# # ################ Medicare suplimentary ###########################
# #
# #   # self.log.info("***** Medicare supplimentary is should be select as 'NO' *****")
# #   #                   medicare_options = keen_GQ.click_supplement()
# #   #                   WebDriverWait(self.driver, 10)
# #   #                   for medicare_no in medicare_options:
# #   #                       if medicare_no.text == "No":
# #   #                           print("medicare options no text:", medicare_no.text)
# #   #                           print("input option:", "No")
# #   #                           time.sleep(6)
# #   #                           self.driver.execute_script("arguments[0].click();", medicare_no)
# #   #                           self.log.info("***** Medicare supplimentary is  selected as 'NO' *****")
# #   #                           break
# #
# #
# #   ########################## Generatequote ##########################
# # #
# # # action_utils.wait_for_element((Keen_Quote_Generation.current_plan_no))
# # # click_on_plan = keen_GQ.click_current_plan_no()
# # # action.move_to_element(click_on_plan).click().perform()
# #
# #
# # # self.log.info("***** Part D plan is selected")
# #     # scroll_to_medication = keen_GQ.move_to_medication()
# #     # self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_medication)
# #     # keen_GQ.select_medication_GenerateQuote()
# #     # keen_testcreate.test_create_Medications(row_medication)
# #     # keen_GQ.click_pharamcy()
# #     # keen_testcreate.test_create_pharmacies(row_pharmacy)
# #     # scroll_to_subsidy = keen_GQ.move_to_extra_help_subsidy()
# #     # self.driver.execute_script("arguments[0].scrollIntoView();", scroll_to_subsidy)
# #     # options_help = keen_GQ.click_extra_help_or_subsidy()
# #     # for subsidy in options_help:
# #     #     if subsidy.text == Extra_help:
# #     #         action.move_to_element(subsidy).click().perform()
# #     #         break
# #     # if Extra_help == "Yes":
# #     #     drug_cost = keen_GQ.verify_drug_pay()
# #     #     assert drug_cost.is_displayed(), "Drug_pay filed is not displayed"
# #     #     options_pay = keen_GQ.select_drug_pay()
# #     #     for drug_cost in options_pay:
# #     #         if drug_cost.text == drug_pay:
# #     #             action.move_to_element(drug_cost).click().perform()
# #     #             break
# #     # elif Extra_help == "No":
# #     #     options_pay = keen_GQ.select_drug_pay()
# #     #     for drug_cost in options_pay:
# #     #         if drug_cost.text == Extra_help:
# #     #             action.move_to_element(drug_cost).click().perform()
# #     #             break
# #     # elif Extra_help == "I don't know":
# #     #     options_pay = keen_GQ.select_drug_pay()
# #     #     for drug_cost in options_pay:
# #     #         if drug_cost.text == Extra_help:
# #     #             action.move_to_element(drug_cost).click().perform()
# #     #             break
# #     # else:
# #     #     if Extra_help == "I don't know":
# #     #         options_pay = keen_GQ.select_drug_pay()
# #     #         for drug_cost in options_pay:
# #     #             if drug_cost.text == Extra_help:
# #     #                 action.move_to_element(drug_cost).click().perform()
# #     #                 break
# #     # keen_GQ.click_TransferToSunfire()
# #     # self.log.info("***** Medicare Supplement plan is selected *****")
# #
# # ##### Nem Medication
# # # import boto3
# # # import json
# # # import sys
# # # class test_s3():
# # #     def transcribe_s3(s3_bucket):
# # #         s3 = boto3.resource('s3')
# # #         path = s3_bucket.split("/")
# # #         s3_bucket = path[0]
# # #         if len(path)>1:
# # #             folder1 = path[1]
# # #         else:
# # #             folder1 = "all"
# # #         bucket = s3.Bucket(s3_bucket)
# # #         for obj in bucket.objects.all():
# # #             key = obj.key
# # #     #        body = obj.get()['Body'].read()
# # #             if key[-5:] == ".json" and (key.split("/")[-2] == folder1 or folder1 == "all"):
# # #                 print(key)
# # #                 body = obj.get()['Body'].read()
# # #                 input_filename = key.split("/")[-1]
# # #                 s3_path = key.replace(input_filename,"")
# # #                 output_filename = "{}_formatted.txt".format(input_filename[:-5])
# # #                 conversation_log = test_s3().transcribe_local(json.loads(body))
# # #                 if len(conversation_log) > 1:
# # #                     print("Writing file ....{}".format(output_filename))
# # #                     log_file = open(output_filename, "w")
# # #                     log_file.write(conversation_log)
# # #                     log_file.close()
# # #                     boto3.session.Session().client(service_name='s3')\
# # #                                 .put_object(Body=open(output_filename, 'rb'), Bucket=s3_bucket, Key=s3_path+output_filename)
# # #
# # #
# # #     def transcribe_local(conversation_json):
# # #     #
# # #         try:
# # #             len_of_conv = len(conversation_json["results"]["items"])
# # #             prev_speaker = ""
# # #             conversation_log = ""
# # #         #
# # #             for i in range(0,len_of_conv):
# # #                 speaker = conversation_json["results"]["items"][i]["speaker_label"]
# # #                 conversation = conversation_json["results"]["items"][i]["alternatives"][0]["content"]
# # #                 if speaker == prev_speaker:
# # #                     conversation_log = "{} {}".format(conversation_log, conversation)
# # #                 else:
# # #                     conversation_log = "{}\n{}:\n\t{}".format(conversation_log, speaker, conversation)
# # #                 prev_speaker = speaker
# # #             return conversation_log
# # #         except Exception as e:
# # #             print(e)
# # #             print("Could not process. Proceeding for next")
# # #             return ""
# # # if __name__ == '__main__':
# # #
# # #     conversation_filename = sys.argv[1]
# # #     if conversation_filename=="s3":
# # #         s3_path = sys.argv[2]
# # #         test_s3().transcribe_s3(s3_path)
# # #
# # #     else:
# # #         input_json_file = conversation_filename
# # #         output_filename = "{}_output.txt".format(input_json_file[:-5])
# # #         f = open(input_json_file, "r")
# # #         conversation_json = json.loads(f)
# # #         print("Outputfilename:",output_filename)
# # #         conversation_log = test_s3().transcribe_local(conversation_json, output_filename)
# # #         if len(conversation_log) > 1:
# # #             log_file = open(output_filename, "w")
# # #             log_file.write(conversation_log)
# #
# #
# # # import json
# # #
# # # transcripts="C:\\Users\\amaddula\\Downloads\\QWVmFXjFxPo7zUA_2250387698048_20231102.mp3.json"
# # # def print_transcripts(json_data):
# # #     transcripts = json_data.get("transcripts", [])
# # #
# # #     for transcript in transcripts:
# # #         text = transcript.get("text", "")
# # #         speaker = transcript.get("speaker", "")
# # #
# # #         print(f"Speaker: {speaker}")
# # #         print("Transcript:")
# # #
# # #         # Split the text into lines and print each line
# # #         lines = text.split('\n')
# # #         for line in lines:
# # #             print(line)
# # #
# # #         print("\n" + "=" * 20 + "\n")  # Separate transcripts with a line
# # #
# # #
# # # if __name__ == "__main__":
# # #     # Load your JSON data (replace this with your actual JSON data)
# # #     json_data = {
# # #         "transcripts": [
# # #             {"text": "This is the first paragraph. It might have multiple lines.\n\nThis is the second paragraph.",
# # #              "speaker": "speaker_1"},
# # #             {"text": "Another transcript with a single paragraph.", "speaker": "speaker_2"},
# # #             {"text": "A third transcript.\nWith line breaks.", "speaker": "speaker_3"}
# # #         ]
# # #     }
# # #
# # #     print_transcripts(json_data)
# #
# import requests
# import time
# from selenium import webdriver
# import json
# def test_api():
#     # Step 1: Prepare Data
#     first_name = "MAGDALENE"
#     ## MAGDALENE,GIBSON,1949-05-14
#     ### ARTHUR,DAVIS,1946-03-21
#     last_name = "GIBSON"
#     dob = "1949-05-14"
#     method = "POST"
#     # api_url = "https://internal-service.choosekeentech.com"
#     auth_user = "aledade"
#     auth_password = "XzwQvF>JtgWr0"
#     api_url = "https://qa-aledade.choosekeentech.com/aledade/user/details"
#     params = {"first_name": first_name, "last_name": last_name, "dob": dob}
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Basic YWxlZGFkZTpYendRdkY+SnRnV3Iw",  # Include if needed for authentication
#         "Accept": "application/json",
#         "User-Agent": "PostmanRuntime/7.35.0",
#     }
#     response = requests.request(
#         method,
#         api_url,
#         auth=(auth_user, auth_password),
#         json=params,
#     )
#     response = requests.post(api_url, headers=headers, json=params)
#     api_data_output = response.json()
#     try:
#         # Check if the request was successful (status code 200)
#         response.raise_for_status()
#         # api_data_output = response.json()
#         time.sleep(15)
#         print("API_Data_output:",api_data_output)
#         print("Hi")
#         # result_value = api_data_output.get('result')
#         # nested_value = api_data_output.get('nested', {}).get('Medication')
#         # patient_data=api_data_output.get('nested', {}).get('patient')
#         # physicians=api_data_output.get('nested', {}).get('Physicians')
#         # Rest of your code
#     except requests.exceptions.RequestException as e:
#         print(f"Error: {e}")
# # # def test_formattext():
# # #     json_data = '''
# # #     {
# # #         "medications": [
# # #             {"medication_name": "Medication A", "dosage": "10mg"},
# # #             {"medication_name": "Medication B", "dosage": "20mg"}
# # #         ],
# # #         "physicians": [
# # #             {"physician_name": "Dr. Smith", "specialty": "Cardiology"},
# # #             {"physician_name": "Dr. Johnson", "specialty": "Dermatology"}
# # #         ],
# # #         "members": [
# # #             {"member_name": "John Doe", "age": 30},
# # #             {"member_name": "Jane Doe", "age": 25}
# # #         ]
# # #     }
# # #     '''
# # #     try:
# # #         data = json.loads(json_data)
# # #     except json.JSONDecodeError as e:
# # #         print(f"Error decoding JSON: {e}")
# # #         data = {}
# # #
# # #     # Convert the JSON data to a formatted text string
# # #     text = json.dumps(data, indent=2)
# # #
# # #     # Print or use the formatted text as needed
# # #     print(text)
# # #     medications = text.get('medications', [])
# # #     physicians = text.get('patient', [])
# # #     members = text.get('members', [])
# # #     print("Medications:", medications)
# # #     print("Physicians:", physicians)
# # #     print("provider:", members)
# # import time
# # import datetime
# # from datetime import datetime
# # def test_extract_month_and_year():
# #     # date_obj = datetime.strptime(date, "%m %d, %Y")
# #     from datetime import datetime
# #     current_datetime = datetime.now()
# #
# #     # Format and print only month and day
# #     formatted_month_day = current_datetime.strftime("%m/%d")
# #     print("Month and Day:", formatted_month_day)
# #     latest_date=formatted_month_day+"/"+"1946"
# #     print("latest_date:",latest_date)
# # # test_extract_month_and_year("1/1/1946")
# # # extract_month_and_year("07/12/2023")
# import time
#
# from selenium.webdriver.common.by import By
#
#
# # def test_sunfire():
# #     from selenium import webdriver
# #     from selenium.webdriver.common.action_chains import ActionChains
# #
# #     # Create a WebDriver instance (e.g., ChromeDriver)
# #     driver = webdriver.Chrome()
# #     # Open a webpage
# #     driver.get("https://www.sunfirematrix.com/app/agent/yourmedicare")
# #     time.sleep(10)
# #     driver.find_element(By.XPATH,"//h3[text()='Quick links']/parent::div//a[@href='#/contacts']").click()
# #     time.sleep(10)
# #     driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("")
# #     driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("")
# #     driver.find_element(By.XPATH,"//label[text()='Disposition']/parent::div//button[@class='not-selected dropdown-toggle btn btn-tertiary']").click()
# #     time.sleep(5)
# #     driver.find_element(By.XPATH,"")
# #
# #     # Locate the element on which you want to perform the right-click
# #     element_to_right_click = driver.find_element(By.XPATH,"example_element_id")
# #
# #
# #     # Use ActionChains to perform the right-click
# #     actions = ActionChains(driver)
# #     actions.context_click(element_to_right_click).perform()
# #
# #     # After performing the right-click, you might want to do something like selecting an option from the context menu
# #     # For example, pressing 'T' after right-clicking (replace with your specific use case)
# #     actions.send_keys('T').perform()
# #
# #     # Close the browser window
# #     driver.quit()



from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "-Q7phjD_ICn4NzLA_1982487653049_1982487653049_20230403"
job_uri = "s3://restrictedaccessfiles/call_analytics/call_recordings/-Q7phjD_ICn4NzLA_1982487653049_1982487653049_20230403.mp3"
print("job_name:",job_name)
print("job_url:",job_uri)
transcribe.start_medical_transcription_job(
      MedicalTranscriptionJobName = job_name,
      Media = {'MediaFileUri': job_uri},
      LanguageCode = 'en-US',
      ContentIdentificationType = 'PHI',
      Specialty = 'PRIMARYCARE',
      Type = 'DICTATION',
      OutputBucketName = 's3://restrictedaccessfiles/call_analytics/call_recordings/call_recording_output/'
  )
while True:
    status = transcribe.get_medical_transcription_job(MedicalTranscriptionJobName = job_name)
    if status['MedicalTranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
    print("Not ready yet...")
    time.sleep(5)
print(status)