from model.contact import Contact


def test_modification_contact(app):
    app.session.login("admin", "secret")
    app.contact.modification_first_contact(Contact(first_name="UpdateName", last_name="UpdateLastName", nick="Updatenick", home_phone="999-999-999", mobile_phone="48 000-000-000", email="Updatetest@test.pl"))
    app.session.logout()