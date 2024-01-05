![Devmark Logo](https://res.cloudinary.com/dulvjkxha/image/upload/v1693680885/Pics/Devmark_Logo1_anpfar.png)

# Devmark -Introduction

DevMark Introduction

DevMark is a blog that is designed for Developers who have no marketing skills. Our posts get developers thinking about how to get their new products out there once they have been created and deployed. This is the base of a project that I would like to expand on with many more posts to help developers when they are at the level of producing a great product. 

View Live:
[Devmark Site](https://devmark-073af775bfae.herokuapp.com/)

## Responsive Layout:
![Responsive Image](https://res.cloudinary.com/dulvjkxha/image/upload/v1693680842/Pics/DMResponsive_mvrlpn.png)

## Methodology:
This project has been approached with an Agile methodology. All steps taken in the in the project were based on User Stories and applying the MVC (Model-View-Controller) framework strategy.  

## UX
I wanted to colours used to be easy on the eye. The theme that has been used incorporates shades of blue, white and grey. The Landing page gives the blog a modern and creative effect. The look and feel is positive, uplifting with minmal text on the landing page. 

![Colour Pallette](https://res.cloudinary.com/dulvjkxha/image/upload/v1704412629/User%20Stories/Colour_Pallete_lq3jjm.png)

## User Stories: 
To help with the development of this project, I created user stories to map out tasks I needed to achieve in order to build the website to a good standard. I further split these user stories into epics in order to take an agile approach to its development.

View a full list of user stories 	[here](https://github.com/BrendanCooney/marketing-for-devs-blog/issues)

Here is a graphical representation of how the user stories were worked on in GitHub's projects section on the Canban board. All user stories were completed. To see a full list of all user stories and tests done for the user stories please see the [TESTING](TESTING.md) File.

![DevMark User Stories](https://res.cloudinary.com/dulvjkxha/image/upload/v1703623172/Pics/UserStoriesImage1_ty7dne.png)

## Technologies Used:

1. Gitpod IDE
2. Python3
3. Github
4. HTML
5. JavaScript
6. CSS
7. PostgreQL
8. Heroku
9. Canva
10. Paint.net
11. Chat GPT
12. Cloudinary
13. Bootstrap
14. Balsamic
15. Summernote



## Gitpod
Gitpod has been my chosen IDE. I nearly went with VSCode however stuck with Gitpod for the Purposes of this project. I have found it works well with Heroku and other applications. It was way faster than CodeAnywhere. 

## Python3
This project and all the recent walk throughs we have done at the code Institute have been created in Python. 

## Github
Github was used for version control 

## HTML
The Template files used in the project that bring the data to the Python Views are written in HTML.

## Javascript
The use of Javascript has been implemented for interactivity and communication to the user via messages pop-ups.

## CSS

Two differnt CSS stylesheets have been used in this project. One coming from the Codestar Blog and the other from a Bootstrap Theme page that has been modified. 

## PostgreSQL
PostgreSQl has been used as the relational databse management system for this application.  

## Heroku
Heroku has been used for hosting the deployed app it is linked to Github.

## Canva
Canva was used to source images and create the logo

## Paint.Net
Paint.Net was used to resize the blog images to keep them unifom

## Chat Gpt 
Chat GPT was used to create the actual Blog content. The reason for this is that I would like to show my fellow students that creating marketing content that can be a good base for posts is something Chat GPT and similar products can help with. 

## Cloudinary
Cloudinary was used to host the images and static files of the project linking up the images and stylesheets.
![Cloudinary](https://res.cloudinary.com/dulvjkxha/image/upload/v1704235941/Testing%20Images/Cloudinary_Screenshot_adbzlg.png) 

## Bootsrap
Using Bootstrap has been an fundamental part of the entire website application. The Landing Page was taken from Start Bootstrap and was adatpted and changed with images from Canva to suit the project. 

## Django
This entire project was build with Python and Django and integrating them with HTML, CSS and Javascript. 
Building with Django has been a great experiece. As I have come to the end of the project I realise just how powerful Django is.
The Admin Panel and apps make it quick and easy for users once it has been deployed corectly. 

## Summernote
Summernote was installed to allow the Django Admin Dashboard to use a WYSIWYG Editor for posts. 

## Wireframes
These wireframes were created in Balsamic. 

Below is the Landing page view where the user first enters the site:

![Landing Page](https://res.cloudinary.com/dulvjkxha/image/upload/v1693730371/Pics/Wireframes/Landing_Page_Wireframe_klfbny.png)

This is a view of the posts page wireframe if you click on the blog link:

![Posts Page](https://res.cloudinary.com/dulvjkxha/image/upload/v1693730370/Pics/Wireframes/Posts_Page_c1hugq.png)

This is a view of the Blog Post Wireframe if someone is reading a post:

![Article Page](https://res.cloudinary.com/dulvjkxha/image/upload/v1693730370/Pics/Wireframes/Blog_Post_View_juhkmg.png)

This is a view if the project Layout as I understand it:
![Project Layout](https://res.cloudinary.com/dulvjkxha/image/upload/v1693737436/Pics/Wireframes/Project_Layout_aqqstq.png)

## Models
In this project there are three apps, each have their own different models. 
The Blog app models come from the Codestar Blog project and don't have muc deviation. The About app model was created by following an extra seminar suggested by the Code Institite. The third app is the Tools app. I wanted to highlight some decent marketing and sales tools for developers to use and provide a rating for them. At this stage of development. Only admins can rate the software being used. 
With further development all users could add to the rating. Below are images of how the models are represented. 

Blog App: Project Model

![Blog Model](https://res.cloudinary.com/dulvjkxha/image/upload/v1704395887/Models/Blog_Model_Devmark_ydlas6.jpg)

About App: Custom Model

![About Model](https://res.cloudinary.com/dulvjkxha/image/upload/v1704395887/Models/Devmark_About_Model_saayqz.jpg)

Tools App: Custom Model

![Tools Model](https://res.cloudinary.com/dulvjkxha/image/upload/v1704395887/Models/Tools_App_Models_oogrkh.jpg)

### Testing
All testing througout the project has been done on a manual testing basis using a MVC framework. From Html, CSS, Javascript, Python3 and Django all work to produce the result has used manual testing. please refer to the [TESTING](TESTING.md) file for more information on the testing processes used.

### Deployment 
The Development plan of this project was to install all the required libraries and deploy to Heroku early. Using this strategy the aim would be leave less room for error with a larger smaller project rather than a larger project at the end. 

### ElephantSQL Database
This project uses ElephantSQL for the PostgreSQL Database.

To obtain your own Postgres Database, sign-up with your GitHub account, then follow these steps:

- Click Create New Instance to start a new database.
- Provide a name (this is commonly the name of the project: retro-reboot).
- Select the Tiny Turtle (Free) plan.
- You can leave the Tags blank.
- Select the Region and Data Center closest to you.
- Once created, click on the new database name, where you can view the database URL and Password.

### Cloudinary Static File hosting
The static Files of the project are hosted in Cloudinary. In order to do this cloudinary had to be installed and a cloudinary account had to be opened. 

### Heroku Deployment
This project uses Heroku, a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:
- Select New in the top-right corner of your Heroku Dashboard, and select Create new app from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select Create App.
- From the new app Settings, click Reveal Config Vars, and set your environment variables.

### References 
This Blog project used the Codestar Project by the code institute as a base. I wanted to change the content and the way the website was repersented so the landing page was added. The Landing page used a template from Start Bootstrap. Canva was used for the images and as an example Chat GPT to quickly produce the articles which were slightly ammended by myself.

Creating the Tools and Rating model relied on the guidelines of this Blog Post:
https://medium.com/geekculture/django-implementing-star-rating-e1deff03bb1c


Thank you to the Code Institute for the opportinty 


