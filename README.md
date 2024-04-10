## setup
python3 -m virtualenv venv
source venv/bin/activate


# configure environment variables in .env file
MONGODB_URI = ''
PORT = ''

# install dependencies
pip install -r requirements.txt


# start flask server 
python main.py

# exposed endpoints

/webhook/test

/webhook/receive