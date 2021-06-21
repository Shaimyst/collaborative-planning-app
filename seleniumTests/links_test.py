import seleniumTests.constants as c
# begin test

def test_home_link(browserdriver): # test Home link works
    browserdriver.get(c.HOME_URL)
    home_link = browserdriver.find_element_by_link_text("Home")
    home_link.click()

    browserdriver.implicitly_wait(10)
    print("Current home url: " + browserdriver.current_url)
    
    assert browserdriver.current_url == c.HOME_URL, "not home"

def test_tasks_link(browserdriver): # test tasks link works
    browserdriver.get(c.HOME_URL)
    tasks_link = browserdriver.find_element_by_link_text("Tasks")
    tasks_link.click()

    browserdriver.implicitly_wait(10)

    print("Current tasks url: " + browserdriver.current_url)
    
    assert browserdriver.current_url == c.TASKS_URL, "wrong page"

def test_select_user(browserdriver): # test select user link works
    browserdriver.get(c.HOME_URL)
    select_user_link = browserdriver.find_element_by_link_text("select user")
    select_user_link.click()

    browserdriver.implicitly_wait(10)

    print("Current select user url: " + browserdriver.current_url)
    
    assert browserdriver.current_url == "http://localhost/#/user-select", "wrong page"

def test_create_user(browserdriver): # test create user link works
    browserdriver.get(c.HOME_URL)
    select_user_link = browserdriver.find_element_by_link_text("create user")
    select_user_link.click()

    browserdriver.implicitly_wait(10)

    print("Current user create url: " + browserdriver.current_url)
    
    assert browserdriver.current_url == "http://localhost/#/user-create", "wrong page"

def test_find_elements(browserdriver): # count the elements on a page
    browserdriver.get(c.HOME_URL)

    count = 0

    ids = browserdriver.find_elements_by_xpath('//*[@id]')
    for ii in ids:
        print("Element found: Tag name - " + ii.tag_name + ". Id attribute - " + ii.get_attribute('id'))
        count += 1 # variable will increment every loop iteration of your code

    print("Elements found: " + str(count))
    assert count == 1, "elements count has changed"

def test_find_links(browserdriver): # lists all links on home and tasks page
    browserdriver.get(c.HOME_URL)
    
    count = 0

    elements = browserdriver.find_elements_by_xpath("//a[@href]")
    for elem in elements:
        print("Home page links: " + elem.get_attribute("href"))
        count += 1 # every loop will add one count
    
    # in case you want to see all links found:
    # print("Home page links found: " + str(count))

    tasks_link = browserdriver.find_element_by_link_text("Tasks")
    tasks_link.click()

    elements = browserdriver.find_elements_by_xpath("//a[@href]")
    for elem in elements:
        print("Task page links: " + elem.get_attribute("href"))
        count += 1 # every loop will add one count

    print("Home and Tasks page links found: " + str(count))

    assert count == 6, "wrong number of links"