import json
import os.path
from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact

class AddressBook:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'], password=db_config['password'])

    def destroy_fixtures(self):
        self.dbfixture.destroy()
        self.fixture.destroy()

    # Groups

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def delete_first_group(self):
        self.fixture.group.delete_first_group()

    def edit_group(self, source_group, new_data_group):
        self.fixture.group.edit_group_by_id(source_group.id, new_data_group)

    def group_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Group.id_or_max) == sorted(list2, key=Group.id_or_max)

    # Contacts

    def new_contact(self, lastname, firstname, address, homephone, mobilephone, workphone, secondaryphone, email, email2, email3):
        return Contact(lastname=lastname, firstname=firstname, address=address,
                       homephone=homephone, mobilephone=mobilephone, workphone=workphone,
                       secondaryphone=secondaryphone, email=email, email2=email2, email3=email3)

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def delete_first_contact(self):
        self.fixture.contact.delete_first_contact()

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def edit_contact(self, source_contact, new_data_contact):
        self.fixture.contact.edit_contact_by_id(source_contact.id, new_data_contact)

    def contact_lists_should_be_equal(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)