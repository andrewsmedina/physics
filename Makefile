clean:
	@find . -name '*.pyc' -delete

test: clean
	@nosetests -s --with-coverage --cover-erase --cover-inclusive --cover-package=physics
