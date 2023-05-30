# App description

## django-boatrent v0.1 alpha

This is a simple boat rental service application that allows to rent a boat for a day or a longer period of time.

Everyone can make a booking, but only admin is able to modify and delete bookings.

# Screenshots

## Anonymous user is able to browse the website and create booking

![Create new order](1.png "Create new order")

## Booking confirmation

When new booking is created system verifies that there are no overlappings and provides a summary with calculated price.

![Booking summary](2.png "Bookings summary")

## Logged in user is able to list bookings and modify them

![Booking list](3.png "Booking list")

Note that modify view is different compared to create new booking view, admin is able to see and modify "price" field as well. 

![Modify booking](4.png "Delete booking")

Admin can also modify any field in the booking and delete the booking completely.

![Delete booking](5.png "Delete booking")

# URL of Admin panel

Admin panel URL has been modified slightly from default.

https://yoursite.com/adm-boatski/

![Delete booking](6.png "Delete booking")

# TODO
This is an MVP alpha version, a lot of functionality needs to be added, such as:

- Implement HTTPS (certbot)
- UI improvements (adding boat pictures, dock location, etc)
- Add detailed instructions and boat descriptions
- Update RentalPrices from JSON
- Add checks and validations
- Notification e-mails (Mailgun)

# Deployment process

This was deployed on a Debian 11 server.

Please refer to [a guide by Tero Karvinen](https://terokarvinen.com/2022/deploy-django/?fromSearch=deploy) for detailed explanation of the deployment process.

# Make sure to run the app within the virtual environment

First you need to create a new virtualenv and install django

	virtualenv --system-site-packages -p python3 env/

--system-site-package uses the packages installed by apt-get whenever possible.

If you don't have a virtualenv installed, you need to install one. On Ubuntu or Debian Linux, you can do it with apt-get

	apt-get -y install virtualenv

Start your virtual env

	source env/bin/activate

To stop virtualenv

	deactivate

# References
https://terokarvinen.com/2023/django-cheatsheet/

https://terokarvinen.com/2022/deploy-django/
