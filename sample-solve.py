#!/bin/python2
# encoding: utf-8
import angr #the main framework

### ログレベルをデバッグモードに
angr.manager.l.setLevel("DEBUG")

### 解析対象を読み込む（ベタ書きでなく変数で書いてくと吉）
ELF_FILE = "./sample"
#### 読み込むときに、CLEローダーでlibc.soを読み込まないように設定する
#### （Trueにしてもlibc.soの関数はシンボリック化されているので影響がない）
proj = angr.Project(ELF_FILE, load_options={'auto_load_libs': False}) 

### エントリーポイントから実行したときのステートを生成
state = proj.factory.entry_state(args=[ELF_FILE])
### 生成したステートをSimulation Managerに読み込む
### （以前はPath Groupだったが、angr 7からsimgrに移行した。詳しくは angr-doc/MIGRATION.md を参照されたし）
simgr = proj.factory.simgr(state)
### Simulation Managerでシンボリック実行を開始する。
### findはお目当ての実行条件を教える。
### この条件を満たすステート至ると、active stash（探索中のステート）はfound stash（探索に成功したステート）に移行する
### findの引数はラムダ式でもアドレスのlist, tupleでもよい
simgr.explore(find=lambda p: "correct" in p.state.posix.dumps(1))

if simgr.found: ### findを満たすstashがsimgr.foundに入る。見つからなかったらここは空になる。
    print "[*] analysis succeeded!"
else:
    print "[!] no solutions"
for i, found in enumerate(simgr.found):
    ### 標準入力をダンプ（入力条件をダンプ）
    print "#%d stdin: %r" % (i, found.state.posix.dumps(0)) 
    ### そのときの標準出力をダンプ
    print "#%d stdout: %r" % (i, found.state.posix.dumps(1)) 
