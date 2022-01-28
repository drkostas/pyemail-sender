# Python Emailer

[![CircleCI](https://circleci.com/gh/drkostas/pyemail-sender/tree/master.svg?style=svg)](https://circleci.com/gh/drkostas/pyemail-sender/tree/master)
[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/drkostas/pyemail-sender/master/LICENSE)

## About <a name = "about"></a>

A utility for sending emails with attachments. Currently only Gmail 
is supported. [PYPI Package](https://pypi.org/project/pyemail-sender/)

## Table of Contents

+ [Using the library](#using)
    + [Installing and using the library](#install_use)
    + [Examples of usage](#examples)
+ [Manually install the library](#manual_install)
    + [Prerequisites](#prerequisites)
    + [Install the requirements](#installing_req)
    + [Run the Unit Tests](#unit_tests)
+ [Continuous Integration](#ci)
+ [Update PyPI package](#pypi)
+ [License](#license)

## Using the library <a name = "using"></a>

For a detailed usage example see 
[example.py](https://github.com/drkostas/pyemail-sender/master/example.py).

You will need an application-specific password for your Google account. 
[Reference 1](https://support.google.com/mail/?p=InvalidSecondFactor), 
[Reference 2](https://security.google.com/settings/security/apppasswords)

### Installing and using the library <a name = "install_use"></a>

First, you need to install the library using pip:

```shell
$ pip install pyemail_sender
```

Then, import it and initialize it like so:

```python
from pyemail_sender import GmailPyEmailSender

email_conf = {'type': 'gmail',
              'config': {'api_key': 'your api key', 'email_address': 'youremail@gmail.com'}}
pymail = GmailPyEmailSender(config=email_conf)
```

If you want to use a yml file to load the configuration, you can use the `PyEmailSenderConfig` class:
```python
from pyemail_sender import PyEmailSenderConfig
import os

config_path = str(os.path.join('confs', 'conf.yml'))
config = PyEmailSenderConfig(config_src=config_path)
email_conf = config.get_pyemail_sender_config()
```

Two example YAML files can be found in 
the [confs folder](https://github.com/drkostas/pyemail-sender/blob/master/confs).
For more details on how to use this YAML configuration loader see 
this [Readme](https://github.com/drkostas/yaml-config-wrapper/blob/master/README.md).

### Examples of usage <a name = "examples"></a>


**Send Simple Email**
```python
pymail.send_email(subject='A simple email',
                  to=[email_conf['email_address']],
                  text='Email body text goes here')
```
**Send HTML Email**
```python
pymail.send_email(subject='A simple HTML email',
                  to=[email_conf['email_address']],
                  html='<h1>Email body with HTML goes here</h1>')
```
**Send Email with all the arguments**
```python
pymail.send_email(subject='Email with all possible arguments',
                  sender=email_conf['email_address'],
                  to=[email_conf['email_address']],
                  cc=[email_conf['email_address']],
                  bcc=[email_conf['email_address']],
                  reply_to=email_conf['email_address'],
                  html='<h1>Test <b>HTML</b> body</h1>',
                  attachments=['my_file.txt'])
```

All of these examples can be found 
in [example.py](https://github.com/drkostas/pyemail-sender/tree/blob/master/example.py).

## Manually install the library <a name = "manual_install"></a>

These instructions will get you a copy of the project up and running on your local machine for
development and testing purposes.

### Prerequisites <a name = "prerequisites"></a>

You need to have a machine with
[anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) installed and
any Bash based shell (e.g. zsh) installed.

```ShellSession

$ conda -V
conda 4.10.1

$ echo $SHELL
/usr/bin/zsh

```

### Install the requirements <a name = "installing_req"></a>

All the installation steps are being handled by
the [Makefile](https://github.com/drkostas/pyemail-sender/blob/master/Makefile).

First, modify the python version (`min_python`) and everything else you need in
the [settings.ini](https://github.com/drkostas/pyemail-sender/blob/master/settings.ini).

Then, execute the following commands:

```ShellSession
$ make create_env
$ conda activate pyemail_sender
$ make dist
```

Now you are ready to use and modify the library.

### Run the Unit Tests <a name = "unit_tests"></a>

If you want to run the unit tests, execute the following command:

```ShellSession
$ make tests
```

## Continuous Integration <a name = "ci"></a>

For the continuous integration, the <b>CircleCI</b> service is being used. For more information you can
check the [setup guide](https://circleci.com/docs/2.0/language-python/).

For any modifications, edit
the [circleci config](https://github.com/drkostas/pyemail-sender/blob/master/.circleci/config.yml).

## Update PyPI package <a name = "pypi"></a>

This is mainly for future reference for the developers of this project. First,
create a file called `~/.pypirc` with your pypi login details, as follows:

```
[pypi]
username = your_pypi_username
password = your_pypi_password
```

Then, modify the python version (`min_python`), project status (`status`), release version (`version`) 
and everything else you need in
the [settings.ini](https://github.com/drkostas/pyemail-sender/blob/master/settings.ini).

Finally, execute the following commands:

```ShellSession
$ make create_env
$ conda activate pyemail_sender
$ make release
```

For a dev release, change the `testing_version` and instead of `make release`, run `make release_test`.

## License <a name = "license"></a>

This project is licensed under the MIT License - see
the [LICENSE](https://github.com/drkostas/pyemail-sender/blob/master/LICENSE) file for details.

<a href="https://www.buymeacoffee.com/drkostas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
