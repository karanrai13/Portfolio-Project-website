Project is created by karan rai TYBCA(science) Prof. ramkrishna more college, akurdi 

follow the instruction to run the project

Requirement -> python and virtualenv (pip install virtualenv)

step1 -> create a virtual environment in the Project Folder USING command
         virtualenv env

step2 -> activate the virtual environment USING command
        . .\env\Scripts\activate.ps1

step3 -> Run requirements.txt file USING command
        pip install -r requirements.txt

step4 -> setup database
        python manage.py makemigrations
        python manage.py migrate

step5 -> run the project
        python manage.py runserver

        server is running on  -> http://127.0.0.1:8000/
        to access admin panel -> http://127.0.0.1:8000/admin/  (username -> karan , password -> karan)

        you can even create a fresh database and newuser just delete the db.sqlite3 file and go to step4
        
        To create a user enter this command
        python manage.py createsuperuser

Functionality of website -> 1 website is mobile responsive
                           2 dynamic gallery is there you can upload image from the admin panel
                           3 contact detail will be save the admin panel 

If any error occur feel free to contact me 
phone no -> 7249518265
