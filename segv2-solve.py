#!/bin/python2
# encoding: utf-8
import angr #the main framework
import claripy

def mappings():
    global proj
    return map(lambda s: (s.min_addr, s.max_addr), proj.loader.all_objects)

def gen_mem_access_violation_assert(state):
    max_addr = state.project.loader.main_object.max_addr
    max_addr += 0x1000 - (max_addr % 0x1000)
    read_addr = state.inspect.mem_read_address
    return state.solver.And(
        read_addr > max_addr,
        read_addr < max_addr + 0x1000,
        )

### add inspecter
def is_outbound_read_access(state):
    return state.solver.satisfiable(extra_constraints=[gen_mem_access_violation_assert(state)])

def check_mem_access_violation(state):
    global simgr
    print '>> Read', state.inspect.mem_read_expr, 'from', state.inspect.mem_read_address
    read_addr = state.inspect.mem_read_address
    if read_addr.symbolic:
        if is_outbound_read_access(state):
            print "[*] found memory access violation"
            # add constraint to current state (to invoke SEGV)
            state.add_constraints(gen_mem_access_violation_assert(state))
            # add constraint to all states in active stash
            for active in simgr.active:
                active.add_constraints(gen_mem_access_violation_assert(state))
            # import ipdb; ipdb.set_trace()

### ログレベルをデバッグモードに
angr.manager.l.setLevel("DEBUG")

### 解析対象を読み込む（ベタ書きでなく変数で書いてくと吉）
ELF_FILE = "./segv2"
#### 読み込むときに、CLEローダーでlibc.soを読み込まないように設定する
#### （Trueにしてもlibc.soの関数はシンボリック化されているので影響がない）
proj = angr.Project(ELF_FILE, load_options={'auto_load_libs': False})

### argv[1]
sym_arg_size = 8 # 8 bytes
argv1 = claripy.BVS('argv1', 8 * sym_arg_size)

### エントリーポイントから実行したときのステートを生成
state = proj.factory.entry_state(args=[ELF_FILE, argv1])

### check memory access violation
state.inspect.b("mem_read", when=angr.BP_BEFORE, action=check_mem_access_violation)

state.options.add("STRICT_PAGE_ACCESS")

### 生成したステートをSimulation Managerに読み込む
### （以前はPath Groupだったが、angr 7からsimgrに移行した。詳しくは angr-doc/MIGRATION.md を参照されたし）
simgr = proj.factory.simgr(state)
### Simulation Managerでシンボリック実行を開始する。
### エラーを吐くステートが出現するまでステップ実行
simgr.step(until=lambda x: len(x.errored) > 0)

if simgr.errored: ### TODO: comment
    print "[*] analysis succeeded!"
else:
    print "[!] no solutions"
    import ipdb; ipdb.set_trace()
for i, errored in enumerate(simgr.errored):
    ### argv[1]をダンプ（入力条件をダンプ）
    print "errored #%d: argv[1]: %r" % (i, errored.state.plugins['solver_engine'].eval(argv1, cast_to=str))
