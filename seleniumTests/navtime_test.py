import constants as c
# Use Selenium to Measure Web Timing
# Performance Timing Events flow
# navigationStart -> redirectStart -> redirectEnd -> fetchStart -> domainLookupStart -> domainLookupEnd
# -> connectStart -> connectEnd -> requestStart -> responseStart -> responseEnd
# -> domLoading -> domInteractive -> domContentLoaded -> domComplete -> loadEventStart -> loadEventEnd


def test_backend(browserdriver):
    browserdriver.get(c.HOME_URL)

    navigationStart = browserdriver.execute_script("return window.performance.timing.navigationStart")
    responseStart = browserdriver.execute_script("return window.performance.timing.responseStart")

    backendPerformance = responseStart - navigationStart

    print("Back End: %s" % backendPerformance)

    assert backendPerformance < 500, "Backend has long loading time."

def test_frontend(browserdriver):
    browserdriver.get(c.HOME_URL)

    responseStart = browserdriver.execute_script("return window.performance.timing.responseStart")
    domComplete = browserdriver.execute_script("return window.performance.timing.domComplete")

    frontendPerformance = domComplete - responseStart

    print("Front End: %s" % frontendPerformance)

    assert frontendPerformance < 500, "Frontend has long loading time."   