BIN := sample

all: $(BIN)
	gcc -o $^ $^.c 

test:
	@echo "### correct input"
	echo -n "flag{angr_makes_it_easy}" | ./$(BIN)
	@echo "### wrong input"
	echo -n "flag{}" | ./$(BIN)