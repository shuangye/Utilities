#!/usr/bin/python3

"""
Output:
[14:43:56] Timing 2.0/3.0
[14:43:57] Timing 1.0/3.0
[14:43:58] Timing 0.0/5.0
[14:43:58] Do work sequence 1
[14:43:59] Timing 4.0/5.0
[14:44:00] Timing 3.0/5.0
[14:44:01] Timing 2.0/5.0
[14:44:03] Timing 1.0/5.0
[14:44:04] Timing 0.0/5.0
[14:44:04] Do work sequence 2
[14:44:05] Timing 4.0/5.0
[14:44:06] Timing 3.0/5.0
[14:44:07] Timing 2.0/5.0
[14:44:08] Timing 1.0/5.0
[14:44:09] Timing 0.0/5.0
[14:44:09] Do work sequence 3
"""

import time
import datetime

g_timerResolution                = 0.2      # in seconds
g_timerFiredCount                = 0
g_initialDelayFires              = 15       # start offset. 3s
g_uiUpdateFires                  = 5        # * g_timerResolution = 1s
g_timerFiresPerInterval          = 25       # work every 5s
g_workSequence                   = 0


def currentTimestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def timerHandler():
    global g_timerFiredCount, g_workSequence
    g_timerFiredCount += 1
    isInInitialDelay = g_timerFiredCount < g_initialDelayFires
    if g_timerFiredCount % g_uiUpdateFires == 0:
        if isInInitialDelay:
            fires = g_initialDelayFires
            remainingFires = fires - g_timerFiredCount % fires
        else:
            fires = g_timerFiresPerInterval
            remainingFires = fires - (g_timerFiredCount - g_initialDelayFires) % fires
        if remainingFires == fires: remainingFires = 0   # if want to be 0. Depends on whichever is reasonable.
        remainingTime = remainingFires * g_timerResolution
        print('[{}] Timing {}/{}'.format(currentTimestamp(), remainingTime, fires * g_timerResolution, isInInitialDelay))
    if isInInitialDelay:
        return
    if (g_timerFiredCount - g_initialDelayFires) % g_timerFiresPerInterval == 0:
        g_workSequence += 1
        print("[{}] Do work sequence {}".format(currentTimestamp(), g_workSequence))

def startTimer(interval):
    while True:
        timerHandler()
        time.sleep(interval)

def main():
    startTimer(g_timerResolution)

if __name__ == '__main__':
    main()
