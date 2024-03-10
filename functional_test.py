import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        FFoptions = Options()
        # FFoptions.add_argument("--headless")
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
        header_text = self.browser.find_element(By.TAG_NAME, "h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        input_box = self.browser.find_element(By.ID, "id_new_item")
        self.assertEqual(input_box.get_attribute("placeholder"), "Enter a to-do item")

        # She types "Buy peacock feathers" into a text box
        # (Edith's hobby is tying fly-fishing lures)
        input_box.send_keys("Buy peacock feathers")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")

        # self.fail("remove this line after finishing: http://www.obeythetestinggoat.com/book/chapter_04_philosophy_and_refactoring.html#_recap_the_tdd_process")

        """self.assertTrue(
            any(row.text == "1: Buy peacock feathers" for row in rows),
            f"New to-do item did not appear in table Contents were:\n {table.text}",
        )"""
        self.assertIn("1: Buy peacock feathers", [row.text for row in rows])

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock feathers to make a fly" (Edith is very methodical)

        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # The page updates again, and now shows both items on her list
        table = self.browser.find_element(By.ID, "id_list_table")
        rows = table.find_elements(By.TAG_NAME, "tr")
        self.assertIn(
            "1: Buy peacock feathers",
            [row.text for row in rows],
        )
        self.assertIn(
            "2: Use peacock feathers to make a fly",
            [row.text for row in rows],
        )

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


## about difference bw unit and functional test (http://www.obeythetestinggoat.com/book/chapter_03_unit_test_first_view.html)
# Unit Tests, and How They Differ from Functional Tests
#
# As with so many of the labels we put on things, the line between unit tests and functional tests can become a little blurry at times.
# The basic distinction, though, is that functional tests test the application from the outside, from the user’s point of view.
# Unit tests test the application from the inside, from the programmer’s point of view.
#
# The TDD approach I’m demonstrating uses both types of test to drive the development of our application, and ensure its correctness.
# Our workflow will look a bit like this:
#
#   1)We start by writing a functional test, describing a typical example of our new functionality from the user’s point of view.#
#   2)Once we have a functional test that fails, we start to think about how to write code that can get it to pass (or at least to get past its current failure). We now use one or more unit tests to define how we want our code to behave—​the idea is that each line of production code we write should be tested by (at least) one of our unit tests.
#   3)Once we have a failing unit test, we write the smallest amount of application code we can, just enough to get the unit test to pass. We may iterate between steps 2 and 3 a few times, until we think the functional test will get a little further.
#   4)Now we can rerun our functional tests and see if they pass, or get a little further. That may prompt us to write some new unit tests, and some new code, and so on.
#   5)Once we’re comfortable that the core functionality works end-to-end, we can extend out to cover more permutations and edge cases, using just unit tests now.
#
# You can see that, all the way through, the functional tests are driving what development we do from a high level, while the unit tests drive what we do at a low level.
# The functional tests don’t aim to cover every single tiny detail of our app’s behaviour, they are there to reassure us that everything is wired up correctly. The unit tests are there to exhaustively check all the lower level details and corner cases.
# !Functional tests should help you build an application that actually works, and guarantee you never accidentally break it. Unit tests should help you to write code that’s clean and bug free.
###

## on VCS hygien
# For me the main big of VCS hygiene is: make sure you always review what you’re about to commit before you do it.
"""
$ git status  # should show you lists/ is untracked
$ git add lists
$ git diff --staged  # will show you the diff that you're about to commit
$ git commit -m "Add app for lists, with deliberately failing unit test"
"""

## On refactoring (http://www.obeythetestinggoat.com/book/chapter_04_philosophy_and_refactoring.html)
# martin Fowler’s Refactoring(http://refactoring.com/).


# a word on sec/hacking http://www.obeythetestinggoat.com/book/chapter_05_post_and_database.html
# I want to recommend the textbook from that course,
# Ross Anderson’s Security Engineering_.
# https://www.cl.cam.ac.uk/~rja14/book.html
# It’s quite light on pure crypto, but it’s absolutely full of interesting
# discussions of unexpected topics like lock picking,
# forging bank notes, inkjet printer cartridge economics,
# and spoofing South African Air Force jets with replay attacks.
# It’s a huge tome, about three inches thick, and I promise you it’s an absolute page-turner.

# http://www.obeythetestinggoat.com/book/chapter_05_post_and_database.html#three_strikes_and_refactor
# See also Three Strikes and Refactor for a further note of caution on applying DRY too quickly.
