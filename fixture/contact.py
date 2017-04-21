from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re


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
        wd.find_element_by_xpath('//input[@value="Enter"][2]').click()
        self.return_to_homepage()
        self.contact_cache = None

    def add_contact_to_group_by_name(self, contact_id, group_id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").click()
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_value(group_id)
        wd.find_element_by_xpath('//input[@value="Add to"]').click()
        wd.find_element_by_xpath('//i//*[contains(text(),"group page")]').click()

    def sort_by_group_by_id(self, group_id):
        wd = self.app.wd
        select = Select(wd.find_element_by_xpath('//select[@name="group"]'))
        select.select_by_value(group_id)

    def edit_empty_name(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath('//img[@title="Edit"]')[index].click()
        return wd.find_element_by_xpath('//input[@name="firstname"]').get_attribute("value")

    def edit_empty_name_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element_by_xpath("//input[@id=" + id + "]//../following-sibling::td//img[@title='Edit']").click()
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

    def edit_contact_by_id(self, id, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # Нажимаем кнопку Edit
        wd.find_element_by_xpath("//input[@id="+id+"]//../following-sibling::td//img[@title='Edit']").click()
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
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("email", contact.email)
        self.change_field_value("homepage", contact.homepage)
        select = Select(wd.find_element_by_xpath('//select[@name="bday"]'))
        select.select_by_value(contact.birthdayday)
        select = Select(wd.find_element_by_xpath('//select[@name="bmonth"]'))
        select.select_by_value(contact.birthdaymonth)
        self.change_field_value("byear", contact.birthdayyear)
        self.change_field_value("address2", contact.address2)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id(id).click()

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

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
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
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(
                    Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                            all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_details_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").text
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address, homephone=homephone,
                       mobilephone=mobilephone, workphone=workphone, secondaryphone=secondaryphone, email=email,
                       email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_details_by_index(index)
        id = wd.find_element_by_name("id").get_attribute("value")
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text)
        workphone = re.search("W: (.*)", text)
        mobilephone = re.search("M: (.*)", text)
        secondaryphone = re.search("P: (.*)", text)
        return Contact(id=id, homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone)

    def get_contact_info_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cells = row.find_elements_by_tag_name("td")
        id = cells[0].find_element_by_tag_name("input").get_attribute("value")
        firstname = cells[2].text
        lastname = cells[1].text
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                                          all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones)

    def get_contact_info_by_id(self, contact_id):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_element_by_xpath('//td/*[@id="'+contact_id+'"]/../..')
        cells = row.find_elements_by_tag_name("td")
        id = cells[0].find_element_by_tag_name("input").get_attribute("value")
        firstname = cells[2].text
        lastname = cells[1].text
        address = cells[3].text
        all_emails = cells[4].text
        all_phones = cells[5].text
        return Contact(id=id, firstname=firstname, lastname=lastname, address=address,
                       all_emails_from_home_page=all_emails, all_phones_from_home_page=all_phones)

    def find_contact_in_group_and_delete(self, group_id):
        wd = self.app.wd
        self.app.open_home_page()

