#!/usr/bin/env python3
from pylogix import PLC
with PLC() as comm:
    tag_name = "F50"

    tags = []
    tags.append("Mnet1.ReadData[2545].13")
    # for i in range(10,16):
    #     tags.append("F50[" + i.__str__() + "]")
    # for i in range(100,157):
    #     tags.append("F50[" + i.__str__() + "]")

    comm.IPAddress = '127.0.0.1'
    #comm.IPAddress = '169.254.1.100'
    comm.ProcessorSlot = 0
    for tag in tags:
        ret = comm.Read(tag)
        print(ret.TagName, ret.Value, ret.Status)