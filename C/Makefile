CC = gcc
TMP = hello.o
TMPTARGET = hello
DEPS :=
CFLAGS :=

%.o:%.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

$(TMPTARGET): $(TMP)
	echo "This is some mandatory shit"
	$(CC) $^ -o $@

clean: 
	rm *.o $(TMPTARGET)
