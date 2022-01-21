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
	pdoc -d restructuredtext -o .\build\docs hellosamples