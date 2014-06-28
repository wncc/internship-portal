WnCC Internship Portal
===
An initiative by Web and Coding Club, IIT Bombay

Developed in Django 1.5.2

## Configuration

 - Copy **settings.sample** file to *./internshipPortal/internshipPortal* and call it **settings.ini**. Essentially, execute the command: `cp settings.sample ./internshipPortal/internshipPortal/settings.ini`
 - Edit the configuration settings (Set username/password of your phpmyadmin etc.). These changes would automatically reflect in the **settings.py** file.
 - Add a new database called **internshipPortal** in your phpmyadmin and do a `./manage.py syncdb`.
 - Please do not push **YOUR** settings.ini file to the git repository.
