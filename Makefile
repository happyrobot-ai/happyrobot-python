.PHONY: clean build upload

clean:
	rm -rf dist/*
	rm -rf build/*

build:
	python setup.py sdist bdist_wheel

upload: clean build
	twine upload dist/*