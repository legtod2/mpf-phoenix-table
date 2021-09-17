from mpf.core.mode import Mode
from mpf.core.delays import DelayManager
from mpf.core.utility_functions import Util

class Count(Mode):

    def mode_start(self, **kwargs):
        self.bonus_value = 1000
        self.count_down = self.player.bonus
        self.machine.events.post("bonus_code_starting_value_" + str(self.count_down))
        self.prepare_bonus()

    def prepare_bonus(self):
        if self.machine.game.tilted:
            self.machine.events.post("bonus_code_tilt_stop")
            self.player.bonus_multiplier = 1     # loose BM on tilt
            self.stop()
            return
        self.bonus_step()
        
    def bonus_step(self, future=None, **kwargs):
        self.machine.events.post("bonus_code_step")   #use this for sound player
        if self.count_down > 0:
            if self.count_down >= 10 and self.count_down <= 19:
                self.machine.lights['l_bonus10'].on()
            else:
                self.machine.lights['l_bonus10'].off()
        
        if self.count_down > 0:
            if self.count_down >= 20 and self.count_down <= 29:
                self.machine.lights['l_bonus20'].on()
            else:
                self.machine.lights['l_bonus20'].off()
            
        if self.count_down % 10 != 0 :
            self.machine.lights['l_bonus' + str(self.count_down % 10)].on()
        
        if self.count_down > 0:
            self.delay.add(ms=500, callback=self.do_bonus_step)
        else:
            self.bonus_pause()        

    def do_bonus_step(self):
        self.machine.events.post("bonus_code_countdown_" + str(self.count_down))
        self.player.score += self.bonus_value * self.player.bonus_multiplier
        if self.count_down % 10 != 0:
            self.machine.lights['l_bonus' + str(self.count_down % 10)].off()
            self.machine.events.post("play_1000_pts")
        self.count_down -= 1 
        self.bonus_step()
        
    def bonus_pause(self):
        self.delay.add(ms=1000, callback=self.bonus_done)

    def bonus_done(self):
        self.machine.events.post("bonus_complete")
        self.player.bonus = 0
        if self.player.keepBM == 0:  # this means bonus mode has been called from ball_drain
            self.player.bonus_multiplier = 1  # don't want to reset if called from bullseye
        self.stop()
