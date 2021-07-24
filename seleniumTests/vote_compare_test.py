from time import sleep
import constants as c

# this test is not finished
# the goal is to run the same task from 2 users
# to see if vote changes can be seen by the other in real time

def test_vote_compare(browserdriver):
    browserdriver.get('http://localhost/#/user-select')
    profile001 = browserdriver.find_element_by_xpath("/html/body/div/div[2]/ul/li[4]")
    profile001.click()

    # print(dir())
    
    # for now we're using an existing task, but it should create a new task first
    # change this later
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')

    browserdriver.implicitly_wait(10)

    #open tab
    browserdriver.execute_script("window.open('http://localhost/#/user-select', 'new tab')")


    profile002 = browserdriver.find_element_by_xpath("/html/body/div/div[2]/ul/li[5]")
    profile002.click()
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')
    sleep(5)