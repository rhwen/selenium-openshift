# py remote_test.py

from selenium.webdriver import Remote

driver = Remote(command_executor="http://11.11.136.113:31444/wd/hub",
        desired_capabilities={'platform': 'ANY',
                              'browserName': 'chrome',
                              'version': '',
                              'javascriptEnabled': True}
        )
driver.set_page_load_timeout(5)
driver.get('http://11.11.136.113:31444/grid/console')
driver.find_element_by_id('kw').send_keys("remote")
driver.find_element_by_id("su").click

driver.quit()
