files := $(shell find ../trunk/ib/ -name "*.py")
modules := $(wordlist 1, $(words $(files)), $(files))
fix := python -c "import sys; s=sys.stdin.readline().replace('__init__', ''); print s[9:-4].replace('/', '_') + '.wiki'"
linkbase := http://ibpy.googlecode.com/svn


.PHONY: all $(modules)


all: $(modules)


$(modules):
	@export PYTHONPATH=$(shell pwd)
	pythondoc.py -s -O wikiformatter -D outfile=$(shell echo $@ | $(fix)) -D link=$(linkbase)$(subst ..,,$@) $@


## base + module.attrib['filename']