#!/usr/bin/env bash


until echo '\q' | mysql -h $API_MYSQL_HOST -u $API_MYSQL_USER -p$API_MYSQL_PASSWORD app; do
    >&2 echo "MariaDB is unavailable - sleeping"
    sleep 1
done

>&2 echo "MariaDB and Data are up - executing command"
