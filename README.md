![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Passeport Chats & Chiens

<a style="text-decoration:underline;" target="_blank" href="https://ci-portfolio4-django-86a85546f387.herokuapp.com/">Passeport Chats & Chiens LIVE link</a><br>
<a style="text-decoration:underline;" target="_blank" href="https://github.com/PhilippeItsMe/ci-portfolio4-django.git">Passeport Chats & Chiens GITHUB link</a>

## Project

Imagine a world where caring for your beloved pet becomes easier, more affordable, and oh-so-rewarding! Our platform is here to connect passionate pet owners with trusted businesses that cater to every furry, feathery, or scaly need. For just a small annual fee, you'll unlock exclusive perks: enjoy a fabulous 50% discount on your first purchase and a delightful CHF 20 off on your second visit—per business. Because your pet deserves the very best, and so do you! 

## Key features

The following table outlines the features included in this project. Their deployment is divided between Project 4 and Project 5, with Project 4 serving as a Minimum Viable Product (MVP) and Project 5 encompassing the full-scale implementation.

  <table border="1" cellpadding="10" cellspacing="0">
    <thead style="background-color:white; color:black">
        <tr style="background-color:RGB(249, 249, 249, 0.1)">
            <th style="width:60%"> <strong>Features</strong></th>
            <th style="width:20%; text-align:center;"><strong>Project 4 (MVP)</strong></th>
            <th style="width:20%; text-align:center;"><strong>Project 5</strong></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="3" style="background-color:RGB(249, 249, 249, 0.1)"><strong>Business Owners Features</strong></td>
        </tr>
        <tr>
            <td colspan="3"><strong>Account management</strong></td>
        </tr>
        <tr>
            <td>Account creation with username & password</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;"></td>
        </tr>
        <tr>
            <td>Account creation with social login</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Account creation with email confirmation</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Login with username & password</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;"></td>
        </tr>
        <tr>
            <td>Username & password recovery</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Social login</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td colspan="3"><strong>Pet Business Management</strong></td>
        </tr>
        <tr>
            <td>Create a new business</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;"></td>
        </tr>
        <tr>
            <td>Edit, update, or delete a business</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;"></td>
        </tr>
        <tr>
            <td>Business statistics (views)</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td colspan="3"><strong>Comments Management</strong></td>
        </tr>
        <tr>
            <td>Respond to pet owners comments</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td colspan="3" style="background-color:RGB(249, 249, 249, 0.1)"><strong>Pet Owners Features</strong></td>
        </tr>
        <tr>
            <td colspan="3"><strong>Account management</strong></td>
        </tr>
        <tr>
            <td>Account creation with username & password</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;"></td>
        </tr>
        <tr>
            <td>Account creation with social login</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Account creation with email confirmation</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Login with username & password</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;"></td>
        </tr>
        <tr>
            <td>Username & password recovery</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Social login</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td colspan="3"><strong>Owned Pet Management</strong></td>
        </tr>
        <tr>
            <td>Create a new pet profile</td>
            <td style="text-align:center;"></td>
            <td style="text-align:center;">✔</td>
        </tr>
        <tr>
            <td>Edit, update, or delete a pet profile</td>
            <td style="text-align:center;">✔</td>
            <td style="text-align:center;">✔</td>
        </tr>
        <!-- Continue for the remaining rows in the same format -->
    </tbody>
</table>


## Planning

The project 4 development was completed over four weeks, following the schedule outlined below:

Weeks 2 & 3: Back-end development<br>
Week 4: Front-end development<br>
Week 5: Fine-tuning and README documentation<br>


## Data Models

The project's data model is structured as follows: it revolves around <span style="color:blue;">pet businesses</span>, <span style="color:green;">pet owners</span> (in green), and <span style="color:orange;">comments and likes</span> (in red). The sales-related section of the data model will be added after completing the corresponding lesson (LMS).


<img src="static/readme/datamodel.webp">

## API Endpoints





## Frameworks & Libraries




## Debugging, Testing & Deployement

### Debugging

<strong>Bug 1</strong><br>
Issue : My page rendering pet businesses wasn't rending anything.<br>
Solution : Adding <context_object_name = "pet_business_list"> in my views.py to be able to pass it my template pet_business_list.html.<br>
<br>
<strong>Bug 2</strong><br>
Issue : Impossible to pass the pet_business attribute to the pet_business-detail.html.<br>
Solution : Adding post object to his view {"pet_business_detail": post}.<br>
<br>
<strong>Bug 3</strong><br>
Issue : Impossible to edit or delete comments.<br>
Solution : Fine tuning the views with introducing the wright source model and destination template pet_business_detail.<br>
<br>
<strong>Bug 4</strong><br>
Issue : Had to change my class names from snake_case to CamelCase. While migrating the change, 4 dB where inversed and a inbetween dB in manytomany relationship erased.<br>
Solution : Create a brand new dB.<br>
<br>
<strong>Bug 5</strong><br>
Issue : Issue rendering My Pet Businesses in the menu to pet owners users only.<br>
Solution : Insert the conditional li inside the {% if user.is_authenticated %} tag.<br>
<br>
<strong>Bug 6</strong><br>
Issue : Data from a many2many relationship where not saved in the dB.<br>
Solution : Adding form.save_m2m() in the pet_business view.<br>

### Testing




### Deployement













