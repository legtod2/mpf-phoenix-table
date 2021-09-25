import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase


class TestSimpleGame(FullMachineTestCase):

    def get_machine_path(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_single_player_game(self):
        # Let attract mode cycle once
        self.advance_time_and_run(5) #was 30
        # Service Menu
        self.hit_and_release_switch("s_door_open")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_service_enter")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_service_down")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_service_down")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_service_enter")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_service_esc")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_service_esc")
        self.advance_time_and_run(.5)
        # Allow attract mode to cycle 1 loop
        self.advance_time_and_run(5) # was 30
        self.assertIsNone(self.machine.game)
