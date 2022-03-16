# Project Four Ondeed README #



**Contents** 

* Project Overview
* Brief
* Timeframe
* Deploy Link
* Technologies Used
* Planning
* Build
* Bugs
* Challenges
* Wins & Learning
* Areas For Future Development

## Project Overview ##

In the final project for General Assembly, we had to build a full-stack application in groups or solo. I decided to do it myself as I wanted to see what areas I need to work on and hadn’t done much of the back end in my previous project. I decided to make a clone of Indeed and use Python and Django to create the back end and JavaScript, React and SCSS in the front end. I had one week to complete this. 

## Project Brief 

Build a full-stack application by making your backend and your front-end.
Use a Python Django API using Django REST Framework to serve your data from a Postgres database.
Consume your API with a separate front-end built with React.
Be a complete product with multiple relations.

## Time Frame

7 Days

## Deployment

Link [**here**](https://61fd12d8752321a20399a3d4--ondeed.netlify.app/)

## Planning

For this project, my plan was to create an Indeed clone but it's a website for software developers to find their jobs. I want companies to be able to post jobs onto the website, and the users the ability to contact the companies if they’re interested in applying for that position. Using an ERD diagram I mapped out the relationships in the back end. I used Excalidraw to note some of the features and styles Indeed currently uses, and how I will replicate that for my solo project. 

MVP requirements:

* Homepage.
* Index All Jobs (On Homepage like Indeed).
* Show page (display all information about a single job).
* Filter/search jobs.
* User-created account.
* Companies can upload jobs.
* Sign in / Sign Out.
* Styling is similar to Indeed.

The Stretch Goal ideas: 

* Users can favourite jobs.
* Email verification.
* Contact email sent to companies.

<img src="https://i.imgur.com/gHFmUF3.png" width="700" height="600" />

<img src="https://i.imgur.com/93g8VwI.png" width="700" height="400" />

## Technologies Used

* SASS
* HTML
* JavaScript
* React
* Axios
* Django
* Django Rest framework
* Python
* Git
* GitHub


## The Build Back End

#### Models

Getting the models right is difficult, this was the first time using Python and Django. Much of it was very different to using Node.js in the previous project. I started off by creating the Job model as this is the primary source of information on the website and it governs how the website is laid out. 

To test if my field options were appropriate, I compared current jobs in tech that existed on Indeed and compared that to whether the field requirements match. “CharField” (character fields) were all straightforward, I just needed to check I had given enough room in max length to fix the information. Having the salary as a “PositiveIntergerField” is important so that the users don’t put negative numbers in which could cause errors when sorting by salary.

To ensure that the Applications match the Job listing, I used a field called “ForeignKey” which created a relationship between the Application and the Job model as seen below. The Application model also uses a “ForeignKey” for the owner. 

<img src="https://i.imgur.com/bvurs4p.png" width="600" height="800" />

#### Authentication

In the next step, I created an authentication class that checks whether the request has a JWT token. If the Header doesn’t match the user will receive Permission Denied, if the token is invalid they will receive an Invalid Token Error. This is tested in Insomnia. 

<img src="https://i.imgur.com/5bWWkVJ.png" width="600" height="600" />

## The Build Front End



#### API

This is the API page where the get requests were refactored too. “getAllJobs” is used on the homepage to access the jobs listing, similarly, “getSingleJob” is used for an individual page for each job. The main difference between these requests is the URL, the “getSingleJob” uses the character “/id” the URL whereas “getAllJobs” uses “/all”. This was all written in the RESTful API documentation.

<img src="https://i.imgur.com/HjzHbmf.png" width="600" height="600" />

#### Home Page

The homepage for this project is very important, when on indeed website they pull a lot of the information onto the home page including indexing all the job listings. I created JobCard’s so that when the information is pulled onto the homepage it arrives in a neat format that was easier to style. Also by formatting them into JobCards, it makes the busy Home.js page a bit more readable. Having the class name of “home-page” allows me to use .home–page in SASS and add styling. 

<img src="https://i.imgur.com/GXfmLRl.png" width="600" height="600" />

#### Show Page

On the indeed website, if you’re interested in a job, clicking on it will bring you to a page with more information. This was my second task in the front end, after getting the index page operational. Unlike the JobCard used in the index page, the show page accessed all the keys in the Schema. As long as the Axios requests are correct, I can use dot notation `{job.location}` . I was able to access each key in the back end and display it in the front end. 

<img src="https://i.imgur.com/fB2cdXw.png" width="600" height="600" />

#### Styling 

Not using a styling framework like Bulma or Bootstrap was hard in this project as I was pushed for time. However, I persevered with SASS and tried to get close to the styling on the Indeed website. Below is my header for the Homepage vs the header on the homepage March 2022. There have been some minor changes but it's quite close. In further improvements, some vertical padding between the search boxes and the Navbar is required. Another improvement would be if the Find Jobs, Company Reviews and Explore Salaries were in separate inline `<div>`. From there it would be easier to create the left section and right section you see in the Indeed.com header. 

<img src="https://i.imgur.com/Qg2hWB9.png" width="600" height="100" />
<img src="https://i.imgur.com/GbF1Tnv.png" width="600" height="100" />

## Bugs

A current bug is data not pulling through from the back end. In development, the data pulls through just fine however in build and in deployment the data does not come through, which leaves a rather unimpressed website. This bug will be resolved ASAP so further bug tests can be carried out. I will document the findings of why this CORS error is blocking the information from coming through. 

## Challenges

The main challenge was the time restraint. I had covid before the project began and a few days into the project, so what started like 7 days to do the work by myself turned into 4.5 days. I had to discard the expectations of trying to complete my stretch goals and just try to make the MVP. Annoying as that was, it was good to adapt my plan of work to a new challenge, just like you would in the workplace if conditions changed. 

Another challenge was using Django and Python for the first time. Although Python is new to me, I like the readability of the code. JavaScript can be very unreadable at times whereas Python you can almost read the code line for line and make sense out of it. Django was very strange to use, I enjoyed the admin tools, I used that to add some information into the database. However, running a lot of the code through the command line and not having the ability to change every detail made it confusing at times.

## Wins & Learning 

A key learning achievement on this project was using a new language Python and successfully creating a back end. I didn’t do as many relationships than I had planned for but It still worked so I was pleased with my ability to adapt to a new language and integrate that into my front end to create an app. 

A big win for me on this project was the styling, I didn’t take any shortcuts and use a framework like Bulma or Bootstrap, I preserved with SASS to create styling that closely matches that of Indeed.

## Area For Future Development

Due to the time constraints and complexities of the project, I didn’t get time to do the stretch goals. This is something I will be working on during March 2022 and will redeploy with the new features and all the bugs fixed. 

In my planning phase, the idea of applying to jobs was that it would work similarly to how comments work. However recently I discovered an NPM plugin that allows users to send auto-generated emails. This means I could adapt this function so that users (if signed in) could click “apply” and an auto-generated email would be sent to the company saying that the user is interested and wants more details. 
