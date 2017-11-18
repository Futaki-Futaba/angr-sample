angr sample
====

environment
----
```
% pip2 list --format=legacy | grep "angr "
angr (7.7.9.21)
```


samples
----
* `./sample`
    * reads user input from __stdin__
* `./segv`
    * reads user input from __argv__
    * find argv[1] SEGVs `./segv`


compile
----
```
make
```


test
----
```
make test
```


result
----
### sample
runtime: 5 sec

```
% ./sample-solve.py 
WARNING | 2017-10-28 03:13:07,095 | cle.loader | The main binary is a position-independent executable. It is being loaded with a base address of 0x400000.
DEBUG   | 2017-10-28 03:13:07,120 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,121 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,141 | angr.manager | Round 1: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,142 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,341 | angr.manager | Round 2: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,341 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,409 | angr.manager | Round 3: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,409 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,426 | angr.manager | Round 4: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,426 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,438 | angr.manager | Round 5: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,438 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,455 | angr.manager | Round 6: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,455 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,468 | angr.manager | Round 7: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,468 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,480 | angr.manager | Round 8: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,480 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,511 | angr.manager | Round 9: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,511 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,521 | angr.manager | Round 10: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,521 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,539 | angr.manager | Round 11: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,539 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,559 | angr.manager | Round 12: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,559 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,576 | angr.manager | Round 13: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,576 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,597 | angr.manager | Round 14: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,597 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,605 | angr.manager | Round 15: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:07,605 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:09,998 | angr.manager | Round 16: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:09,999 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,010 | angr.manager | Round 17: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,011 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,019 | angr.manager | Round 18: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,019 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,529 | angr.manager | Round 19: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,529 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-10-28 03:13:10,583 | angr.manager | Round 20: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,583 | angr.manager | Round 0: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,613 | angr.manager | Round 21: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,613 | angr.manager | Round 0: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,636 | angr.manager | Round 22: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,637 | angr.manager | Round 0: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,653 | angr.manager | Round 23: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,653 | angr.manager | Round 0: stepping <SimulationManager with 2 active>
DEBUG   | 2017-10-28 03:13:10,676 | angr.manager | Out of states in stash active
DEBUG   | 2017-10-28 03:13:10,676 | angr.manager | Out of states in stash active
[*] analysis succeeded!
#0 stdin: 'flag{angr_makes_it_easy}\x00 \x80\x10\x00\x80\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
#0 stdout: 'correct\n'
```

### segv
runtime: 30 sec

```
% ./segv-solve.py
WARNING | 2017-11-19 04:35:22,336 | cle.loader | The main binary is a position-independent executable. It is being loaded with a base address of 0x400000.
DEBUG   | 2017-11-19 04:35:22,361 | angr.manager | Round 0: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,377 | angr.manager | Round 1: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,571 | angr.manager | Round 2: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,599 | angr.manager | Round 3: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,617 | angr.manager | Round 4: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,628 | angr.manager | Round 5: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,644 | angr.manager | Round 6: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,657 | angr.manager | Round 7: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,667 | angr.manager | Round 8: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,698 | angr.manager | Round 9: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,708 | angr.manager | Round 10: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,725 | angr.manager | Round 11: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,743 | angr.manager | Round 12: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,760 | angr.manager | Round 13: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,784 | angr.manager | Round 14: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,797 | angr.manager | Round 15: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:22,805 | angr.manager | Round 16: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:23,046 | angr.manager | Round 17: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:23,160 | angr.manager | Round 18: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:23,170 | angr.manager | Round 19: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:23,253 | angr.manager | Round 20: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:23,262 | angr.manager | Round 21: stepping <SimulationManager with 1 active>
DEBUG   | 2017-11-19 04:35:24,862 | angr.manager | Round 22: stepping <SimulationManager with 2 active>
DEBUG   | 2017-11-19 04:35:26,581 | angr.manager | Round 23: stepping <SimulationManager with 3 active>
DEBUG   | 2017-11-19 04:35:28,322 | angr.manager | Round 24: stepping <SimulationManager with 4 active>
DEBUG   | 2017-11-19 04:35:30,018 | angr.manager | Round 25: stepping <SimulationManager with 5 active>
DEBUG   | 2017-11-19 04:35:31,700 | angr.manager | Round 26: stepping <SimulationManager with 6 active>
DEBUG   | 2017-11-19 04:35:33,535 | angr.manager | Round 27: stepping <SimulationManager with 7 active>
DEBUG   | 2017-11-19 04:35:35,331 | angr.manager | Round 28: stepping <SimulationManager with 7 active, 1 deadended>
DEBUG   | 2017-11-19 04:35:37,055 | angr.manager | Round 29: stepping <SimulationManager with 7 active, 2 deadended>
DEBUG   | 2017-11-19 04:35:38,767 | angr.manager | Round 30: stepping <SimulationManager with 7 active, 3 deadended>
DEBUG   | 2017-11-19 04:35:40,474 | angr.manager | Round 31: stepping <SimulationManager with 7 active, 4 deadended>
DEBUG   | 2017-11-19 04:35:42,065 | angr.manager | Round 32: stepping <SimulationManager with 7 active, 5 deadended>
DEBUG   | 2017-11-19 04:35:42,134 | angr.manager | Until function returned true
[*] analysis succeeded!
errored #0: argv[1]: '100\xf0\x13e\xc0\xbc'
```