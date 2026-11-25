"""Three 'Distorted Americana' sketches for a Trump v. United States video. Render with fluidsynth."""
import random, mido
TPB = 480
def song(tempo_bpm):
    mid = mido.MidiFile(ticks_per_beat=TPB); events = []
    return mid, events, mido.bpm2tempo(tempo_bpm)
def note(ev, t, ch, n, dur, vel):
    ev.append((int(t*TPB), mido.Message('note_on', channel=ch, note=n, velocity=max(1,min(127,vel)))))
    ev.append((int((t+dur)*TPB), mido.Message('note_off', channel=ch, note=n, velocity=0)))
def prog(ev, t, ch, p): ev.append((int(t*TPB), mido.Message('program_change', channel=ch, program=p)))
def bend(ev, t, ch, v): ev.append((int(t*TPB), mido.Message('pitchwheel', channel=ch, pitch=max(-8191,min(8191,int(v))))))
def cc(ev, t, ch, c, v): ev.append((int(t*TPB), mido.Message('control_change', channel=ch, control=c, value=v)))
def write(mid, ev, tempo, name):
    tr = mido.MidiTrack(); mid.tracks.append(tr); tr.append(mido.MetaMessage('set_tempo', tempo=tempo))
    last = 0
    for t, m in sorted(ev, key=lambda x: (x[0], x[1].type == 'note_on')):
        tr.append(m.copy(time=t-last)); last = t
    mid.save(name)
random.seed(7)
# Yankee Doodle (public domain), in beats
YD = [(72,.5),(72,.5),(74,.5),(76,.5),(72,.5),(76,.5),(74,1),(72,.5),(72,.5),(74,.5),(76,.5),(72,1),(71,1),
      (72,.5),(72,.5),(74,.5),(76,.5),(77,.5),(76,.5),(74,.5),(72,.5),(71,.5),(67,.5),(69,.5),(71,.5),(72,1),(72,1)]

# 1. The Fife Unravels: fife tune detunes, snare loses time, low drone swallows it.
mid, ev, tempo = song(112)
prog(ev,0,0,72); prog(ev,0,1,58); prog(ev,0,2,48)
t = 0
for rep in range(5):
    drift = rep/4
    for i,(n,d) in enumerate(YD):
        bend(ev, t, 0, random.uniform(-1,1)*2200*drift + (-1200*drift if i%5==0 else 0))
        if not (rep>=3 and random.random()<0.25*rep/4):           # notes start dropping out
            note(ev, t+random.uniform(0,0.12)*drift, 0, n+(12 if rep==4 and i%7==0 else 0), d*0.9, 95-8*rep)
        t += d
    for b in range(16):                                           # snare march, jitter grows
        for s in (0,.5,.75):
            if random.random() > 0.2*drift:
                note(ev, (t-16)+b+s+random.uniform(-.2,.2)*drift, 9, 38, .1, 80+int(30*drift)+(15 if s==0 else 0))
    if rep>=2:
        note(ev, t-16, 1, 36-rep, 16, 50+15*rep); note(ev, t-16, 2, 37+rep, 16, 40+12*rep)  # dissonant drone
note(ev, t, 1, 24, 6, 110); note(ev, t, 9, 49, 4, 120)
write(mid, ev, tempo, 'option1_fife_unravels.mid')

# 2. Bugle in the Fog: original bugle call echoed by detuned ghosts; heartbeat timpani speeds up.
mid, ev, tempo = song(80)
for ch,p in ((0,56),(1,56),(2,56),(3,47),(4,52)): prog(ev,0,ch,p)
CALL = [(67,.75),(67,.25),(72,1),(76,.75),(72,.25),(67,1),(72,.5),(76,.5),(79,2)]
t = 0
for rep in range(6):
    for ch,lag,detune,vel in ((0,0,0,100),(1,.375+rep*.06,-900-rep*400,60),(2,.75+rep*.1,700+rep*500,45)):
        if ch>0 and rep==0: continue
        bend(ev, t, ch, detune); tt = t+lag
        for n,d in CALL: note(ev, tt, ch, n, d*.95, vel-rep*5); tt += d
    beats = 8
    gap = max(.35, 1-rep*.13)                                     # heartbeat accelerates
    x = t
    while x < t+beats: note(ev, x, 3, 41, .3, 90+rep*5); note(ev, x+gap*.3, 3, 41, .2, 70); x += gap
    if rep>=2:                                                    # crowd: clustered choir swell
        cc(ev,t,4,7,40+rep*15)
        for n in (55,56,58,61,62): note(ev, t, 4, n-rep, beats, 50+rep*10)
    t += beats
note(ev, t+1, 0, 79, 4, 70); bend(ev, t+2, 0, -6000)
write(mid, ev, tempo, 'option2_bugle_in_the_fog.mid')

# 3. Broken March: brass march whose bass slips a half step off key; ends in silence and one piano chord.
mid, ev, tempo = song(120)
for ch,p in ((0,61),(1,58),(2,0)): prog(ev,0,ch,p)
MEL = [(72,1),(76,1),(79,1.5),(77,.5),(76,1),(74,1),(72,2),(74,1),(76,1),(77,1),(74,1),(79,2),(67,2)]
BASS = [48,43,48,43, 50,43,48,43]
t = 0
for rep in range(5):
    shift = 1 if rep>=2 else 0                                    # bass slides into another key
    for i,(n,d) in enumerate(MEL):
        off = random.choice([0,0,1,-1,6]) if rep>=3 and random.random()<.3 else 0
        note(ev, t, 0, n+off, d*.9, 100); t += d
    for b in range(16):
        note(ev, t-16+b, 1, BASS[b%8]-shift-(rep>=4)*6, .8, 100)
        if not (rep>=2 and b%3==2): note(ev, t-16+b+(.5 if rep>=3 and b%4==1 else 0), 9, 38, .1, 95)
        if rep>=3 and random.random()<.3: note(ev, t-16+b+.33, 9, 49, .5, 115)   # off-beat crashes
t += 2                                                            # silence
for n in (36,48,51,54,60): note(ev, t, 2, n, 6, 105)              # diminished chord: the dissent
write(mid, ev, tempo, 'option3_broken_march.mid')
