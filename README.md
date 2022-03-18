# Python Configuration Environment loader

This extension allows loading configuration files containing variables in a Python script, to then access to them via a
configuration dictionary.

## Requirements

* Python >= 3.6
* werkzeug >= 2.0.3
* python-dotenv >= 0.19.2

## Motivation

Applications might have a configuration file containing variables that will be different in each environment. This
extension reads a configuration file containing variables in Python, to then access to them via a configuration
dictionary.

## How to use the extension

Include the extension library and initialize a variable with the class ``EnvironmentLoader`. Check at this example.

`test_env.py`

```python
from py_config_env import EnvironmentLoader

env_loader = EnvironmentLoader(
    env_file='example_1',  # File to load
    env_variable='APP_ENVIRONMENT',  # Variable containing file to load (read from OS or from .env file)
    env_path='environments.files'  # Path where files are contained (use period for sub-folders)
)

# Variable containing loaded variables
configuration = env_loader.configuration

if __name__ == '__main__':
    # Use variables
    number_value = configuration.get('VARIABLE_INT')
    str_value = configuration.get('VARIABLE_STR')
    dict_value = configuration.get('VARIABLE_DICT')

    print(f'Person {dict_value.get("name")} {dict_value.get("last_name")}')
    print(f'Number: {number_value}')
    print(f'String: {str_value}')
```

## Priority of loading

### File name from OS variable

By setting the APP_ENVIRONMENT value before running the script, the environment configuration variable `env_loader` will
load `example_3.py`
file.

`Run script`

```bash
APP_ENVIRONMENT=example_3 python test_env.py
```

### File name from .env.example file

By creating a `.env` file and setting the APP_ENVIRONMENT value before running the script, the environment configuration
variable `env_loader` will load `example_2.py` file.

`.env`

```dotenv
APP_ENVIRONMENT=example_2
```

`Run script`

```bash
$ python test_env.py
```

### File name from parameter 'env_file'

If no OS nor .env file exist, the environment configuration variable `env_loader` will load `example_1.py` file.

`Run script (erase .env before)`

```bash
python test_env.py
```