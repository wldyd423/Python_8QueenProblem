CC = gcc
OBJ = main.o queen.o util.o
TARGET = main
CFLAGS := -Wall -w -Wformat=0

%.o:%.c 
	$(CC) -c -o $@ $< $(CFLAGS)


$(TARGET): $(OBJ)
	$(CC) $^ -o $@
	rm -f *.o *~ core
	@echo "Build complete"

run:
	./main -v