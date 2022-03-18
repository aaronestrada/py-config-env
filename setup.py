from distutils.core import setup

setup(
    name='py-config-env',
    version='1.0',
    description='Read environment variables from configuration file, accessible from a dictionary.',
    license='BSD',
    author='Aaron Estrada Poggio',
    author_email='aaron.estrada.poggio@gmail.com',
    url='https://github.com/aaronestrada/py-config-env',
    packages=['py_config_env'],
    python_requires='>=3.6',
    install_requires=[
        'werkzeug>=2.0.3',
        'python-dotenv>=0.19.2'
    ]
)
