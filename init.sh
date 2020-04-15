#!/usr/bin/env bash


chmod +x ./wait-for-mysql.sh
./wait-for-mysql.sh

echo "Migrate data"
python ./manage.py migrate main
