import adafruit_midi
import usb_midi
from adafruit_midi.control_change import ControlChange
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
from adafruit_midi.pitch_bend import PitchBend
from adafruit_midi.program_change import ProgramChange
from adafruit_midi.start import Start
from adafruit_midi.stop import Stop
from kmk.modules.midi import *
from kmk.keys import make_argumented_key

default_velocity = 64

class velocityValidator:
    def __init__(self, velocity=10, channel=None):
        self.velocity = velocity
        self.channel = channel
    
class midiNoteValidator:
    def __init__(self, note=69, velocity=default_velocity, channel=None):
        self.note = note
        self.velocity = velocity
        self.channel = channel


class MIDI(MidiKeys):
    def __init__(self):
        super().__init__()
        make_argumented_key(
            names=('MIDI_VEL',),
            validator=velocityValidator,
            on_press=self.velocity_change,
        )
        make_argumented_key(
            names=('MIDI_VELR',),
            validator=velocityValidator,
            on_press=self.velocity_change,
        )
        make_argumented_key(
            names=('NOTE',),
            validator=midiNoteValidator,
            on_press=self.note_on,
            on_release=self.note_off,
        )
        try:
            self.midi = adafruit_midi.MIDI(midi_in=usb_midi.ports[0],midi_out=usb_midi.ports[1], out_channel=0)
        except IndexError:
            self.midi = None
            # if debug_enabled:
            print('No midi device found.')
    
    def velocity_change(self,key, keyboard, *args, **kwargs):
        global default_velocity
        delta = key.meta.velocity
        default_velocity = (default_velocity + delta)
        default_velocity = 0 if default_velocity < 0 else default_velocity
        default_velocity = 127 if default_velocity > 127 else default_velocity
    
    def note_on(self, key, keyboard, *args, **kwargs):
        self.send(NoteOn(key.meta.note, default_velocity, channel=key.meta.channel))

    def after_matrix_scan(self, keyboard):
        if self.midi:
            message = self.midi.receive()
            if message:
                print(f'====>>> midi message:{message}')
        return None