files := $(shell find ../trunk/ib/ -name "*.py")
modules := $(wordlist 1, $(words $(files)), $(files))

fix := python -c "import sys; s=sys.stdin.readline().replace('__init__', ''); print s[9:-4].replace('/', '_') + '.wiki'"
wd := $(shell pwd)

.PHONY: all $(modules)

all: $(modules)

$(modules):
	@export PYTHONPATH=$(wd)
	pythondoc.py -s -O wikiformatter -D outfile=$(shell echo $@ | $(fix)) $@
