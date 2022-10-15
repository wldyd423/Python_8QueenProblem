CC = gcc
OBJ = main.o queen.o
TARGET = main
CFLAGS :=

%.o:%.c 
	$(CC) -c -o $@ $< $(CFLAGS)


$(TARGET): $(OBJ)
	$(CC) $^ -o $@
	rm -f *.o *~ core
	@echo "Build complete"

