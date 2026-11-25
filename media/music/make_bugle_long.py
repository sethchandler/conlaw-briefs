"""Bugle in the Fog, two-minute version (80 bpm; 8 beats = 6 s per section, 20 sections).
Arc: 0-18 s lone call | 18-60 s ghosts and heartbeat build | 60-90 s the mob (peak) |
90-102 s collapse to near silence | 102-120 s lone bugle sags, choir fades."""
import random, mido
from make_tracks import song, note, prog, bend, cc, write
random.seed(11)
mid, ev, tempo = song(80)
for ch,p in ((0,56),(1,56),(2,56),(3,47),(4,52),(5,56),(6,58),(7,48)): prog(ev,0,ch,p)
CALL = [(67,.75),(67,.25),(72,1),(76,.75),(72,.25),(67,1),(72,.5),(76,.5),(79,2)]
def call(t, ch, lag, det, vel, transpose=0):
    bend(ev, t, ch, det); tt = t+lag
    for n,d in CALL: note(ev, tt, ch, n+transpose, d*.95, vel); tt += d
for sec in range(20):
    t = sec*8
    if sec < 3:                                   # lone call
        call(t, 0, 0, 0, 95)
        if sec == 2: call(t, 1, .375, -600, 45)
    elif sec < 10:                                # build
        k = sec-3
        call(t, 0, 0, 0, 100-k*2)
        call(t, 1, .375+k*.05, -800-k*350, 55+k*2)
        if k >= 2: call(t, 2, .75+k*.08, 600+k*450, 45+k*2)
        gap = max(.45, 1-k*.08); x = t
        while x < t+8: note(ev, x, 3, 41, .3, 80+k*4); note(ev, x+gap*.3, 3, 41, .2, 60+k*3); x += gap
        if k >= 2:
            cc(ev, t, 4, 7, min(127, 50+k*10))
            for n in (55,56,58,61,62): note(ev, t, 4, n-(k//2), 8, 45+k*7)
    elif sec < 15:                                # the mob
        k = sec-10
        for ch,lag,det,v,tr in ((0,0,0,105,0),(1,.25,-2500-k*500,80,0),(2,.6,2000+k*600,75,0),(5,.9+k*.1,-4000,70,-5)):
            call(t, ch, lag, det, v, tr)
        x = t
        while x < t+8: note(ev, x, 3, 41, .2, 110); note(ev, x+.17, 3, 41, .15, 90); x += .38   # racing heart
        for r in range(16): note(ev, t+r*.5+random.uniform(-.1,.1), 9, random.choice([38,40,45]), .1, 70+random.randint(0,40))
        for n in (50,51,53,55,56,58,61,62): note(ev, t, 4, n, 8, 100)          # crowd cluster
        note(ev, t, 6, 29-k, 8, 100); note(ev, t, 7, 30+k, 8, 90)              # low brass/strings grind
        if sec == 14: note(ev, t+7, 9, 49, 2, 127); note(ev, t+7, 9, 57, 2, 127)
    elif sec < 17:                                # collapse
        if sec == 15: note(ev, t, 6, 24, 8, 70); note(ev, t, 3, 41, .3, 70)
        else: note(ev, t+4, 3, 41, .3, 45)
        cc(ev, t, 4, 7, 40); note(ev, t, 4, 55, 8, 30)
    else:                                         # lone bugle sags, fades
        k = sec-17
        call(t, 0, 0, -k*1500, 75-k*15)
        if k < 2: call(t, 1, 1.5, -3000-k*1000, 30)
        note(ev, t, 4, 55-k, 8, 35-k*10)
bend(ev, 158, 0, -7000); note(ev, 157, 0, 67, 3, 40)
write(mid, ev, tempo, 'option2_bugle_in_the_fog_2min.mid')
