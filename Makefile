# -*- mode: makefile-gmake; coding: utf-8 -*-

SUBDIRS = $(shell ls -d */)
SUBDIRS = \
	py py-icestorm py-ami py-amd \
	java \
	cpp cpp-icestorm cpp-observer cpp-ami \
	icegrid

all:     RULE = all
install: RULE = install
clean:   RULE = clean

all clean install: subdirs

check: all
	atheist .

clean:
	$(RM) *~


.PHONY: subdirs $(SUBDIRS)
subdirs: $(SUBDIRS)
$(SUBDIRS):
	$(MAKE) -C $@ $(RULE)
