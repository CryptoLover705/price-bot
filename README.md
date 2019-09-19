

# Requirements
* discord.py installed
* Python 3.6+
* A MySQL database


# Instructions
These instructions were used to create a working bot in March 2018.
Once a VPS is obtained, follow these instructions.
## mySQL
These instructions will help you install and setup a mySQL database
### Install mySQL
```
sudo apt-get install mysql-server
```
When prompted, set up a password for root.
### Configure mySQL Security
```
mysql_secure_installation
```
Press "Y" and ENTER to accept all the questions, with the exception of the one that asks if you'd like to change the root password.
### Verify mySQL is Running
```
systemctl status mysql.service
```
You should see a status message that says "active (running)".
## Update Python
Python should be updated to version 3.6 or later because version 3.5 is not compatible with some libraries
```
sudo add-apt-repository ppa:jonathonf/python-3.7
sudo apt update
sudo apt-get install python3.7
sudo apt-get install python3.7-dev
sudo apt-get install python3.7-venv
```
## Install Python's pip
Python's pip is a useful tool used to install python libraries
```
wget https://bootstrap.pypa.io/get-pip.py
sudo python3.6 get-pip.py
```
## Install json-rpc Library
```
pip install json-rpc
```
## Link python3 to python3.7
```
sudo ln -s /usr/bin/python3.7 /usr/local/bin/python3
```
## Install Discord Library
Install the discord library used for the bot, This uses the old discord libraries 
```
python3 -m pip install discord.py==0.16.12
```
## Install PyMySQL Library
```
pip install PyMySQL
```
