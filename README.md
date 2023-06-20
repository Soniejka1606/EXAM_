# Multiplatform Dating Bot

This project is a multiplatform dating bot that works on both Telegram and VKontakte. The bot acts as a mediator between people, allowing them to fill out their profiles and partner preferences. The bot displays user cards, and if one partner likes another, the card of the first partner is added to the queue of the second partner's cards. If the second partner reciprocates, the bot establishes a connection between them, helping to avoid unwanted meetings or deanonymization.

### Platforms

The bot operates on Telegram and VKontakte platforms with equal capabilities and interaction with users.

### Management System

The management system is built using the PyQT5 library, which enables the addition and editing of advertisements.

## Registration

To register users, the following information needs to be provided:

- Login
- Password
- Region

All information is stored in a database, and the database is created using the sqllite3 library.

## User Profiles

Each user has a profile containing the following information:

- Photos (ability to upload multiple)
- Name
- Age
- Description
- User's positive qualities
- User's negative qualities

The following information is provided to users when viewing cards:

- Photo (up to 3 photos)
- Name
- Age
- Description
- User's positive qualities
- User's negative qualities

## Business Process

### Advertising

The bot also functions as an advertising platform, allowing the insertion of ads while users view cards. The administrative panel of the management system allows the administrator to input advertising announcements. The advertising announcement is presented in the form of an image.

The administrator has the ability to specify the number of times the advertisement will be shown. On every n-th card view (where n is a random number within a specified range set by the administrator), an advertisement will be displayed. The advertising can be targeted to a specific gender and age range from three categories (18-25, 25-40, 40+).

The administrator has the ability to interrupt the display of advertisements. Additionally, it is implemented that the same user should not encounter the same advertisement twice in a row or more than twice.

The application also collects statistics on the number of views.

## Filtering Unwanted Content

The bot performs the function of filtering negative expressions and unacceptable content, as well as preventing the display of pornographic content. The following services are used for this purpose:

- [https://lf.statusnick.com](https://lf.statusnick.com)
- [https://pikabu.ru/story/proveryaem_foto_na_nalichie_zapreshchenki_8589636](https://pikabu.ru/story/proveryaem_foto_na_nalichie_zapreshchenki_8589636)


## Dependencies

The project utilizes the following libraries:
- Telebot: a Python library for working with the Telegram Bot API.
- vk_api: a Python library for working with the VKontakte API.
- PyQT5: for creating the management system (SU) and application interface.
- sqllite3: for working with the database and storing information about users and advertisements.
- requests: a Python library designed to simplify working with HTTP requests.
- threading: a module in the Python standard library that provides functionality for working with threads (for running two bots simultaneously).
