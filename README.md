<h1 align="center">click a book</h1>
<div align-itmes="center">
<h2 align="center">
    <a  href=""  target="_blank"><img  src="/documentation/gifs-view/desktop.png"  alt="click-a-book desktop screen"/></a>
<br>
    <a  href=""  target="_blank"><img  src="/documentation/gifs-view/mobile.gif" alt="click-a-book mobile Screen"/></a>
</h2>
</div>
<h2 align="center">click a book</h2>


**click a book**  is a website of for a fictional book club set up by the founders of the book club. 

***

This project is created for the Practical Python and Data-Centric Development module at the **Full Stack Software Development Course** with **Code Institute**.

**The brief** 

_Project purpose_: In this project, you'll build a full-stack site that allows your users to manage a common dataset about a particular domain.

_Main Technologies Required_: HTML, CSS, JavaScript, Python, Flask, MongoDB.

_Optional_: Additional libraries and external APIs.

_Value provided_:

1. Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members.

2. The site owner advances their own goals by providing this functionality, potentially by being a regular user themselves. The site owner might also benefit from the collection of the dataset as a whole.

   

   

***

This web app will use **CRUD** operations so the users can create, read, update and delete data from the database (MongoDB) and is hosted on Heroku.com.

**THE IDEA**

_click a book_ is a web app of a book club set up by the founders of the book club. They post suggestions of books for the next meetup and members can log in and pick the book they are interested in reading for the next meetup.

 I have chose this theme for the website because I like reading books and I think I can understand better how a user will navigate the site and what are their expectations when they open the website. 

### The need:

The book club founder wants to have a platform where the book club members can see her book suggestions for the next meetup. This way they can pick their favourite and they can comment on it why they would like to read that book.

### The goals of this website are:

* The books  on the website are posted by the book club founder through the MongoDB Database and fetched on the website.
* Provide a choice of books to the book club members, so they can pick which book they would like to read for their next book club meetup.
* Only registered  members can see the comments posted by other users or post their comments  on the site.
* Provide a clean feel and easy to navigate website, on all screen sizes.

***

###  UX

Common characteristics of a user:

* Avid reader who likes discovering new books, sharing their reading list and review books.
* Book club member or someone who is interested in joining the book club.

#### Design and colours

##### Fonts

For logo I have used two fonts: _Merryweather_ and _Old Standard_ to emphasise the word _book_.

I have used two fonts, _Open Sans_ for general text displayed on the site. It's easy to read and looks good on all devices. Where I need to put more emphasis on a piece of text, I have used Libre Baskerville. Because is a books/reading related website, I think it fits well with the theme.

##### Colour Scheme

