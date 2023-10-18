import m5
from m5.objects import *
system = System()
system.clk_domain=SrcClockDomain()
system.clk_domain.clock='1GHz'
system.clk_domain.voltage_domain=VoltageDomain()
system.mem_mode='timing'
system.mem_ranges=[AddrRange('512MB')]
system.cpu=X86TimingSimpleCPU()
system.membus=SystemXBar()
system.l2bus = L2XBar()

class L1i(Cache):
    size='16kB'
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20
    def __init__(self,cpu,bus):
        super().__init__()
        self.connect(cpu,bus)
    def connect(self,cpu,bus):
        self.cpu_side=cpu.icache_port
        self.mem_side=bus.cpu_side_ports
class L1d(Cache):
    size='16kB'
    assoc = 2
    tag_latency = 2
    data_latency = 2
    response_latency = 2
    mshrs = 4
    tgts_per_mshr = 20
    def __init__(self,cpu,bus):
        super().__init__()
        self.connect(cpu,bus)
    def connect(self,cpu,bus):
        self.cpu_side=cpu.dcache_port
        self.mem_side=bus.cpu_side_ports

class L2(Cache):
    size='1024kB'
    assoc = 4
    tag_latency = 10
    data_latency = 10
    response_latency = 10
    mshrs = 4
    tgts_per_mshr = 20
    def __init__(self,bus1,bus2):
        super().__init__()
        self.connect(bus1,bus2)
    def connect(self,bus1,bus2):
        self.cpu_side=bus1.mem_side_ports
        self.mem_side=bus2.cpu_side_ports

system.cpu.icache=L1i(system.cpu,system.l2bus)
system.cpu.dcache=L1d(system.cpu,system.l2bus)
system.l2cache=L2(system.l2bus,system.membus)

system.cpu.createInterruptController()
system.cpu.interrupts[0].pio=system.membus.mem_side_ports
system.cpu.interrupts[0].int_requestor=system.membus.cpu_side_ports
system.cpu.interrupts[0].int_responder=system.membus.mem_side_ports
system.system_port=system.membus.cpu_side_ports

system.mem_ctrl=MemCtrl()
system.mem_ctrl.dram=DDR3_1600_8x8()
system.mem_ctrl.dram.range=system.mem_ranges[0]
system.mem_ctrl.port=system.membus.mem_side_ports

binary = 'configs/ca/assignment-1/qsortbinary'
system.workload=SEWorkload.init_compatible(binary)
process=Process()
process.cmd=[binary,'configs/ca/assignment-1/input_small.dat']
system.cpu.workload=process
system.cpu.createThreads()

root=Root(full_system=False,system=system)
m5.instantiate()
print("Beginning simulation!")
exit_event = m5.simulate()
print('Exiting @ tick {} because {}'.format(m5.curTick(), exit_event.getCause()))