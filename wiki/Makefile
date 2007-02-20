files := $(shell find ../trunk/ib/ -name "*.py")
modules := $(wordlist 1, $(words $(files)), $(files))

fix := python -c "import sys; s=sys.stdin.readline().replace('__init__', ''); print 'Api' + str.join('', [a.title() for a in s[9:-3].split('/')]) + 'wiki'"

.PHONY: all $(modules)

all: $(modules)

$(modules):
	@export PYTHONPATH=.
	@pythondoc.py -s -O wikiformatter -D outfile=$(shell echo $@ | $(fix)) $@



