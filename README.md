#Project 4
ghghg
[![Build Status](https://travis-ci.org/JohnMellaley/unicorn_attractor.svg?branch=master)](https://travis-ci.org/JohnMellaley/unicorn_attractor)

# Unicorn_attractor
## Overview

This website was set up to that allows registered users to request bug fixes and feature updates to our existing software. We
make money from it by the users paying for extra features, but also helps us remove bugs from our software by having an on-line
community. Bugs and features are prioritised based on the number of votes each has. As bugs are free, users are only allowed to 
vote for each bug once. The bug with the most votes will be worked on. Features on the other hand the user can vote many times 
for each feature, as the user is paying a set fee for each vote. The features with the most votes (or made the most money) will
be worked on first. The company will split its time between working on features and bugs evenly. 

## UX

### What is this website for?
This website was created to create revenue through adding extra features, and also help to identify bugs on our existing software and
and allows us to prioritise the bugs causing the most issues with our customers.
The benfit for the customer is they also get a better product due to reduced bugs in the software, but can also get extra 
features added.

### User Stores
This site is used by anyone using our sofware products. The users will be able to vote on features and bugs to fixed.

**Existing and New Users. **

* Users should be able to see what the company does from the home page.
* Users should be able to some metrics before deciding they want to join
* Users should be to register with the company if they choose to join.
* User should be able to reset there password if they have forgoten it.
* Users should be add bugs
* Users should be able to vote for each bug once.
* Users should be able to comment on all bugs raised. 
* Users should be add features
* Users should be able to vote for each feature as many times as they like.
* Users should be able to add features to a shopping cart.
* Users should be able to amend the shopping cart.
* Users should be able to checkout the shopping cart and pay for the votes by the credit/debit card
* Users should be able to comment on all feature raised. 
* Users should be able to see comments from out users or company employees as well
* Users should have their own profile page with their own bugs and features displayed if any along with some basic personal information.
* Users should be able to dashboard with some site metrices.


In the design of this web page I decided to use Balsamiq to create my wire frames. I did two sets of screens one for mobile and the other for desktop. For mobile I only did screen that were significantly different from large screens. Both can be seen under assets\wire frames folder
within the project.

### How does it work

## Features
 
### Existing Features

* register
    - Can only log in if registered. The home page navbar allows you to do this. Once registered they will be redirected to the home page.

* Login 
    - login in form. Once logged in will be directed to the home page.
    - Can log on with either username or email.
    
* Reset Password
    - Password Reset Form with email
    - Email sent with link to reset users password.
    - Page that allows you change your password.
    - Message to tell you to log in when complete

* Home page
    -  The home page has inforation about the company. Who we are and what we do as well as a two tables with some statistics for both Features and bugs

* Statistics
    - This page contains 5 graphs. 
    - Features vs bugs break down.
    - Bugs with the most likes.
    - Features with the most likes
    - Count of Bugs created by each user
    - Count of Features created by each user
    
* Profile Page
    - This page has all the Bugs and features you have created as well as your name and e-mail address at the top.

* Bugs Page
    - Displays all bugs created on one page with all there detials and status.

* Add Bug Page
    - This page allows you create you own Bug

* View Bug Page
    - Displays bug details on one page.
    - Can also upvote on the Bug on this page.

* Post Bug Comment Page
    - Allow a user to add a comment about the Bug.

* Features Page
    - Displays all Features created on one page with all there detials and status.
    - For each feature on the page you can add as many votes as you like to the shopping cart

* Add Feature Page
    - This page allows you create you own Feature

* View Feature Page
    - Displays feature details on one page.

* Post Feature Comment Page
    - Allow a user to add a comment about the Feature.

* Cart Page
    - Allow user to amend shopping cart
    - Allow user to checkout cart for payment

* Payment Details Page
    - Allow user to enter their payment detials.
    - Once payment submitted bring back to Features page with each feature having its upvote details increase were you purchased an upvote.

* Logout
    - This page allows the user to logout and directs user back to the index page

### Features Left to Implement
  - Would like to add pagination.

### Interesting Bugs
  

## Some the tech used includes:
- Base languages used to create website
  -**Python**, **JavaScript**, **HTML**, **CSS**, **JINJA**
- [Cloud9] (https://aws.amazon.com/cloud9/)
    - We use **Cloud9** to build our web pages
- [Bootstrap] (https://getbootstrap.com/docs/3.3/)
    - We use **BootStrap** for a CSS Framework
- [Django] (https://www.djangoproject.com//)
    - We use **Django** for making web services with Python
- [Fontawesome] (https://fontawesome.com/)
    - Using **Fontawesome** to get use of icons
- [GitHub] (https://github.com/)
    - Using **GitHub** a web-based hosting service for version control using Git
- [Heroku] (https://heroku.com/)
    - We use **Heroku** a web-based hosting service.
- [Stripe] (https://stripe.com)
    - We use **Stripe** for recieving on-line payments
- [Coverage] (https://coverage.readthedocs.io/en/v4.5.x/)
    - We use **Coverage** to measure how much of the code has been tested
- [gunicorn] (https://gunicorn.org/)
    - We use **gunicorn** to connect to heroku
- [psycopg2] (https://pypi.org/project/psycopg2/)
    - We use **psycopg2** to allow connection to postgress database
- [django forms bootstrap] (https://django-bootstrap-form.readthedocs.io/en/latest/)
    - We use **django forms bootstrap** for styling forms
- [gmail] (https://www.google.com/intl/en-GB/gmail/about/#/)
    - We use **gmail** used for semd e-mails to reset passworda
- [d3] (https://d3js.org/)
    - We use **D3** as a datebase for storing users and recipes
- [dc.js] (https://dc-js.github.io/dc.js/)
    - We use **DC** for creating reactive charts
- [crossfilter] (https://mlab.com/welcome/)
    - We use **crossfilter** for grouping data together


## Testing
### Manual testing
- All internal links have been checked and work correctly
   - **Home** Brings user to home page
   - **Login** Brings user Login Page
   - **Register** Brings user to Register page
   - **Statistics** Brings user to Statistics page
   - **Reset Passord** Brings user to reset password page page
   - **Email Reset Passord** Brings user to  password reset page
   - **Logout** Logs out user and bring to home page
   - **Profile** Brings user to their profile page
   - **Bugs** Bring user to bugs page
   - **Features** Bring user to Features page
   - **Comments** Bring user to add comment page (Both Bugs and Features)
   - **Views** Bring user to View page(Both Bugs and Features)
   - **Cart** Bring user to Cart Page
   - **Social Media**  All link to home pages of site

- Register Modal
    - If password not the same, error message display.
    - If User name already in Database then error message is displayed
    - if no e-mail provided then an error message is displayed
    - If everything okay user moved home page.

- Login form
    - if Password or user name incorrect, error message displayed
    - Can login with user name or email
    - If everything okay then page directed to home page

- Reset Password
  - Reset password functionality works once correct e-amil is provided

- Profile page
  - name email are displayed at the top of the page
  - All Bugs and features created by the the user’s are display here and order from most likes down.
  - Can access view page for Feature and Bug
      
- Bugs page.
  - All Bugs displayed here correctly in order from most liked down
  - Can acces Bugview page here
      
- Bug view page
  - All Bugs displayed here correctly in order from most liked down
  - Add comment link works
  - Add comment will display error messgage if no Title or Content is left blank
  - Comment will be added if everything is okay
  - Upvote button works okay. Upvotes will ne increaed by one if everything is okay
  - Upvote will display error if you created this bug or already voted for this bug
  
- Add Bug Page.
  - Once Name description are added but will be added
  - Error displayed if no name or descripton

- Features Pagw
  - All Featuress displayed here correctly in order from most liked down.
  - Add comment link works
  - Add comment will display error messgage if no Title or Content is left blank
  - Comment will be added if everything is okay
  - Add button will add votes to shopping cart
  - Quantity must be filled in or will get an error
  
- Add Feature Page.
  - Once Name description are added but will be added
  - Error displayed if no name or descripton

- Cart
  - Cart icon brings you to checkout page
  - Features in shopping cart are displayed okay
  - Amend button amends shopping cart to change specified 
  - Amend value Must be an integer value
  - Total updates when quntity of upvotes is adjusted
  - Checkout Button brings you to payment page
    
- Payment Page
  - for each selected feature for purchase selected each Feature has its detials and quantity displayed correctly for each selcted
  - total purchase price displayed
  - payment form displayed correctly
  - Error message is displayed if required field is not entered
  - Validation done on phone number is provided, expected correct format
  - Invalid card will be declined
  - Expiry date error will diplay if month and year ealier then this month and this year
  - Error message displayed if not correct payment information.
  - if details okay redirected to features page with message confirming payment and the upvotes indicator increased based not the number of vote purchased
  
- Statistics
      - All charts display as expected
      - 
- Logout
      - Works okay, logs user out and redirects to home page with a message.
    
- Site viewed and tested in the following browsers (all work as expected):
  - Google Chrome displays okay
  - Mozilla Firefox    displays okay
  - Opera   displays okay
  - Internet explorer displays okay

### Automatic testing
  - For all apps I created unit tests for Models, forms and views.
  - Break down of coverage per app
    - accounts 85%
    - bugs 94%
    - cart 94%
    - checkout 97%
    - features 98%
    - home 47%
  - For intergration testing I used Travis CI which builds and tests my app everytime I commit changed to GithUB

### Site has been tested on mobile, tablet and laptop devices as well as testing on chrome for the different sizes.

### Home page
  - feature and bug tables display on large screens beside each other and on smaller screens the bugs table displays on top of the features table

### Registration page
  - Same on all screens

### All pages dealing with password reset
  - Same on all screens

### Login page
  - Same on all screens

### Statistics Page
  - on large and medium screens, bar charts desplay two in a row and on smaller screen on op of each other

### Navbar: 
- On medium to large screens the nav-items are display on the left-hand side of the navbar. On Small screens these items are displayed under
  a hamburger icon which when click a side nav opens with a list of the item underneath each other

### Profile page.
- Recipes on large screen are displayed 3 per row
- Recipes on medium screens are displayed 2 per row
- Recipes on small screens are displayed 1 per row

### Bugs page
- Buga on large screen are displayed 3 per row
- Bugs on medium screens are displayed 2 per row
- Bugs on small screens are displayed 1 per row

### Bugs view page
- More screen room giving to content in smaller screens

### Bugs add page
  - Same on all screens

### Features page
- Features on large screen are displayed 3 per row
- Features on medium screens are displayed 2 per row
- Features on small screens are displayed 1 per row

### Features view page
- More screen room giving to content in smaller screens

### Features add page
  - Same on all screens

### Cart page
- Features on large screen are displayed 3 per row
- Features on medium screens are displayed 2 per row
- Features on small screens are displayed 1 per row

### Checkout page
- Features on large screen are displayed 3 per row
- Features on medium screens are displayed 2 per row
- Features on small screens are displayed 1 per row

### Footer 
- Stays the same for all devices


# Deployment
Set web up in Github
This web site is deployed on the Heroku platform.
https://recipe-book-jm.herokuapp.com/
- Set up app in Herouk. Choose name and set  region to Europe
- Set git repository Heroku
  - git init
  - git add .
  - git commit -m "initial deployment"
- Set Requirements file up
  - Sudo pip3 freeze --local>requirment.txt
-Setup Proc file
  -echo web: python app.py > Profile
- finally push to heroku
  - add requirments.txt
  - add Profile
  - git push -u heroku master
  - 
- Set up in GitHub and give name

Then in Heroku under deploy tab you can connect to GitHub using the name you set uo in gitHUb

The database is stored using MLAb

# Credits

### Logo
-	Created using https://secure.logomaker.com/user