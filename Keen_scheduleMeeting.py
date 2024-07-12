from selenium.webdriver.common.by import By
from utilities.action_utils import ActionUtils

class Keen_Scedule_Meeting(ActionUtils):
    member_name=(By.XPATH,"//flexipage-component2[@data-target-selection-name='c_customAccountCmp']//span[@class='slds-text-heading_small slds-truncate']")
    meeting = (By.XPATH, "(//button[@title='Schedule Meeting'])")
    cookies=(By.XPATH,"//button[text()='Accept cookies']")
    calendly=(By.XPATH,"//h1[text()='Innominds Development']")
    test=(By.XPATH,"//div[text()='Test']")
    date_sheet=(By.XPATH,"//h2[text()='Select a Date & Time']")
    verify_avaliable_dates=(By.XPATH,"(//tbody//button[@class='o5PJ_9jHomezuy5op7Th gyO7ZjgvT__guDnWiKg5 mIJUmpwwZd5mH9SMq9XQ EB2mi2RIA2h7Wxx0AwVH kSlFN4st3jDtREypXE1G Mgn_oZenegAhr3_8YPJ2 d0wC8bgLHW4KRF7spxB1'])[1]")
    date_available=(By.XPATH,"//tbody//button[@class='o5PJ_9jHomezuy5op7Th gyO7ZjgvT__guDnWiKg5 mIJUmpwwZd5mH9SMq9XQ EB2mi2RIA2h7Wxx0AwVH kSlFN4st3jDtREypXE1G Mgn_oZenegAhr3_8YPJ2 d0wC8bgLHW4KRF7spxB1']//span")
    next=(By.XPATH,"//button[@class='_NBjM8Q6c03EfxjK90hm _wYinQZCx29_pxs0TZnM Iy168r_YSkmFtzeEXUss uoYd30C1K4Sdef0CubtJ tg_cqD7Ia3z_hRQg_eyg EB2mi2RIA2h7Wxx0AwVH kSlFN4st3jDtREypXE1G Mgn_oZenegAhr3_8YPJ2 d0wC8bgLHW4KRF7spxB1 confirm-button-enter-done']")
    available=(By.XPATH,"//button[@class='o5PJ_9jHomezuy5op7Th gyO7ZjgvT__guDnWiKg5 mIJUmpwwZd5mH9SMq9XQ EB2mi2RIA2h7Wxx0AwVH kSlFN4st3jDtREypXE1G Mgn_oZenegAhr3_8YPJ2 d0wC8bgLHW4KRF7spxB1']")
    name=(By.XPATH,"//input[@name='full_name']")
    available_time=(By.XPATH,"//button[@data-container='time-button']")
    test_page=(By.XPATH,"//h1[text()='Test']")
    email=(By.XPATH,"//input[@name='email']")
    phone=(By.XPATH,"//input[@name='phone_number']")
    schedule_meeting=(By.XPATH,"//button[@type='submit']")
    confirmed_meeting=(By.XPATH,"//h1[text()='Confirmed']")
    verify_BD_activity=(By.XPATH,"//div[@class='standardTimelineUpcomingActivities']//div//a[@class='subjectLink slds-truncate']")
    BD_home=(By.XPATH,"//div[@class='fc-content']")
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
    def schedule_meeting_member(self):
         return self.find_element(*Keen_Scedule_Meeting.member_name)
    def click_schedule_meeting(self):
        return self.click_element(*Keen_Scedule_Meeting.meeting)
    def accept_cookies(self):
        return self.click_element(*Keen_Scedule_Meeting.cookies)
    def title_calendly(self):
        return self.find_element(*Keen_Scedule_Meeting.calendly)
    def click_test(self):
        return self.click_element(*Keen_Scedule_Meeting.test)
    def verify_date_sheet(self):
        return self.find_element(*Keen_Scedule_Meeting.date_sheet)
    def pick_dates(self):
        return self.find_element(*Keen_Scedule_Meeting.verify_avaliable_dates)
    def select_dates(self):
        return self.Find_Elements(*Keen_Scedule_Meeting.date_available)
    def select_time(self):
        return self.Find_Elements(*Keen_Scedule_Meeting.available_time)
    def click_next(self):
        return self.click_element(*Keen_Scedule_Meeting.next)
    def schedule_member_page(self):
        return self.find_element(*Keen_Scedule_Meeting.test_page)
    def enter_name(self,text):
        return self.enter_text(text,*Keen_Scedule_Meeting.name)
    def enter_emali(self,text):
        return self.enter_text(text,*Keen_Scedule_Meeting.email)
    def enter_phone_number(self,text):
        return self.enter_text(text,*Keen_Scedule_Meeting.phone)
    def submit_schedule_meeting(self):
        return self.click_element(*Keen_Scedule_Meeting.schedule_meeting)
    def verify_confirmed_meeting(self):
        return self.find_element(*Keen_Scedule_Meeting.confirmed_meeting)
    def verify_meeting_link(self):
        return self.Find_Elements(*Keen_Scedule_Meeting.verify_BD_activity)
    def verify_Home_BD(self):
        return self.Find_Elements(*Keen_Scedule_Meeting.BD_home)



