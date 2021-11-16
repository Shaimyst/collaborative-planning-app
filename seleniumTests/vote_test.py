
import constants as c


def test_vote(browserdriver):
    
    # driver is set up and ready to go
    browserdriver.get('http://localhost/#/user-select')
    assert browserdriver.current_url == "http://localhost/#/user-select", "FAIL"

    # plan:
    # user 1:
    # go the the user page
    # select a random user
    # go to the tasks page
    # select a random task
    # select a random vote
    # click on that vote
    # assert the vote has been cast

    # user 2: 
    # open a second window
    # random select a different user
    # go to the same task page
    # ** wait until user 1 has voted **
    # assert that vote has changed