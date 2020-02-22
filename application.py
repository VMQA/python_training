from selenium import webdriver
class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        driver = self.wd
        driver.get("http://localhost/addressbook")

    def login(self, username, password):
        driver = self.wd
        self.open_home_page()
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("%s" % username)
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("%s" % password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups_page(self):
        driver = self.wd
        driver.find_element_by_link_text("groups").click()

    def create_group(self, group):
        driver = self.wd
        self.open_groups_page()
        # init group creation
        driver.find_element_by_xpath("//input[@name='new']").click()
        # fill group form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        driver.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        driver = self.wd
        driver.find_element_by_link_text("group page").click()

    def logout(self):
        driver = self.wd
        driver.find_element_by_link_text("Logout").click()

    def destroy(self):
        self.wd.quit()

    def create_contact(self, contact):
        driver = self.wd
        # init contact creation
        driver.find_element_by_link_text("add new").click()
        # input First name
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.first_name)
        # input Last name
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.last_name)
        # input address
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(contact.address)
        # input email
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.email)
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        #return to home page
        driver.find_element_by_link_text("home page").click()


