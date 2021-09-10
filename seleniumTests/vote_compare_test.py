from time import sleep
import constants as c

# the goal is to run the same task from 2 users
# to see if vote changes can be seen by the other in real time

# for now create a test that opens multiple tabs in the same window

def test_open_tabs(browserdriver):
    # go to specific task
    browserdriver.get('http://localhost/#/task/061c24b959994ba3be05fcd51e7cf1a3')

    browserdriver.implicitly_wait(10)

    # open a new tab
    browserdriver.execute_script("window.open('http://localhost/#/user-select', 'new tab')")

    sleep(1)

    # open a third tab
    browserdriver.execute_script("window.open('https://www.google.com');")
    sleep(1)

    # go to previous tab
    browserdriver.switch_to.window(browserdriver.window_handles[-1])

    sleep(1)

    # go back to main tab
    browserdriver.switch_to.window(browserdriver.window_handles[0])

    sleep(1)