I wanted the user to get a sense of calmness and warmth when they open the website. To invite them to think about the feel and look of the books they have read or they will like to read. 
I have used the website [Coolors.co](https://coolors.co/) to create the colour scheme. I have used #e3c6b9 ![#e3c6b9](https://placehold.it/15/e3c6b9/000000?text=+) , #F6FEDB ![#F6FEDB](https://placehold.it/15/F6FEDB/000000?text=+) , #f4f4f4![#f4f4f4](https://placehold.it/15/f4f4f4/000000?text=+) as main colours. 

These colours bring a sense of calmness and cleanness for the reader to put them in a peaceful  state when they read through the website.

#### Design wireframes / mock-ups:

At the beginning of the  project, the idea was a bit more complex, but I downsized it, so I can meet the submission deadline. 

Click on the below links to see the wireframes or you can view them in the  [wireframes](/documentation/wireframes) folder. These were create with [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjwj975BRBUEiwA4whRB9TM6Ift0fUSy8zuYxc6kubGo-Z-_NgB56zcqoXHBgj6VbkIfGjz9RoCfaEQAvD_BwE).

#### Wireframes

* **[Desktop view](/documentation/wireframes/desktop)**
* **[Mobile view](/documentation/wireframes/mobile)**


#### Users stories:

* As a _general user_ I would like to get a clean and calm feel of the website when I open it.

* As a _general user_, I want to be able to create an account with password protected.

* As a _general user_, I want to be able to read synopsis of the books the book club founder posted on the website.

* *As a registered user*, I want to navigate my way easy on the website, to browse around through the content.

* As a _registered user_ I would like to be able to log in and log out from my account to keep it secure and private.

* As a _registered user_ I would like to be able to delete my account at any point.

* As a _registered user_ I would like to be able to comment on books.

* As a _registered user_ I would like to be able delete comments I've posted.

* As a _registered user_ I would like to be able update any comments I've posted.

* As a _registered user_ I would like to be able delete any comments I've posted.

  

***

### Database Design

<h2 align="center">
    <a href="" target="_blank"><img src="/documentation/DBSchema.PNG" alt="click-a-book db-schema"/></a>  
</h2>



_______________________________________



### FEATURES

#### Functionalities

On this web app, the users can do the following actions, depending if they registered or not:

- read the content 
- create account
- log in on the site
- comment on a book
- delete their comment
- update their comment
- delete their profile

#### EXISTING FEATURES

**Logo** 

I have created the logo for _click a book_ web app with [Canva](https://www.canva.com/). 

**Navbar**

The navbar has 3 links:

- when the user is not logged in: Home | Register | Login

- when the user is logged in: Home | Profile | Logout

  

**Hero Image** - The image shows at the top of the screen under the navbar on each page.

**Forms** for registration and for logging in.

**Modal** for deletion confirmation. When the user wants to delete their profile or a comment, there is a modal with the option for cancelation or confirmation of deletion.

**Buttons** used by the user to interact with the content on the page.

**Flash messages** appear at the top of the screen to notify the user when they perform certain actions: login, logout, add/delete/update messages.




#### FEATURES left to implement

- **Admin Panel** for the book club founder, so he can have control over the data through the site itself, not only though database.
- **Like an Unlike buttons** for each book, so users can vote for their favourite book.
- **Forms** for users to submit book suggestions.
- **Search area** to look for books by title or author
- **Filter option** to filter books by genre or alphabetical order
- When the users deletes their profile, their comments to be deleted as well.





### Technologies Used

I have created this website with the help of a multiple technologies:

* [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) to creating the main structure of my pages.
* [CSS](https://www.w3.org/Style/CSS/Overview.en.html) for styling my components and layout on the page.
* [Balsamiq](https://balsamiq.com/wireframes/?gclid=CjwKCAjwj975BRBUEiwA4whRB9TM6Ift0fUSy8zuYxc6kubGo-Z-_NgB56zcqoXHBgj6VbkIfGjz9RoCfaEQAvD_BwE) for designing the wireframes
* [Python](https://www.python.org/) for the back-end development.
* [PyMongo](https://api.mongodb.com/python/current/) as the Python API for MongoDB to bring the data from the database to the web app.
* [Flask](https://flask.palletsprojects.com/en/1.0.x/) is a Python microframework.
* [Jinja](https://jinja.palletsprojects.com/en/2.10.x/) for templating with Flask and HTML. It simplifies the code to avoid repetition and links data from MongoDB.
* [MongoDB](https://cloud.mongodb.com/) as a database to keep all the records. 
* [Visual Studio Code](https://code.visualstudio.com/) and [Gitpod](https://gitpod.com) was used as IDE.
* [JavaScript](https://www.javascript.com/) for adding interactivity on the page.
* [jQuery](https://jquery.com/) for JavaScript functionality and Materialize.
* [git](https://git-scm.com/) for saving my code in Github.
* [Bootstrap](https://getbootstrap.com/) as a framework to make the web app responsive.
* [Google Fonts](https://fonts.google.com/) for linking fonts.
* [GitHub Desktop](https://desktop.github.com/) for pushing code from Visual Studio code from my pc to Github.
* [Heroku](https://www.heroku.com/) for hosting and deploying the web app.

***

### TESTING

[Esprima: Syntax Validator](https://esprima.org/demo/validate.html) was used to check scripts.js file for any syntax errors. All code is valid and does not contain any syntax errors.

W3C was used to validate the HTML and CSS code. All code is valid.

I have regularly checked my app.py file to make sure the code is indented properly and it has the correct syntax with the help of PEP8.

I have used Responsinator to see how the site looks like on different screens. Please see here [Responsinator](http://www.responsinator.com/?url=https%3A%2F%2Fclick-a-book.herokuapp.com%2F).

I wanted to check how the page looks on different browsers for Windows and iOS, so I have used [crossbrowsertesting.com](https://app.crossbrowsertesting.com/test-center). I have only been able to take screenshots of what test I have performed, because you need to buy a licence to be able to download the results. Please see below the types of test I have performed.

#### Manual Testing

I have performed various tests on what actions the user might take on the site and the results can be found in this table.


----------------
----------------

***

#### Deployment

At the beginning I have started the development on my machine with Visual Studio code and I was saving  regularly the code in a repository I have created on GitHub. When I have connected my MongoDB to my app, I have started using Gitpod online IDE.

To make sure the data is linked and displayed correctly I have created an account on Heroku and deployed my web app live. This helped me with the debugging part as well.

### Running the project locally

To run this web app locally on your machine you need to have these technologies in place:

- [Python3](https://www.python.org/downloads/) to run the app.py files and the application
- [PIP](https://pip.pypa.io/en/stable/)
- An IDE - Visual Studio Code or online Gitpod
- [git](https://www.atlassian.com/git/tutorials/install-git)
- [MongoDB](https://www.mongodb.com/) 

To save my code on your machine, you have to follow the below steps:

**Clone the project on your machine**

Go to [click-a-book](https://github.com/andreeaiosip/click-a-book#click-a-bookhttpclick-a-bookherokuappcom)

Click on green button on the right with 'code' and  an arrow on it

*Option 1*

- Copy the clone URL for the repository in the 'Clone with HTTPs section'.

- Open your git bash

- Choose the folder you want to clone the project in.

- Type `git clone`, then paste the URL you copied in Step 3:

  `git clone https://github.com/andreeaiosip/click-a-book`

- Press `Enter` to save the cloned project

  

*Option 2*

  Save the files as a zip and unzip it in a folder of your choice.



**Create a database in MongoDB**

1. Go to [MongoDB](https://www.mongodb.com/) and create an account
2. Create a new Database (called _books_) in MongoDB - Here's a useful [video tutorial](https://www.youtube.com/watch?v=rE_bJl2GAY8) if you don't know how to use MongoDB 
3. Create collections for _users_, _bookInfo_ and _comments_ - please follow the format as in my database schema:

**Link local project with MongoDB**

1. Go to your IDE  and add your MongoDB URI in the following format:

   - MONGO_URI: `mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority`
   - SERCET_KEY: `<your_value>`

2. In the terminal, run the `pip3 install -r requirements.txt` command to install the requirements.txt file.

3. You will be able to run the app locally using the `python3 run.py` command.

   

### Live Deployment on Heroku

The project from GitHub is deployed and set live on Heroku. To deploy this project to Heroku I followed the  steps below and I have watched this [tutorial](https://www.youtube.com/watch?v=GgNcs9zlFSA).

1. Sign up for Heroku and sign in to create a new app
2. Click the "New" button to create a new app
3. Give a name to the app and specify the region
4. Generate a requirement.txt file to inform Heroku of what dependencies are needed to run the app. In the terminal `pip3 freeze --local > requirements.txt`
5. You need to create a Procfile file type to inform Heroku what type of app is being deployed `echo web: python run.py > Procfile`
6. At the deployment tab of the app in Heroku click the Heroku git method for deployment.
7. In the terminal of you IDE type the commands:

```
$ heroku login
$ heroku git:remote -a <click-a-book>
$ git push heroku master
```

1. In the Heroku settings tab, click on the "Real Config Vars" button to set environmental variables:

- IP: `0.0.0.0`
- PORT: `5000`
- MONGO_URI: `mongodb+srv://<username>:<password>@<cluster_name>.mongodb.net/<database>?retryWrites=true&w=majority`
- SERCET_KEY: `<your_value>`

On the dashboard click on "Open App" button to view your deployed Heroku app.


***

## Credits

Books title and synopsis were taken off Amazon.com.

Navbar gradient was created with the help of gradient css generator on [cssgradient.io](https://cssgradient.io/)

Registration and login functionalities  were implemented with the help of tutor [Tim Nelson](https://github.com/TravelTimN) from Code Institute and my colleague [Antonela Mrkalj](https://github.com/antonelam) helped me with the implementation of CRUD.

Hero image was taken of Google images (no copyrights).

##### Acknowledgement

Thank you to all my colleagues from Code Institute who took the time to answer my questions and review my project. Thank you to Tim Nelson! He made me believe I can do this project and finish on time.  Thank you to Antonela Mrkalj. She reinforced what Tim did - she made me believe in myself even more.

Thank you to [Alan McGee](https://github.com/alimgee) who gave me the first pointers on how to start this project by giving me advice from his experience when he built a similar project [BookBites](https://github.com/alimgee/book-review-milestone-project3).

Thank you to my mentor [Simen Daehlin](https://github.com/Eventyret) who helped me with shaping my idea for this project and being patient with the submission of this project.


#### Disclaimer

The content of this Website is for educational purposes only.