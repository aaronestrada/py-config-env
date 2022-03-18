import os
from dotenv import load_dotenv
from werkzeug.utils import import_string


class EnvironmentLoader:
    """
    Class to read environment configuration variables from folder in the root path of the application.

    Each environment file contains the variables that will be stored in a dictionary.
    """

    def __init__(self,
                 env_file: str = 'example',
                 env_variable: str = 'APP_ENVIRONMENT',
                 env_path: str = 'environments'):
        """
        Class constructor

        :param env_file: Name of file to load
        :param env_variable: Variable on .env.example file containing the environment file to load
        :param env_path: Path in project to store environment files
        """
        if type(env_variable) != str:
            env_variable = 'APP_ENVIRONMENT'

        if type(env_file) != str:
            env_file = 'example'

        if type(env_path) != str:
            env_path = 'environments'

        load_dotenv()

        # --------------------------------------
        # Priority of loading
        # 1) file name from OS variable
        # 2) file name from .env.example file
        # 3) file name from parameter 'env_file'
        # --------------------------------------
        env_file_os = os.getenv(env_variable, None)
        if env_file_os not in ['', None]:
            env_file = env_file_os

        self._env_file = env_file
        self._env_path = env_path

    def _get_vars(self) -> dict:
        """
        Retrieve list of variables with multiline values

        :return: Key -> value variables to set in application
        """
        multiline_vars = {}
        module = import_string(f'{self._env_path}.{self._env_file}', silent=True)

        if module is not None:
            variables = vars(module)

            for item in dir(module):
                # Load only public variables
                if item.startswith("__") == 0:
                    multiline_vars[item] = variables[item]

        return multiline_vars

    @property
    def configuration(self) -> dict:
        return self._get_vars()
