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
