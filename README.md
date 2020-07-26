# Pytonik Bootstrap Flash Message

Store messages in session data until they are retrieved. Bootstrap compatibility, sticky messages, and more

## Installation

### With Pip

````
pip install FlashBootstrap
````

### With Git
````
git clone https://github.com/emmamartins/FlashBootstrap/
````

### Import the Module:

````python
from FlashBootstrap.FlashBootstrap import FlashBootstrap
````
or

````python
from FlashBootstrap.FlashBootstrap import *
````

### Defualt Parameter 

````
description=""
title=""
dismissible=True
key='flash' 

````

## Basic Usage

````python

#Instantiate the class
msg = FlashBootstrap

#Add messages With Bootstrap
msg.info('This is an info message')
msg.success('This is a success message')
msg.warning('This is a warning message')
msg.error('This is an error message')

#Add messages Without Bootstrap
msg.message('This is an info message')


#Wherever you want to display the messages simply call:
msg.display()
````

### Message Types

#### Info
````python
msg.info('This is a info message')
````

![Info Message](https://pytonik.com/public/assets/home/img/info.png)

#### Success
````python
msg.success('This is a success message')
````
![Success Message](https://pytonik.com/public/assets/home/img/success.png)


#### Warning
````python
msg.warning('This is a warning message')
````
![Warning Message](https://pytonik.com/public/assets/home/img/warning.png)

#### Error
````python
msg.error('This is a error message')
````
![Error Message](https://pytonik.com/public/assets/home/img/error.png)

### Redirect

It's possible to redirect to a different URL before displaying a message. For example, redirecting from **checklogin** back to a form **login** using **http_referral**, (and displaying an error message) so a user can correct an error - **subjected to pytonik developers**.

![Error Message](https://pytonik.com/public/assets/home/img/Flashbootstrap.gif)


````python 
  #Import Pytonik
  from pytonik.Web import app
  #Import FlashBoostrap
  from FlashBoostrap.FlashBoostrap import *

  def checklogin():
    FlashBoostrap.error('Cannot login account')
    return app.redirect('/login', True)
  
````

