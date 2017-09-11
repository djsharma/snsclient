# @Author: dhananjaysharma
# @Date:   2017-09-11 11:26:26
# @Last Modified by:   dhananjaysharma
# @Last Modified time: 2017-09-11 11:31:03
sudo apt-get update
sudo apt-get install python-pip
sudo pip install virtualenv
cd ..
virtualenv env
source env/bin/activate
pip install requests
pip install boto
pip install django