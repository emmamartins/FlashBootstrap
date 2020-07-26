# Pytonik Bootstrap Flash Message

Store messages in session data until they are retrieved. Bootstrap compatibility, sticky messages, and more


## Installation

### With Pip

````
pip install FlashBootstrap
````

### With Git
````
git clone https://github.com/emmamartins/FlashBootstrap
````

Import the file:

````python
from FlashBootstrap.FlashBootstrap import FlashBootstrap
````
or

````python
from FlashBootstrap.FlashBootstrap import *
````

## Basic Usage

````python

	
#Instantiate the class
msg = FlashBootstrap
#Add messages
msg.info('This is an info message')
msg.success('This is a success message')
msg.warning('This is a warning message')
msg.error('This is an error message')

	
#Wherever you want to display the messages simply call:
msg.display()
````

### Message Types

#### Info
````python
msg.info('This is a info message')
````

![Info Message](http://mikeeverhart.net/php-flash-messages/assets/img/info.png)

#### Success
````python
msg.success('This is a success message')
````
![Success Message](http://mikeeverhart.net/php-flash-messages/assets/img/success.png)


#### Warning
````python
msg.warning('This is a warning message')
````
![Warning Message](http://mikeeverhart.net/php-flash-messages/assets/img/warning.png)

#### Error
````python
msg.error('This is a error message')
````
![Error Message](http://mikeeverhart.net/php-flash-messages/assets/img/error.png)


