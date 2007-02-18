##
## This is the IbPy distribution Makefile.  Use this file to build a
## source distribution only after the source has been edited, remade,
## and checked into the repository.
##
## To build a source distribution, run:
##
##	make dist
##

ibpy_ver     := 0.7.0
ibpy_rev     := $(shell svnversion|cut -f 2 -d \:|cut -f 1 -d M)
twsapi_ver   := $(shell cat ib/ext/src/IBJts/API_VersionNum.txt |cut -f 2 -d \=)
release_num  := $(ibpy_ver)-$(twsapi_ver)
release_dir  := release-$(release_num)
release_date := $(shell date +"%d %b %Y")
release_root := IbPy-$(release_num)
release_file := $(release_root).tar.gz
svn_root     := http://ibpy.melhase.net/repos/branches/ast


.PHONY: all clean


.SILENT: clean $(release_dir)


all: dist


clean:
	$(if $(wildcard $(release_dir)), echo [W] removing release directory $(release_dir))
	rm -rf $(release_dir)


dist: $(release_dir)


$(release_dir):
	echo [I] building release=$(release_num) version=$(ibpy_ver) revision=$(ibpy_rev) api=$(twsapi_ver)
	echo [I] exporting trunk from $(svn_root) into $(release_dir)
	svn export $(svn_root) $(release_dir) > /dev/null
	echo [I] fixing version strings
	cd $(release_dir)/ib && sed -i s/api\ \=\ \"0\"/api\ \=\ \"$(twsapi_ver)\"/ __init__.py
	cd $(release_dir)/ib && sed -i s/version\ \=\ \"0\"/version\ \=\ \"$(release_num)\"/ __init__.py
	cd $(release_dir)/ib && sed -i s/revision\ \=\ \"r0\"/revision\ \=\ \"r$(ibpy_rev)\"/ __init__.py
	cd $(release_dir)/ && sed -i s/version\ \=\ \"0\"/version\ \=\ \"$(release_num)\"/ setup.py
	cd $(release_dir)/ && sed -i s/\:release_num\:/$(release_num)/ README
	cd $(release_dir)/ && sed -i s/\:release_date\:/"$(release_date)"/ README
	cd $(release_dir)/ && sed -i s/\:twsapi_ver\:/$(twsapi_ver)/ README
	cd $(release_dir)/ && sed -i s/\:release_file\:/$(release_file)/ README
	cd $(release_dir)/ && sed -i s/\:release_root\:/$(release_root)/ README
	echo [I] building source distribution
	cd $(release_dir) && python setup.py sdist > /dev/null
	echo [I] source distribution file: $(release_dir)/dist/$(release_file)
