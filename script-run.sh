apt-get install -y python python-dev python-setuptools python-pip
cp image.jpg ../
cd fit-calculator
pip install -r requirements.txt
python fitness.py 6001 & python fitness.py 6002 & python fitness.py 6003 & python fitness.py 6004 &
