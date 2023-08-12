# local-airflow

Use this repository to create a local airflow environment
on your computer. Before setting up the environment, make
sure that:

1. Your docker environment is up and running,
and you have docker-compose installed on your machine.
2. If you are in a private network, you have access to
docker images for postgres (preferably 13) and
apache/airflow (preferably 2.6.3).
3. You have enough memory on your computer and on your
docker environment. Airflow will alert you if you have
less than 4 GB, and it is best to allocate at least
5GB for docker overall, if possible.

Now that we are ready to deploy our local airflow
environment, run the next commands in your terminal:
```bash
docker compose up airflow-init
docker-compose up -d
```
When all the containers created by those commands are
up and running, go to https://0.0.0.0:8080 where you
will find a login page. Enter airflow as the username
and password.

## You are done! Enjoy your new airflow