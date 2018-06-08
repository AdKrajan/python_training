# -*- coding: utf-8 -*-
import pytest
from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.fill_contact_form(Contact(first_name="FirstName", last_name="LastName", nick="nick", home_phone="999-000-111", mobile_phone="888-000-222", email="test@test.pl"))
    app.logout()


def test_add_empty_contact(app):
    app.login("admin", "secret")
    app.fill_contact_form(Contact(first_name="", last_name="", nick="", home_phone="", mobile_phone="", email=""))
    app.logout()
