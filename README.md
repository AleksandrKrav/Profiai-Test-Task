# Profiai Test Task

### Before run

Build docker image

```
    docker-compose build
```

Run docker containers

```
    docker-compose up -d
```

### How to run

Should execute generate_employee django command.

Parameters for action arguments - **[create, get]**
Default - *create*.

```
    docker-compose run api_server python manage.py generate_employee --action=get 
```

Examples:

```
(.env) Alexs-MacBook-Pro:profiai alexkravchuk$ docker-compose run api_server python manage.py generate_employee --action=create
Starting profiai_mariadb_server_1 ... done
2020-04-15 09:37:08,659 main.management.commands.generate_employee INFO     create
2020-04-15 09:37:08,659 main.management.commands.generate_employee INFO     Create employee with all parameters
2020-04-15 09:37:08,669 main.management.commands.generate_employee INFO     Create employee with required fields.
2020-04-15 09:37:08,674 main.management.commands.generate_employee INFO     Create employee with non validate fields.
2020-04-15 09:37:08,675 main.services ERROR    Failed to save employee to database
2020-04-15 09:37:08,675 main.management.commands.generate_employee INFO     Failed create employee with non validate fields.
(.env) Alexs-MacBook-Pro:profiai alexkravchuk$ docker-compose run api_server python manage.py generate_employee --action=get
Starting profiai_mariadb_server_1 ... done
2020-04-15 09:37:25,153 main.management.commands.generate_employee INFO     get
2020-04-15 09:37:25,153 main.management.commands.generate_employee INFO     Get data from database by name=Alex
2020-04-15 09:37:25,160 main.management.commands.generate_employee INFO     Result: [Employee(name=Alex, surname=Karpenko, salary=26 age=1000), Employee(name=Alex, surname=Kravchuk, salary=None age=None), Employee(name=Alex, surname=Karpenko, salary=26 age=1000), Employee(name=Alex, surname=Kravchuk, salary=None age=None)]


```
