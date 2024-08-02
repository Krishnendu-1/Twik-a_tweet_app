# Project: Twik - a tweet app
**Full stack _Django_ project to _Create, Edit, Delete_ and view tweets from different usernames with _Register, Login and Logout_ functionalities. It emphasizes user authentication and secure tweet management system, ensuring that users can interact with their own tweets while viewing tweets from others.**

![Screenshot (70)](https://github.com/user-attachments/assets/d4d6eb12-fed0-4956-ab64-c935439c2818)

**_Key Features_:**

**User Authentication:** Users must register or log in with a unique username and password to create a new tweet. Creation, editing, and deletion of tweets are restricted to authenticated users only.
**Tweet Management:** Users can view tweets from other users but can only edit or delete their own tweets. Each tweet can be accompanied by a favorite image selected by the user. Tweets are displayed to users based on the posting time. If no image is selected, a default image is displayed with the tweet.
**User Interface:** The frontend is built with static HTML and Bootstrap for an eye-catching design. The tweets are presented in a clean, chronological order for easy browsing.

**_Development Features_:**

**Frontend:** Static HTML and Bootstrap are used to create a visually appealing and responsive website.
**Backend:** Django serves as the backend framework, implementing the Model-View-Template (MVT) architecture. The default Django database, SQLite, is used for managing user data and tweets.
**Security and Forms:** Django authentication mechanisms are employed to protect user data and restrict access. Django forms, created within the app, include CSRF tokens for security, ensuring safe data handling for registration, login, and logout functionalities.
**Image Handling:** The Pillow library is added to the requirements.txt file for efficient image processing and management.
**Additional Security:** Django's inbuilt security features are leveraged to make the web app resilient against common web vulnerabilities, ensuring a secure environment for managing tweets.

**_Installation_:**

To set up the project, follow these steps:
# All the commands should be run in `sh`(bash,command prompt,windows powershell etc.) under the project tree

**Clone the repository:**

**`git clone https://github.com/Krishnendu-1/Twik-a_tweet_app`
`cd Twik-a_tweet_app`**

**Create a virtual environment and activate it:**

**`python -m venv virtual_env`**
**#On Windows use `virtual_env\Scripts\activate.bat` 
  #On mac/unix use `source env/bin/activate.bat`**

**Install the required packages:**

**`pip install -r requirements.txt`**

**Apply migrations:**

**`python manage.py migrate`**

**Run the development server:**

**`python manage.py runserver`**

**_Congrats!_**

Usage:

Navigate to http://127.0.0.1:8000 to access the web application.
Register a new account or log in with an existing account.
Create, view, edit, and delete tweets as per the permissions.
Feel free to explore, modify, and enhance the project to suit your needs. Contributions are welcome!

By following these guidelines and utilizing Django's robust features, this Tweet Management Web Application offers a secure, user-friendly, and efficient platform for managing tweets.

Thank you,
Krishnendu Roy
