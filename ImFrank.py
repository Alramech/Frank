from grizzly import *
import time
import ansible 

addrs=Grizzly.get_all_ids()
gs=[] 
for addr in addrs:
    g = Grizzly(addr)
    g.set_mode(ControlMode.NO_PID, DriveMode.DRIVE_COAST)
    g.limit_acceleration(142)
    g.limit_current(10)
    gs.append(g)

for g in gs:
    g.set_target(0)

while True:
    command = ansible.recv()
    print command
    if command:
        # for i in range(len(command)):
        #     if abs(command[i]) < .15:
        #         command[i] = 0
        for i in range(len(gs)):
            gs[i].set_target(100.0*command[i])
        time.sleep(0.01)