from selenium import webdriver
browser = webdriver.Chrome('chromedriver.exe')
browser.get('https://www.google.com/search?q=hello&rlz=1C1SQJL_jaJP784JP784&oq=hello&aqs=chrome..69i57.2534j0j1&sourceid=chrome&ie=UTF-8')
elem_search = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div/div[2]/input')
elem_search.clear()
elem_search.send_keys('SEO')
elem_next = browser.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/button').click()