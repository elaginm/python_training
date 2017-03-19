from selenium.webdriver.common.keys import Keys


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_new_address(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_new_address()
        self.fill_contact_form(contact)
        # Нажимаем кнопку Enter
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_homepage()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.select_first_contact()
        # Нажимаем кнопку Edit
        wd.find_element_by_xpath('//table/..//tr[2]/td[8]').click()
        self.fill_contact_form(new_contact_data)
        # Нажимаем кнопку Update
        wd.find_element_by_xpath('//input[@value="Update"][2]').click()
        self.return_to_homepage()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.Firstname)
        self.change_field_value("lastname", contact.Lastname)
        self.change_field_value("nickname", contact.Nickname)
        self.change_field_value("title", contact.Title)
        self.change_field_value("company", contact.Company)
        self.change_field_value("address", contact.Address)
        self.change_field_value("home", contact.Homephone)
        self.change_field_value("mobile", contact.Mobilephone)
        self.change_field_value("email", contact.Email)
        self.change_field_value("homepage", contact.Homepage)
        wd.find_element_by_xpath('//select[@name="bday"]').click()
        wd.find_element_by_xpath("//select[@name=\"bday\"]/option[@value='" + str(contact.BirthdayDay) + "']").click()
        wd.find_element_by_xpath('//select[@name="bday"]').send_keys(Keys.ENTER)
        wd.find_element_by_xpath('//select[@name="bmonth"]').click()
        wd.find_element_by_xpath(
            "//select[@name=\"bmonth\"]/option[@value='" + str(contact.BirthdayMonth) + "']").click()
        wd.find_element_by_xpath('//select[@name="bmonth"]').send_keys(Keys.ENTER)
        self.change_field_value("byear", contact.BirthdayYear)
        self.change_field_value("address2", contact.Address2)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_contact()
        # Нажимаем кнопку удалить
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # Подтверждаем удаление
        wd.switch_to_alert().accept()
        self.app.open_home_page()

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()
