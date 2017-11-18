BIN := sample segv

all: $(BIN)
	@### Do Nothing 

%: %.c
	gcc -o $@ $^

test:
	@echo "### correct input"
	echo -n "flag{angr_makes_it_easy}" | ./sample
	@echo "### wrong input"
	echo -n "flag{}" | ./sample