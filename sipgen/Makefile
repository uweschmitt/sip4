TARGET = sip
OFILES = main.o transform.o gencode.o extracts.o export.o type_hints.o heap.o parser.o lexer.o
HFILES = sip.h parser.h

CC = cc
CXX = c++
LINK = c++
CPPFLAGS = -DNDEBUG -I.
CFLAGS = -pipe -arch x86_64 -Os -Wall -W
CXXFLAGS = -pipe -arch x86_64 -Os -Wall -W
LFLAGS = -headerpad_max_install_names -arch x86_64
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
	@test -d $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/bin || mkdir -p $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/bin
	cp -f $(TARGET) $(DESTDIR)/Users/uweschmitt/Projects/sip4/venv/bin/$(TARGET)

clean:
	-rm -f $(TARGET)
	-rm -f main.o
	-rm -f transform.o
	-rm -f gencode.o
	-rm -f extracts.o
	-rm -f export.o
	-rm -f type_hints.o
	-rm -f heap.o
	-rm -f parser.o
	-rm -f lexer.o
