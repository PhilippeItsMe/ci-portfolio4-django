![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Passeport Chats & Chiens

<a style="text-decoration:underline;" target="_blank" href="https://ci-portfolio4-django-86a85546f387.herokuapp.com/">Passeport Chats & Chiens LIVE link</a><br>
<a style="text-decoration:underline;" target="_blank" href="https://github.com/PhilippeItsMe/ci-portfolio4-django.git">Passeport Chats & Chiens GITHUB link</a>

## Project

Imagine a world where caring for your beloved pet becomes easier, more affordable, and oh-so-rewarding! Our platform is here to connect passionate pet owners with trusted businesses that cater to every furry, feathery, or scaly need. For just a small annual fee, you'll unlock exclusive perks: enjoy a fabulous 50% discount on your first purchase and a delightful CHF 20 off on your second visit—per business. Because your pet deserves the very best, and so do you! 

## Key features

<table border="1" cellpadding="10" cellspacing="0">
    <thead>
        <tr>
            <th>Feature</th>
            <th>Project 4</th>
            <th>Project 5</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><b>User Features</b></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Account Creation & Management</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Subscription System</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Pet Profile Management</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Business Directory</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Exclusive Discounts</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td><b>Business Features</b></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Business Account Management</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Discount Management</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Ratings & Reviews</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td><b>Core Website Features</b></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Homepage</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Search Engine</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>User Authentication</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Secure Payment Gateway</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Automated Notifications</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td><b>Marketing Features</b></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Blog/Content Section</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Social Media Integration</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Referral Program</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td><b>Administrative Features</b></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>Admin Dashboard</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Discount Management</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Customer Support</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
        <tr>
            <td>Data Analytics</td>
            <td>✔</td>
            <td>✔</td>
        </tr>
    </tbody>
</table>




## Planning

### Project 4
Week 




## Data Models



## API Endpoints





## Frameworks & Libraries




## Debugging, testing & deployement

### Debugging

Bug 1 
Issue : My page rendering pet businesses wasn't rending anything.
Solution : Adding <context_object_name = "pet_business_list"> in my views.py to be able to pass it my template pet_business_list.html.

Bug 2 
Issue : Impossible to pass the pet_business attribute to the pet_business-detail.html.
Solution : Adding post object to his view {"pet_business_detail": post}.

Bug 3 
Issue : Impossible to edit or delete comments.
Solution : Fine tuning the views with introducing the wright source model and destination template pet_business_detail.

Bug 4
Issue : Had to change my class names from snake_case to CamelCase. While migrating the change, 4 dB where inversed and a inbetween dB in manytomany relationship erased.
Solution : Create a brand new dB.

Bug 5
Issue : Issue rendering My Pet Businesses in the menu to pet owners users only.
Solution : Insert the conditional li inside the {% if user.is_authenticated %} tag.

Bug 6
Issue : Data from a many2many relationship where not saved in the dB.
Solution : Adding form.save_m2m() in the pet_business view.

### Testing




### Deployement













