
all:
	@(cd siplib; $(MAKE))

install:
	@(cd siplib; $(MAKE) install)

clean:
	@(cd siplib; $(MAKE) clean)
