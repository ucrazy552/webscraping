from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

import time 


#Global stuff
browser = webdriver.Chrome('/Users/roydejong/Desktop/chromedriver')

#Sign up details 
pinterest_email = input('Email Address: ')
pinterest_wachtwoord = input('Password: ')


#Keyword to target on pinterest 
important_keyword = input('Keyword: ') 


#default workflow 
def default_work_flow(): 
    print("Running automation") 
    #Initiating the connection with the pinterest website 
    website = browser.get('https://nl.pinterest.com/')
    #Caaling the function to click on the button 
    #clickButton('tBJ.dyH.iFc.yTZ.pBj.tg7.mWe')
    clickButton('tBJ.dyH.iFc.yTZ.erh.tg7.mWe')
    #Some time to not make it look spammy
    time.sleep(1)
    #Some time to not make it look spammy
    login()
    time.sleep(1)
    #Running the searchbar function 
    searchBar()




#Function that will click on buttons 
def clickButton(buttonId):
    #Gets the element css selector and peforms a click event on it 
    #So it directs to the sign up page 
    browser.find_element_by_class_name(buttonId).click()

#Will look things up in the search bar 
def searchBar(): 
    search_bar = browser.find_element_by_name("searchBoxInput")
    time.sleep(2)
    search_bar.send_keys(important_keyword)
    time.sleep(2)
    search_bar.send_keys(Keys.ENTER)





#Will try to log in to the website 
def login(): 
    #Filling out email user input 
    p_email = browser.find_element_by_id("email")
    p_email.send_keys(pinterest_email)

    time.sleep(5) 
    #Filling out the 
    p_pass = browser.find_element_by_id("password")
    p_pass.send_keys(pinterest_wachtwoord)
    p_pass.submit()

 


#Runs the default function 
default_work_flow()     

