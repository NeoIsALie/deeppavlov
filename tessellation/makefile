SHELL = /bin/bash

test: 
	docker build -t tessellation .
	docker run --rm -ti -v "${PWD}":/usr/src/app tessellation python test_solution.py
.PHONY: test

test_example: 
	docker build -t tessellation .
	docker run --rm -ti -v "${PWD}":/usr/src/app tessellation python solution_example.py
.PHONY: test_example