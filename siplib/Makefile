TARGET = sip.so
OFILES = siplib.o apiversions.o descriptors.o qtlib.o threads.o objmap.o voidptr.o array.o int_convertors.o bool.o
HFILES = sip.h sipint.h array.h 

CC = cc
CXX = c++
LINK = c++
CPPFLAGS = -DNDEBUG -DSIP_MODULE_NAME=PyQt5.sip -I. -I/usr/local/opt/python@3.9/Frameworks/Python.framework/Versions/3.9/include/python3.9
CFLAGS = -pipe -fPIC -arch x86_64 -Os -Wall -W
CXXFLAGS = -pipe -fPIC -arch x86_64 -Os -Wall -W
LFLAGS = -headerpad_max_install_names -bundle -undefined dynamic_lookup -arch x86_64
LIBS = 
.SUFFIXES: .c .o .cpp .cc .cxx .C


.cpp.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cc.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.cxx.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.C.o:
	$(CXX) -c $(CXXFLAGS) $(CPPFLAGS) -o $@ $<

.c.o:
	$(CC) -c $(CFLAGS) $(CPPFLAGS) -o $@ $<

all: $(TARGET)

$(OFILES): $(HFILES)

$(TARGET): $(OFILES)
	$(LINK) $(LFLAGS) -o $(TARGET) $(OFILES) $(LIBS)

install: $(TARGET)
	@test -d $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/lib/python3.9/site-packages/PyQt5 || mkdir -p $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/lib/python3.9/site-packages/PyQt5
	cp -f $(TARGET) $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/lib/python3.9/site-packages/PyQt5/$(TARGET)
	@test -d $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/lib/python3.9/site-packages/PyQt5 || mkdir -p $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/lib/python3.9/site-packages/PyQt5
	cp -f /Users/uweschmitt/Projects/sip4/sip.pyi $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/lib/python3.9/site-packages/PyQt5/sip.pyi

clean:
	-rm -f $(TARGET)
	-rm -f siplib.o
	-rm -f apiversions.o
	-rm -f descriptors.o
	-rm -f qtlib.o
	-rm -f threads.o
	-rm -f objmap.o
	-rm -f voidptr.o
	-rm -f array.o
	-rm -f int_convertors.o
	-rm -f bool.o
