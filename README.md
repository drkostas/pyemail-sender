# Cloud Filemanager

[![CircleCI](https://circleci.com/gh/drkostas/cloud-filemanager/tree/master.svg?style=svg)](https://circleci.com/gh/drkostas/cloud-filemanager/tree/master)
[![GitHub license](https://img.shields.io/badge/license-Apache-blue.svg)](https://github.com/drkostas/cloud-filemanager/master/LICENSE)

## About <a name = "about"></a>

A high-level filemanager utility for cloud services. Currently, only Dropbox 
is supported. [PYPI Package](https://pypi.org/project/cloud-filemanager/)

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
[example.py](https://github.com/drkostas/cloud-filemanager/master/example.py).

### Installing and using the library <a name = "install_use"></a>

First, you need to install the library using pip:

```shell
$ pip install cloud_filemanager
```

Then, import it and initialize it like so:

```python
from cloud_filemanager import DropboxCloudManager

cloud_conf = {'type': 'dropbox', 'config': {'api_key': 'your api key'}}
dbx = DropboxCloudManager(config=cloud_conf)
```

If you want to use a yml file to load the configuration, you can use the `CloudConfig` class:
```python
from cloud_filemanager import CloudConfig
import os

config_path = str(os.path.join('confs', 'conf.yml'))
config = CloudConfig(config_src=config_path)
cloud_conf = config.get_cloud_config()
```

Two example YAML files can be found in 
the [confs folder](https://github.com/drkostas/cloud-filemanager/blob/master/confs).
For more details on how to use this YAML configuration loader see 
this [Readme](https://github.com/drkostas/yaml-config-wrapper/blob/master/README.md).

### Examples of usage <a name = "examples"></a>

The currently supported operations are the following:
- Upload, Download, Delete Files
- List directories

**Upload**
```python
with open('my_file.txt', 'rb') as fp:
    file_to_upload = fp.read()
dbx.upload_file(file_bytes=file_to_upload, upload_path='/tests/my_file.txt', write_mode='overwrite')
```
**Download**
```python
dbx.download_file(frompath='/tests/my_file.txt', tofile='my_file_downloaded.txt')
```
**Delete**
```python
dbx.delete_file('/tests/my_file.txt')
```
**List Files**
```python
dbx.ls('/tests/')
```

All of these examples can be found 
in [example.py](https://github.com/drkostas/cloud-filemanager/tree/blob/master/example.py).

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
the [Makefile](https://github.com/drkostas/cloud-filemanager/blob/master/Makefile).

First, modify the python version (`min_python`) and everything else you need in
the [settings.ini](https://github.com/drkostas/cloud-filemanager/blob/master/settings.ini).

Then, execute the following commands:

```ShellSession
$ make create_env
$ conda activate yaml_config_wrapper
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
the [circleci config](https://github.com/drkostas/cloud-filemanager/blob/master/.circleci/config.yml).

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
the [settings.ini](https://github.com/drkostas/cloud-filemanager/blob/master/settings.ini).

Finally, execute the following commands:

```ShellSession
$ make create_env
$ conda activate yaml_config_wrapper
$ make release
```

For a dev release, change the `testing_version` and instead of `make release`, run `make release_test`.

## License <a name = "license"></a>

This project is licensed under the MIT License - see
the [LICENSE](https://github.com/drkostas/cloud-filemanager/blob/master/LICENSE) file for details.

<a href="https://www.buymeacoffee.com/drkostas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
