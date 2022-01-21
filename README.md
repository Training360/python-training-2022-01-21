# Python forráskód és projekt kezelés

Tematika, témák:

* Kód szervezés, modularizálás
* Javasolt könyvtár struktúra, kód struktúra
* Saját package fejlesztése, ami meghivatkozható más projektből
* Unit test
* PEP8

Windows környezet

* Python telepítése Choco-val https://chocolatey.org/

```shell
choco list --localonly
choco outdated
choco install python
python --version
```

## Új projekt

Új könyvtár: `hellosamples`

`hello.py`

```python
print("Hello Python")
```

Jelenleg ismert szervezési formák:

```python
def say_hello(name):
    return f"Hello {name}"
```

```python
class Greeting:

    def __init__(self, name):
        self.name = name

    def say_hello():
        return f"Hello {self.name}" 
```

# Modul - fájl

`hello_controller.py` létrehozása

```python
name = input("What is your name?")
say_hello(name)
```

Importkor meghívódik a modul

```python
if __name__ == "__main__":
```

# Csomag - könyvtár

Átmozgatás `src\hellosamples` könyvtárba, `__init__.py` fájl létrehozása

# Teszteset

Python 3.4 óta a `pip` része

Python Package Index: https://pypi.org/

pytest

A `tests` könyvtárban `test_say_hello`:

```python
def test_say_hello():
    assert say_hello("John Doe") == "Hello John Doe"
```

`requirements.txt` létrehozása:

```
pytest
```

```shell
python -m venv venv
python.exe -m pip install --upgrade pip
pip install -r ./requirements.txt

pytest
```

A `setup.py` tartalma

```python
#env/bin python

from distutils.core import setup

setup(name='hellosamples',
      version='1.0',
      packages=['hellosamples'],
      package_dir={'':'src'}
     )
```

```shell
pip install -e .
pytest -v
```

VS Code - laboredény

# Csomag futtatása direktben

```shell
python -m hellosamples.hello
```

`__main__.py`

```python
say_hello("Anonymous")
```

```shell
python -m hellosamples
```

## Külső csomag használata alkalmazásból

Új könyvtár

```python
import requests


response = requests.get('https://api.github.com/users/vicziani')
user = response.json()
print(user["public_repos"])
```

`requirements.txt`

A `setup.py` tartalma

```python
#env/bin python

from distutils.core import setup

setup(name='hellosamples',
      version='1.0',
      packages=['hellosamples'],
      package_dir={'':'src'}
     )
```

```
pip freeze
```

## Csomagolás Docker konténerbe

```dockerfile
FROM python
WORKDIR app
COPY *.py requirements.txt .
RUN pip install -r ./requirements.txt
ENTRYPOINT python repos.py
```

## Jupyter notebook

`pythontutorial` kvt.

```
jupyter
ipykernel
```

```shell
python -m venv venv
venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r ./requirements.txt
```

Közben a Visual Studio Code megkérdezi, hogy akarjuk-e a létrehozott virtual enviromentet használni, válasszuk, hogy igen.
Majd _F1_, és _Notebook: Select Notebook Kernel_.

## Jupyter és Selenium

`seleniumtutorial` kvt.

`HelloWorld.ipynb`

`requirements.txt`

```
jupyter
ipykernel
webdriver-manager
selenium
```

```shell
python -m venv venv
venv\Scripts\activate
python.exe -m pip install --upgrade pip
pip install -r ./requirements.txt
```

Közben a Visual Studio Code megkérdezi, hogy akarjuk-e a létrehozott virtual enviromentet használni, válasszuk, hogy igen.
Majd _F1_, és _Notebook: Select Notebook Kernel_.

Futtatás

## Átállás a pyproject.toml fájlra

A `setup.py` leváltására

Vissza a `hellosamples` kvt.

`pyproject.toml`

```
[build-system]
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
```

`setup.cfg`

```
[metadata]
name = hellosamples
version = 0.0.1
author = Istvan Viczian
description = hellosamples demo package
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/vicziani/jtechlog-python
project_urls =
    Bug Tracker = https://github.com/vicziani/jtechlog-python/issues
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir = = src
packages = find:
python_requires = >=3.8

[options.packages.find]
where = src

[options.extras_require]
test = 
    pytest
```

`README.md`

`venv` törlése

```shell
python -m venv venv
python.exe -m pip install --upgrade pip
python -m pip install -e .[test]
pytest -v
```

# Coverage

```
pytest --cov=jtechlog_python --cov-report=xml -v
```

# pylint

https://www.python.org/dev/peps/pep-0008/

```
pylint
```


`.pylintrc`

```
[MESSAGES CONTROL]
msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}"

disable=C0111
```

```shell
pylint src --rcfile=.pylintrc hellosamples -r n > pylint-report.txt
```

VC Code

F1 / Python: Select Linter
enable linting

# flake8

```shell
flake8 --exit-zero src > flake8-report.txt
```

# mypy

```
mypy
```

Type hinting

```shell
mypy src
```

# SonarQube

```shell
docker run --name my-sonarqube -d -p 9000:9000 sonarqube:lts
```

https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/

`sonar-project.properties`

```
sonar.projectKey=hellosamples
sonar.sources=src/hellosamples
sonar.host.url=http://localhost:9000
sonar.language=py
sonar.python.pylint.reportPaths=pylint-report.txt
sonar.python.flake8.reportPaths=flake8-report.txt
sonar.sourceEncoding=UTF-8
sonar.python.coverage.reportPaths=coverage.xml
sonar.login=admin
sonar.password=admin12
```

```shell
C:\Java\sonar-scanner-4.6.2.2472-windows\bin\sonar-scanner.bat
```

## Build

setuptools, wheel formátum

A Built Distribution format introduced by PEP 427, which is intended to replace the Egg format.

```shell
python -m pip install --upgrade build
python -m build
```

## Repo proxy

```
docker run --name nexus -d -p 8081:8081 sonatype/nexus3
docker exec -it nexus cat /nexus-data/admin.password
```

`pip.ini`

```
[global]
index = https://localhost:8081/repository/pypi-group/pypi
index-url = https://localhost:8081/repository/pypi-group/simple
```

vagy

```
[global]
trusted-host=localhost:8091
index = http://localhost:8091/repository/pypi-group/pypi
index-url = http://localhost:8091/repository/pypi-group/simple
no-cache-dir = false
```

```
pip config -v list
```

## Deploy

```
twine
```

`venv/pyvenv.cfg`

```
[distutils]
index-servers = pypi
[pypi]
repository: http://localhost:8081/repository/pypi-hosted/
username: admin
password: admin
```

```
python -m twine upload --config-file venv\pip.ini dist/*
```

## Docs

Futás időben le lehet kérni

```
"""
.. include:: ../../docs/fizzbuzz.md
"""
```

```
pdoc
```

```exit
pdoc -o .\build\docs hellosamples
```

## Make

```shell
choco install make
```

`Makefile`

```
install:
	python -m pip install -e .[test]

test:
	pytest --cov=hellosamples --cov-report=xml -v

pylint:
	pylint src --rcfile=.pylintrc hellosamples -r n > pylint-report.txt

flake8:
	flake8 --exit-zero src > flake8-report.txt

mypy:
	mypy src

sonar:
	C:\Java\sonar-scanner-4.6.2.2472-windows\bin\sonar-scanner.bat

package:
	python -m build

deploy:
	python -m twine upload --config-file venv\pip.ini dist/*

doc:
	pdoc -o .\build\docs hellosamples
```

## Felhasználás más projektben

`pip.ini` átmásolása

```
pip install hellosamples
pip show hellosamples
```

