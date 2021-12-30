#!/usr/bin/env python3
# insert colons into mac address (or remove them)


def removeColons(macAddr):
    '''Remove colons from macAddr'''
    return "".join(macAddr.split(":"))

def addColons(macAddr):
    '''Add colons to macAddr'''
    newMacAddr = []
    for x in range(0,len(macAddr),2):
        newMacAddr.append(macAddr[x:x+2])
    return ":".join(newMacAddr)


print(addColons("0123456789ABF"))
