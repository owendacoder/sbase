from seleniumbase import BaseCase


class HomeTest(BaseCase):
    def test_home_page(self):
        # open a page
        self.goto("https://www.amazon.com/")

        # click on "Sign in"
        self.click('//*[@id="nav-link-accountList"]/span')
        print(self.get_title())
        # a little comment here
        self.assert_title("Amazon Sign-In")

    def test_nypl_book_lists(self):
        # open the page
        self.goto("http://qa-lists.nypl.org/books-music-dvds/recommendations/lists/")

        # click on the links and go back

        list_length = len(self.find_elements("/html/body/div/div/div/div/div[2]/div"))

        count = 0

        for x in range(1, list_length + 1):
            print(x)
            self.click("/html/body/div/div/div/div/div[2]/div[" + str(x) + "]/a")
            self.wait(2)
            if "nable to complete this" in self.get_text('//*[@id="userlists"]/div'):
                print(self.get_current_url())
            self.goto("http://qa-lists.nypl.org/books-music-dvds/recommendations/lists/")
            count += 1

        print("Count of the libraries are = " + str(count))

