files := $(shell find ../trunk/ib/ -name "*.py")
modules := $(wordlist 1, $(words $(files)), $(files))


.PHONY: all $(modules)

all: $(modules)

$(modules):
	@export PYTHONPATH=.
	pythondoc.py -s -O wikiformatter -D outfile=ApiDoc$(subst .py,.wiki,$(subst /,_,$(subst ../trunk,,$@))) $@


