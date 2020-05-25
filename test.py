#!/usr/bin/env python3
from pylogix import PLC
with PLC() as comm:
    tags = [
        "F20[200]", "F20[201]", "F20[202]", "F34[0]", "F34[202]", "F34[3]",
        "N13[0].15", "N13[0].9", "N13[12].1", "N13[13].1", "N13[3].1",
        "N13[5].1", "N23[200].0", "N23[200].2", "N23[200].5", "N23[200].8"
    ]
    comm.IPAddress = '87.100.97.130'
    #comm.IPAddress = '169.254.1.100'
    comm.ProcessorSlot = 0
    #for tag in tags:
    #retWrite = comm.Write("N52[12]", 0)
    rets = comm.Read(tags)
    for ret in rets:
        print(ret.TagName, ret.Value, ret.Status)

    print("fini")