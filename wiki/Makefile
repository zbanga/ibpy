files := $(shell find ../trunk/ib/ -name "*.py")
modules := $(wordlist 1, $(words $(files)), $(files))

fix := python -c "import sys; s=sys.stdin.readline(); print s[9:].replace('/', '_').replace('.py', '.wiki')"

.PHONY: all $(modules)

all: $(modules)

$(modules):
	@export PYTHONPATH=.
	pythondoc.py -s -O wikiformatter -D outfile=$(shell echo $@ | $(fix)) $@



