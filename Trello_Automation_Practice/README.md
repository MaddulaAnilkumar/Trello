# Selenium Python Framework

### _Test Automation Framework built with Selenium and Python Pytest for browser testing._

## Prerequisites
- Install Python
- Install pip
- pycharm editor

## Installation Steps:
- Clone this repo
- Navigate to root folder
- pip install -r requirements.txt

## Features 
 - Framework follows page object pattern
 - Logger has been implemented 
 - Integrated allure report and screenshot 
 - Run tests on any browser such as Chrome and firefox
 - Read form environment variables to fetch username, password and URL
 - Read test data from .env file

## Basic set up to pass environment variables 
Create a .env file in root directory and provide details such as username, password to login to app and which url needs to be opened

```
user=test
password=xxx
testenv=qa
browser=chrome
url=https://trello.com/login


## Run Tests and generate report 
To generate all tests report using Allure you need to run tests by command first:

```$ pytest -v -s tests --alluredir=allure-results ```

After that you need to use command:

```$ allure serve allure-results ```
