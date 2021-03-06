# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.fill_form(Contact(first_name="FirstName", last_name="LastName", nick="nick", home_phone="999-000-111", mobile_phone="888-000-222", email="test@test.pl"))
    app.session.logout()


def test_add_empty_contact(app):
    app.session.login("admin", "secret")
    app.contact.fill_form(Contact(first_name="", last_name="", nick="", home_phone="", mobile_phone="", email=""))
    app.session.logout()