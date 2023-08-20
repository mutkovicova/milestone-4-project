# Milestone 4 project - Slovak shop

[Live site on Heroku](https://slovak-shop-milestone-4.herokuapp.com/)

## Purpose

The purpose of this project is to create a marketplace for Slovak products to be sold to residents in the UK.  

![Am I Responsive screenshot of website on many sizes](/media/testing/amiresponsive-slovakshop-screenshot.png)

## Table of contents

1. [Users](#users)
2. [Design](#design)
3. [Wireframes](#wireframes)
4. [Features](#features)
5. [Data model](#data-model)
6. [Technologies used](#technologies-used)
7. [Testing](#testing)
8. [Future developments](#future-developments)
9. [Deployment](#deployment)
10. [Acknowledgments](#acknowledgments)
11. [Thank you](#thank-you)

## Users

1. Returning user
    1. Retain my details for future checkout
        The user is able to both re-use previous data they have used if registered on the site. A future development could be the use of multiple addresses - billing and delivery.
    2. Have an order history
        The order history is clear. The user has an easy way to navigate to past orders and review them.
    3. Ability to update my details
        The user is able to edit their profile and the information the store hold on them - including deleting useless information.

In general, as a returning user, it would be useful to implement more features that would keep people on the site - such as wishlist function, in stock alerts, etc.

2. New user
    1. Find items easily
        The products are clearly categorised and are sortable. In the future, a "if you like this product, you may be interested in this" would be a good addition.
    2. Add items to cart
        A user is prompted to add items to cart and is able to do so with the fewest clicks possible.
    3. Pay seamlessly
        The payment process is incredibly simple to understand, is secure, and a user feels no hesitation to pay.
    4. Receive news of new products
        A user can sign up to a newsletter that will keep them up to date on new items on the store. In the future, this would include alerts for out-of-stock items and the ability to vote on products that should be restocked.

3. Administrator
    1. Add products
        An administrator can easily add new items to the store.
    2. Edit products
        If needed, an administrator, while logged into the site, can visually edit the details of the product.
    3. Delete products 
        If necessary, an administrator can delete a product. This is verified by the system to prevent accidental deletion.

## Design

I designed the site to use fairly neutral colours (with a blue pop of colour) to emulate the more country living feeling that Slovak food evokes in me. The colour scheme can be seen below with hex codes:

![shop colour scheme](/media/readme/colour-palette.png)

The font used is Lexend, as it is a dyslexia friendly font, which means a wider audience can find it easier to navigate the site. The font was sourced from [Google Fonts](https://fonts.google.com/specimen/Lexend?query=lexend).

The tone of the entire website is more fun and playful than a regular store ("Uh-oh, something went wrong!" rather than "Error occured" etc). This was with a back story in mind of this being a more local shop that really values its customers and breaks away from the norm.

### Wireframes

Using the design elements, I combined them to keep the site incredibly simple and easy to view for most visitors.

![shop wireframe design desktop](/media/readme/website-wireframe.jpg)

![shop wireframe design mobile](/media/readme/website-mobile-wireframe.jpg)

The end design is a much more scaled down version with a few elements missing, but I think it delivers the same clean look in the end.

## Features

### Products

The site features products from various categories that would be found on other shops such as this one. The products are clearly marked with these categories and have an easy view of the price. When viewed, the product detail offers the option to add the product to a bag and produces a lovely little notification to respond to a users action.

### Shopping

The checkout bag features a list of products, as well as the option to increase/decrease quantities. The checkout page then has a simple form for users to fill in, the option to save information for future purchases and an easy pay interface.  

### Accounts

Logged in users can edit their details and these details will automatically pull into the order form when checking out. They can also use the checkout process to override the details they have saved in their profile.

### FAQs

The FAQs on this site are simple and can be answered by a logged in user. In the backend, these answers can be deleted and replaced by administrators however in the short term, are useful as a way to ensure answers quickly.

### Contact Form

If a user does not find an answer to their question in the FAQs, they have the option to ask a custom question directly to the administrators' email.

### Admin

Administrators have the ability to upload new products, edit existing products or delete them off the site. All this is done via clean interfaces within the website itself and don't require lengthy visits to the admin portal.

## Data model

![data model](/media/readme/data-model.png)

## Technologies used

### [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)

HTML5 was used for basic structure of the landing pages.

### [CSS3](https://en.wikipedia.org/wiki/CSS#CSS_3)

CSS3 was used minimally to fix issues with formatting in certain areas.

### [Python](https://www.python.org/)

Python was used in conjunction with Django to create the back end.

### [Am I Responsive?](https://ui.dev/amiresponsive?url=https://project-3-wishlist.herokuapp.com/)

Am I Responsive? was used to create the screenshot for the finished project.

### [Font Awesome 5.15.4](https://fontawesome.com/)

Font Awesome was used to add a little bit of interest to the form, as well as the buttons, across the site.

### [Bootstrap](https://getbootstrap.com/docs/4.0/getting-started/introduction/)

Bootstrap was used for all the styling.

### [Django](https://www.djangoproject.com/)

Django was used for all its apps and e-commerce functionality.

### [Google Fonts](https://fonts.google.com/)

Google Fonts was used to implement a custom font for the whole project for better accessibility.

## Testing

Full testing is detailed in the [Testing markdown file](/TESTING.md).

## Future developments

This project could benefit from a good thorough re-write due to some outdated technologies within the CI walkthrough.
However, some specific areas that really would make this site wonderful are:

### Expanding product management page

I'd like to make the product management page more than just an add product site. I'd like it to also have a lookup of products for editing and deleting, and option to add product at the bottom.

### Footer

A footer that could provide a secondary navigation across the site and link to areas such as Privacy Policy etc would be essential to a live site.

### Receive news of new products

I would love an ability which would notify users if a favourite product of theirs came back in stock, or would automatically scrape their previous views and notify them of new stock.

## Deployment

### Heroku

1. Generate requirements.txt file using:  
pip freeze --local > requirements.txt

2. install gunicorn with pip3 install gunicorn

3. Create a new file with the name Procfile and the content of  
web: gunicorn slovak_shop.wsgi:application
  
4. Change Development to FALSE and Debug to FALSE within settings.py
  
5. (if applicable) Navigate to Heroku and create account
    - Click on New and go to Create New App in top right
6. Choose a unique name and choose the Europe region
7. Go to Reveal Config Vars
    1. Navigate back to ElephantSQL and copy the Database URL in your created instance
    2. In Config Vars, add a new one with DATABASE_URL as key and the URL from ElephantSQL as value
    3. Use all other values from settings.py, including your secret key, stripe keys, AWS key and any other values you may need.
8. Navigate back to the app interface and click on Open App in the top right

All done!

### [ElephantSQL]

1. Create account with ElephantSQL
2. Link GitHub repositories with ElephantSQL
3. Create new instance and name it similarly
4. Choose region close to you (I chose Ireland EU West)
5. All done!

### [AWS](https://aws.amazon.com/)

1. Create an account
2. Once you're through creating all the necessary credentials, navigate to search bar/Browse button.
3. Search/find S3
4. Click on Create Bucket
5. Name your bucket similar to the project name
6. Any option that gives public access to the repository, tick it
7. When necessary to create policy, select S3 and paste in the heroku URL to "Response" (I may remember that part wrong!)
8. Once created, navigate to User Groups on the left
9. Create a group with admin rights, applying the policy from the bucket and name appropriately
10. Once group is created, add any users you want to have access to the site (mainly yourself)
11. Create folders in bucket for static/ and media/
12. Navigate to the bucket landing page and find the key
13. Reveal and copy over to Heroku's Config Vars.

All done!

## Acknowledgments

This project is a very close replica of the Boutique Ado project from Code Institute. While I have put my stamp on design, interaction and extension choices, I have followed the main logic of e-commerce site from the walkthrough.

## Thank you

Rachel from EKC Group - thank you for your unwavering support of my many times in giving up and for providing us with a supportive environment to complete our project.

Ariela - Without you, I literally would never have completed this course. Thank you so much for supporting me, making me feel smarter than I am, and helping me to see a potential career.

Alex - I know there are many days where I abandoned you in favour of coding. Thank you for being supportive and reminding me every day that I am doing this to give us all a better life, not just me.

James - For coming into my life and giving me that lightbulb moment that made me think about pursuing that thing I've always wanted to do. You may have made life 10x harder, but you've also made it much clearer.
