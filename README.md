
# REST API for autopark application

REST API application for autopark with car and drivers 
The application working with Drivers and Vehicles models.

## Built With
* [Python v3.10.0](https://www.python.org/) - Programming language
* [Django](https://www.djangoproject.com/) - The web framework used
* [Django Rest Framework](https://www.django-rest-framework.org/) - The toolkit for building Web APIs.
* [SQLite](https://sqlite.org/index.html) - Database 
### OPTIONAL (for UNIX-like systems)
* [Pyenv](https://github.com/pyenv/pyenv) - Simple Python Version Management
* [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) - plugin that provides features to manage virtualenvs and conda environments for Python on UNIX-like systems.

## General Notes
+ An autopark app has already been provided in this repo upon which you will be adding a new assesement feature.
+ The project provides to get, post, update and delete information about drivers/vehicles. 
+ Depends on your deployment, you may choose any SQL database Django supported such as SQLite3, PostgreSQL, and MySQL (default is SQLite3).


## Endpoint`s

Driver:
+ GET /drivers/driver/ - output drivers list
+ GET /drivers/driver/?created_at__gte=10-11-2021 - output of the list of drivers created after 10-11-2021
+ GET /drivers/driver/?created_at__lte=16-11-2021 - output of the list of drivers created before 16-11-2021
+ GET /drivers/driver/<driver_id>/ - obtaining information on a particular driver
+ POST /drivers/driver/ - create new driver
  + Required fields:
  

    {
        "first_name": str,
        "last_name": str
    }
+ UPDATE /drivers/driver/<driver_id>/ - update driver`s info
  + Required fields:
  

    {
        "first_name": str,
        "last_name": str
    }
+ DELETE /drivers/driver/<driver_id>/ - delete driver

Vehicle:
+ GET /vehicles/vehicle/ - output vehicles list
+ GET /vehicles/vehicle/?with_drivers=yes - output of the list of cars with drivers
+ GET /vehicles/vehicle/?with_drivers=no - output of the list of cars without drivers
+ GET /vehicles/vehicle/<vehicle_id> - obtaining information on a specific machine
+ POST /vehicles/vehicle/ - create new vehicle
  + Required fields:
  

    {
        "driver_id": int/null,
        "make": str,
        "model": str,
        "plate_number": str
    }
+ UPDATE /vehicles/vehicle/<vehicle_id>/ - update vehicle`s info 
  + Required fields:
  

    {
        "make": str,
        "model": str,
        "plate_number": str 
    }
+ POST /vehicles/set_driver/<vehicle_id>/ - put the driver in the car / get the driver out of the car
  + Required fields:
  

    {
        "driver_id": int/null
    }
+ DELETE /vehicles/vehicle/<vehicle_id>/ - delete vehicle

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details