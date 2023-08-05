#!/bin/bash
echo "Creating env"
python3 -m venv env

echo "Activate env"
source "env/bin/activate"

echo "Installing requirements"
pip3 install -r requirements.txt

echo "Run servers"
python3 users/manage.py runserver 8000 &
users_pid=$!

python3 products/manage.py runserver 8001
products_pid=$!

kill $users_pid
kill $products_pid
echo "Servers stopped."


