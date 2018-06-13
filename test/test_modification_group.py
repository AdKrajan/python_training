from model.group import Group

def test_modification_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modification_first_group(Group(name="NameGroup", header="HeaderGroup", footer="FooterGroup"))
    app.session.logout()