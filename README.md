# commerce-website


1) There will be a requirements.txt file in Root Please Read it further more there is 

2) A File named commands.sh Run it for install all the depedencies
   
3) I use phpmyadmin based on mysql if you are using mysql 
then add following code in settings.py
           
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'DATABASE_NAME_HERE',
                'USER': '',
                'PASSWORD': '',
                'HOST': 'localhost',
                'PORT': '3306',
                'OPTIONS': {
                    'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
                }
            }
        }


