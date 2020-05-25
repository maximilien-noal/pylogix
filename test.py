#!/usr/bin/env python3
from pylogix import PLC
with PLC() as comm:
    tags = [
        ["N53[0].0", 15],
        ["N53[0].1", 15],
        ["N53[0].2", 15],
        ["N53[0].3", 15],
        ["N53[0].4", 15],
        ["N53[0].5", 15],
        ["N53[0].6", 15],
        ["N53[0].7", 15],
        ["N53[0].8", 15],
        ["N53[0].9", 15],
        ["N53[0].10", 15],
        ["N53[0].11", 15],
        ["N53[0].12", 15],
        ["N53[0].13", 15],
        ["N53[0].14", 15],
        ["N53[0].15", 15]
    ]
    comm.IPAddress = '87.100.97.130'
    comm.ProcessorSlot = 0
    rets = comm.Write(tags)

    for tag in tags:
        ret = comm.Read(tag[0])
        print(ret.TagName, ret.Value, ret.Status)

    print("End of program.")