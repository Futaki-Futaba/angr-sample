#!/bin/python2
# encoding: utf-8
import angr #the main framework
import claripy


### ログレベルをデバッグモードに
angr.manager.l.setLevel("DEBUG")

### デバッグモード
DEBUG = False

### 解析対象を読み込む（ベタ書きでなく変数で書いてくと吉）
ELF_FILE = "./segv"
#### 読み込むときに、CLEローダーでlibc.soを読み込まないように設定する
#### （Trueにしてもlibc.soの関数はシンボリック化されているので影響がない）
proj = angr.Project(ELF_FILE, load_options={'auto_load_libs': False})

### argv[1]
sym_arg_size = 8 # 8 bytes
argv1 = claripy.BVS('argv1', 8 * sym_arg_size)

### エントリーポイントから実行したときのステートを生成
state = proj.factory.entry_state(args=[ELF_FILE, argv1])

state.options.add("STRICT_PAGE_ACCESS")

### 生成したステートをSimulation Managerに読み込む
### （以前はPath Groupだったが、angr 7からsimgrに移行した。詳しくは angr-doc/MIGRATION.md を参照されたし）
simgr = proj.factory.simgr(state)
### Simulation Managerでシンボリック実行を開始する。
### エラーを吐くステートが出現するまでステップ実行
simgr.step(until=lambda x: len(x.errored) > 0)

if simgr.errored: ### TODO
    print "[*] analysis succeeded!"
else:
    print "[!] no solutions"
if hasattr(simgr, 'found'):
    for i, found in enumerate(simgr.found):
        ### argv[1]をダンプ（入力条件をダンプ）
        print "found #%d: argv[1]: %r" % (i, found.se.eval(argv1))
for i, errored in enumerate(simgr.errored):
    if DEBUG:
        print "error: %r" % (errored.error)
        for k, v in vars(errored.error).items():
            print "\t%s: %r" % (k, v)
        print ""
        print "state: %r" % (errored.state)
        for k, v in vars(errored.state).items():
            if k == "plugins":
                print "\t%s:" % (k)
                for k2, v2 in v.items(): # type of errored.state.plugins is dictinary
                    print "\t\t%s: %r" % (k2, v2)
                    if k2 == "solver_engine":
                        print "\t\t\t%s" % filter(lambda x: not x.startswith('_'), dir(v2))
            else:
                print "\t%s: %r" % (k, v)
        print ""
        print "traceback: %r" % (errored.traceback)
        print "\ttb_frame: %r" % (errored.traceback.tb_frame)
        print "\ttb_fasti: %r" % (errored.traceback.tb_lasti)
        print "\ttb_lineno: %r" % (errored.traceback.tb_lineno)
        print "\ttb_next: %r" % (errored.traceback.tb_next)
        print ""
    ### argv[1]をダンプ（入力条件をダンプ）
    print "errored #%d: argv[1]: %r" % (i, errored.state.plugins['solver_engine'].eval(argv1, cast_to=str))
