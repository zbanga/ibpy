files := $(shell find ../trunk/ib/ -name "*.py")
modules := $(wordlist 1, $(words $(files)), $(files))


.PHONY: all $(modules)


all: $(modules)


$(modules):
	@export PYTHONPATH=$(shell pwd)
	pythondoc.py -s -O wikiformatter $@
