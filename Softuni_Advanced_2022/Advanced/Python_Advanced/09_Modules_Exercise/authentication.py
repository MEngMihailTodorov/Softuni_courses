from canvas import *
from helpers import clean_screen


def render_entry():
    register_button = Button(
         root,
         text='Register',
         bg='light blue',
         fg='black',
         borderwidth=0,
         width=20,
         height=3,
         command=register
    )
    login_button = Button(
        root,
        text='Login',
        bg='pink',
        fg='black',
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350,320, window=login_button)


def register():
    clean_screen()

    frame.create_text(100, 30, text="First name:")
    frame.create_text(100, 60, text="Last name:")
    frame.create_text(100, 90, text="Username:")
    frame.create_text(100, 120, text="Password:")

    frame.create_window(200, 30, window=first_name_box)
    frame.create_window(200, 60, window=last_name_box)
    frame.create_window(200, 90, window=username_name_box)
    frame.create_window(200, 120, window=password_box)

    registration_button = Button(
        root,
        text='Register',
        bg='light blue',
        fg='black',
        command='registration'
    )

    frame.create_window(200, 200, window=registration_button)


def registration():
    user_info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_name_box.get(),
        "password": password_box.get(),
        "products": []
    }
    pass


def check_registration():
    



def login():
    clean_screen()

    pass


first_name_box = Entry(root,bd=0)
last_name_box = Entry(root,bd=0)
username_name_box = Entry(root,bd=0)
password_box = Entry(root,bd=0)