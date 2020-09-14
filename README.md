# Doctor Appointment App

### Brief Description
An app suited for everyone as far as fast and reliable health care services
are concerned. This app is build entirely in Python/Django as the backend and 
bootstrap on the frontend (CSS library). Within this app, users who are Doctors, by 
profession, can sign up and build their professional career portfolio, where users 
who are patients can find and reach them for their service.


#### Structure of the Project 
##### Backend
On the backend, ...


##### Frontend
On the Frontend, ...


#### Installation Guide
It takes not much to install and setup this project to run,
for the ease of setup and deployment purpose, **docker** was 
chosen for containerizing the project, but at the moment, it has
not been setup yet. But going through the normal setup guidelines,
follow the steps below:

##### Prerequisite
1. Python 3.6 or Higher
2. Django 3.0 or Higher (Django 2.2 will do but with minor configs)
3. Virtual Environment (pipenv, venv, etc)

**NOTE**  
This project comes with a requirements.txt file so all other 
packages and dependencies of the packages listed can be found
there with their specific versions

**Steps**  
1. Setup a virtual environment
2. Clone the project and cd into the project directory
3. Install the project dependencies
4. Run your project. Voila!!! It's done.

Run the code snippet in your terminal

```shell script
git clone https://github.com/kali-physi-hacker/Doctor-Appointment-App.git   # That clones the project to your local machine
cd Doctor-Appointment-App
python install -r requirements.txt
python manage.py runserver
```

**Note** that your run the 3rd and 4th commands after you have activated your
virtual environment.