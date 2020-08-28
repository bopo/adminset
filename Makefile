# Makefile six

PIP=$(VIRTUAL_ENV)/bin/pip
PY=$(VIRTUAL_ENV)/bin/python

.PHONY: clean-pyc clean-build clean clean-others pep8 start shell

help:
	@echo "Available commands:"
	@echo "  clean - 清理各种编译和临时文件."
	@echo "  start - 运行 Django 服务器."
	@echo "  shell - 运行 Django Shell."
	@echo "  test  - 运行测试脚本."
	@echo "  lint  - 项目文件语法检查."
	@echo "  fmt   - 格式化文件导入格式化."
	@echo "  dep   - 安装项目所需的包."

distclean: clean
	rm -rf fixture tests Procfile pytest.ini Vagrantfile requirements requirements.in env.* db.sqlite3 Pipfile *.md *.py
	find service -type f -name "[0-9]*.py" | xargs rm -rf
	rm -rf .pytest_cache
	rm -rf .vagrant

clean: clean-build clean-others clean-test clean-pyc

clean-migrate:
	find . -type d -name migrations -exec find {} -name "[0-9]*.py" \; | egrep -v '__init__.py' | xargs rm
	#find service -type f -name "[0-9]*.py" | xargs rm -rf
	#find . -type d -name migrations -exec find {} -name "[0-9]*.py" \;

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf .eggs/
	rm -rf '*.tgz'

	find . -name '*.egg-info' -exec rm -rf {} +
	find . -name '*.egg' -exec rm -rf {} +
	find . -name '*.log' -exec rm -rf {} +
	find . -name '*.sql' -exec rm -rf {} +

clean-others:
	rm -rf runtime/**/**
	rm -rf celerybeat-schedule
	rm -rf dump.rdb
	rm -rf deploy/.fabric

	find . -name 'Thumbs.db' -exec rm -rf {} +
	find . -name '*.tgz' -exec rm -rf {} +
	find . -name 'dump.rdb' -exec rm -rf {} +
	find . -name 'celery*.db' -exec rm -rf {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -rf {} +
	find . -name '*.pyo' -exec rm -rf {} +
	find . -name '*~' -exec rm -rf {} +
	find . -name '__pycache__' -exec rm -rf {} +

clean-test:
	rm -rf nosetests.html
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf reports/
	rm -rf .tox/

lint:
	@pylint -r y service
# 	isort --recursive .
# 	flake8 service tests
# 	pycodestyle --ignore=E501,F403,E122 **/*.py

fmt:
	yapf -i -r . -vv --style=google

dep:
	@$(PY) -m pip install -r requirements.txt

test:
	DJANGO_SETTINGS_MODULE=config.settings.dev TEST=1 $(PY) manage.py test --traceback -v2 tests

start:
	@$(PY) manage.py runserver_plus

shell:
	@$(PY) manage.py shell_plus

init:
	mkdir -p assets/media
	mkdir -p assets/static
	mkdir -p runtime/log
	mkdir -p runtime/run

# DO NOT DELETE
