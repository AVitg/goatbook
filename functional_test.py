import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        FFoptions = Options()
        FFoptions.add_argument("--headless")
        FFservice = Service(executable_path="/snap/bin/geckodriver")
        self.browser = webdriver.Firefox(options=FFoptions, service=FFservice)

    def tearDown(self) -> None:
        super().tearDown()
        self.browser.quit()
        return

    def test_can_start_a_todo_list(self) -> None:
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        # assert "To-Do" in browser.title
        # assert "To-Do" in browser.title, f"Browser title was {browser.title}"
        self.assertIn("To-Do", self.browser.title)

        # She is invited to enter a to-do item straight away
        self.fail("Finish the test!")

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        # The page updates again, and now shows both items on her list

        # Satisfied, she goes back to sleep


if __name__ == "__main__":
    unittest.main()


## clean up git commit, if you added wrong files
# git rm -r --cached superlists/__pycache__
#

## about comments ##
# There is more fun to be had in this area, things like Behaviour-Driven Development
# (see [appendix_bdd]) and building Domain-Specific Languages (DSLs) for testing,
# but they’re topics for other booksfootnote: Check out this video by the great Dave Farley
# if you want a taste: https://youtu.be/JDD5EEJgpHU?t=272 ].
#
# For more on comments, I recommend John Ousterhoudt’s A Philosophy of Software Design
# (https://web.stanford.edu/~ouster/cgi-bin/cs190-spring16/lecture.php?topic=comments),
# which you can get a taste of by reading his lecture notes from the chapter on comments.

## pytest vs unittest: (http://www.obeythetestinggoat.com/book/chapter_02_unittest.html)
# Read Brian Okken’s Python Testing with pytest for an excellent, comprehensive guide to Pytest instead.
# (https://pythontest.com/pytest-book/)

## about errors: (http://www.obeythetestinggoat.com/book/chapter_03_unit_test_first_view.html)
# Zed Shaw memorably insisted in Learn Python The Hard Way(https://learnpythonthehardway.org/),
# this kind of debugging is also an absolutely vital part of learning, so do stick it out!
