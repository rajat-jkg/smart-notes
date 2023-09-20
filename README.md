# Smart Notes

A simple Django application that allows users to create and manage notes. It has a LogIn portal built with django's default user management system. A user can add notes in the app and when you browse the notes you will be able to see the notes you have created.

## Web Link
[Click Here](https://smart-notes.rajat-jkg.repl.co/)

## Installation 

1. Download the code

2. Create an outlook email account.

3. In the file /home/mails.py , replace line 10 with the following code:

```
server = smtplib.SMTP('smtp-mail.outlook.com',587)
```

Line 14:

```
server.login('youremail@outlook.com', 'your_password')
```

Line 17:

```
message['From'] = 'Your Name <youremail@outlook.com>'
```

4. Create a virtual environment and activate.

```
$ python -m virtualenv environment_name
$ environment_name/Scripts/activate
```

5. Install Django.
```
$ pip install django
```

6. Go to the project's root directory and run manage.py file with command runserver

```
$ python manage.py runserver
```

7. This will run a server on localhost at the address displayed on the sehll/cmd.

8. Go to the browser and paste that address to run the application.

[Web link](https://smart-notes.rajat-jkg.repl.co/)