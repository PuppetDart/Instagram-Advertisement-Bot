from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
#defining
desired_cap=  {
    "deviceName": "fd656ac0f936",
    "platformName": "Android",
    "appActivity": "com.instagram.mainactivity.MainActivity",
    "appPackage": "com.instagram.android"
}

#setting the driver server
driver=webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
driver.implicitly_wait(5)

#starting the app
cont=driver.find_element_by_id('com.instagram.android:id/facebook_text_switcher')
driver.implicitly_wait(5)
cont.click()
driver.implicitly_wait(5)
#app started

#entering the search item
search_item=driver.find_element_by_xpath('//android.widget.FrameLayout[@content-desc="Search and Explore"]/android.widget.ImageView')
driver.implicitly_wait(5)
search_item.click()
driver.implicitly_wait(5)

search_item=driver.find_element_by_id('com.instagram.android:id/action_bar_search_edit_text')
search_item.click()

#dealing with the pop up permission
driver.implicitly_wait(5)
allow=driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_always_button')
driver.implicitly_wait(5)
allow.click()

#reconcentrating on search
search_item=driver.find_element_by_id('com.instagram.android:id/action_bar_search_edit_text')
search_item.click()
driver.implicitly_wait(5)

#passing the name
search_item.send_keys('dhruvrathee')
driver.implicitly_wait(5)

#selecting the first search item
select=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]')
driver.implicitly_wait(5)
select.click()
driver.implicitly_wait(5)

#opening the followers list
followers=driver.find_element_by_id('com.instagram.android:id/row_profile_header_textview_followers_count')
driver.implicitly_wait(5)
followers.click()
driver.implicitly_wait(5)  

#clicking the users
for i in range(2,100000):
    x=str(i)
    y='3'
    print(i)
    user=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.FrameLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout['+y+']/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]')
    if i>2:
        driver.implicitly_wait(5)  
        driver.swipe(300,427,300,267)
    driver.implicitly_wait(5)  
    user.click()
    try:
        message=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[2]')
        driver.implicitly_wait(5)
        message.click()
        driver.implicitly_wait(5)  
        msg_in=driver.find_element_by_id('com.instagram.android:id/row_thread_composer_edittext')
        driver.implicitly_wait(5)  
        msg_in.send_keys('https://youtu.be/69y-u05h9TY')
        driver.implicitly_wait(5)  
        send=driver.find_element_by_id('com.instagram.android:id/row_thread_composer_button_send')
        driver.implicitly_wait(5)  
        send.click()
        driver.implicitly_wait(5)  
        back=driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Back"]')
        driver.implicitly_wait(5)  
        back.click()
        #i=i-1
    except:
        pass
    driver.implicitly_wait(5)  
    back=driver.find_element_by_xpath('//android.widget.ImageView[@content-desc="Back"]')
    driver.implicitly_wait(5)  
    back.click()


#follows=driver.find_element_by_id('com.instagram.android:id/follow_list_username')
#follows=driver.find_element_by_id('com.instagram.android:id/action_bar_button_back')