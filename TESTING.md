# Testing for Milestone 4 project - Slovak shop 

1. [Testing used](#testing-used)
2. [Manual code testing](#manual-code-testing)
    1. [In browser testing](#in-browser-testing)
    2. [JSLint](#jslint)
    3. [JSHint](#jshint)
    4. [Lighthouse](#lighthouse)
3. [User story testing](#user-testing)
4. [Additional testing](#additional-testing)


## User testing


## Bugs

Bootstrap hates me and continues to not allow me to amend button hover styling. SAD.

### Significant usage of walkthrough code

With my best efforts, I was not able to not apply Size in the product model, despite not needing to use it, so I had to copy over code from the tutorial for bag.html, quantity_input_script.html and views.py on 28th May 2023, 15:28 as the omission of this variable caused many issues. [Commit log](https://github.com/mutkovicova/milestone-4-project/commit/eb505f3e9d87589e0668ea1bfbc325491253f0a0)

I attempted to resolve this over a 4 hour span but due to time constraints, had to abandon the problem.

### Use of important for shop now

the shop now button would not display correctly unless I use !important. 

### Use of noimage.png

I could not figure out why the template couldn't render the noimage.png correctly. It would respond normally when in the products pages and views, however in bag, it would cause an error and due to time constraints, I just uploaded a no image file to the Django admin directly. Will investigate this later if I have time.

### Stripe payments integration

Following the walkthrough, I do believe Stripe updated the documentation and in the future, I will make sure to familiarise myself with their recommended route. For the purposes of this project, I have decided to follow the walkthrough code.

### Deleting an item from database while in basket

A seemingly known bug occurs if a user tries to delete a product from the shop while that product is in the checkout bag. It will trigger a full Django meltdown that says 'No Product found' and refuse to load anything else. 
Should this happen, Go to DevTools -> Applications -> Cookies -> Session.id and delete the session. This will reset the interface and allow you to continue working.