from selenium.webdriver.support.ui import Select
from model.contact import Contact


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
        self.contact_cache = None

    def edit_empty_name(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()
        return wd.find_element_by_xpath('//input[@name="firstname"]').get_attribute("value")

    def edit_first_contact(self):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Нажимаем кнопку Edit
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()
        self.fill_contact_form(new_contact_data)
        # Нажимаем кнопку Update
        wd.find_element_by_xpath('//input[@value="Update"][2]').click()
        self.return_to_homepage()
        self.contact_cache = None

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
        select = Select(wd.find_element_by_xpath('//select[@name="bday"]'))
        select.select_by_value(contact.BirthdayDay)
        select = Select(wd.find_element_by_xpath('//select[@name="bmonth"]'))
        select.select_by_value(contact.BirthdayMonth)
        self.change_field_value("byear", contact.BirthdayYear)
        self.change_field_value("address2", contact.Address2)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Нажимаем кнопку удалить
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        # Подтверждаем удаление
        wd.switch_to_alert().accept()
        self.app.open_home_page()
        self.contact_cache = None

    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_xpath('//tr[@name="entry"]'):
                text1 = element.find_element_by_xpath('td[3]').text
                text2 = element.find_element_by_xpath('td[2]').text
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(Contact(Firstname=text1, Lastname=text2, id=id))
        return list(self.contact_cache)