SHELL = /bin/bash

test:
	docker build -t code_review .
	docker run --rm -ti code_review --path data.csv --control_sum 10
.PHONY: test