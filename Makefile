BIN := sample segv segv2

all: $(BIN)
	@### Do Nothing 

%: %.c
	gcc -o $@ $^

clean:
	rm $(BIN)

test:
	@echo "### correct input"
	echo -n "flag{angr_makes_it_easy}" | ./sample
	@echo "### wrong input"
	echo -n "flag{}" | ./sample