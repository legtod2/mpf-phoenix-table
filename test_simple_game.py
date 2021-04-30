import os
from mpfmc.tests.FullMpfMachineTestCase import FullMachineTestCase


class TestSimpleGame(FullMachineTestCase):

    def get_machine_path(self):
        return os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir, os.pardir))

    def test_single_player_game(self):
        # Prove coins work to get credit (takes 2 coins for 1 credit and game not on free play)
        self.hit_and_release_switch("s_left_coin")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_coin")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run(.5)
        # game should be running
        self.assertIsNotNone(self.machine.game)
        self.assertEqual(1, self.machine.game.player.ball)
        # playfield expects a ball
        self.assertEqual(1, self.machine.playfield.available_balls)
        # but its not there yet (Not till passes Lane 1 - 5)
        self.assertEqual(0, self.machine.playfield.balls)
        self.advance_time_and_run(.5)
        # ball launched and goes thru lane1
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        # Now we have a ball on the playfield
        self.assertEqual(1, self.machine.playfield.balls)

        # make some points
        self.hit_and_release_switch("s_rjet")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_ljet")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_cjet")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lbdrop1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lbdrop2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lbdrop3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_rbdrop4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_rbdrop1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_rbdrop2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_rbdrop3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_rbdrop4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run()
        # Score should add up to 29,300
        self.assertEqual(29300, self.machine.game.player.score)
        self.assertEqual(2, self.machine.game.player.multiplier)
        self.release_switch_and_run("s_flipper_left", 1)

        # ball 1 drains
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        # Wait 10 sec so ball can be ejected from outhole
        self.advance_time_and_run(5) 
        # A ball is not on playfield until is passes one of the 5 top lanes
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(2, self.machine.game.player.ball)

        self.advance_time_and_run(.5)

        # ball 2 ejected and plunged to top of field
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        # Now a ball is officially on the field
        self.assertEqual(1, self.machine.playfield.balls)
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_bullseye")
        self.advance_time_and_run(1)
        # Score should add up to 64,300
        self.assertEqual(64300, self.machine.game.player.score)
        # Letters P & H Lit
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_bullseye")
        self.advance_time_and_run(1)
        # Score should add up to 119,300
        self.assertEqual(119300, self.machine.game.player.score)
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run(1)
        # Score should add up to 154,300
        self.assertEqual(154300, self.machine.game.player.score)
# Letters O & E Lit and so is extra ball lamp lit
        self.hit_and_release_switch("s_bullseye")
        self.advance_time_and_run(1)
        # Score should add up to 174,300
        self.assertEqual(174300, self.machine.game.player.score)
# Check to see if extraball awarded
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run(1)
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane2")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane3")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane4")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_lane5")
        self.advance_time_and_run(1)
        # Score should add up to 319,300
        self.assertEqual(319300, self.machine.game.player.score)

        # ball 2 drains again but shoot again lit
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        # wait for highscore display
        self.advance_time_and_run(5) # was 10
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(2, self.machine.game.player.ball)

        # and it should eject a new ball to the pf
        self.advance_time_and_run(5) 
        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        # Score should add up to 353,300
        self.assertEqual(353300, self.machine.game.player.score)
        # Prove score of spinner starts 100 and grow to 1000 when 10 bonus
        self.hit_and_release_switch("s_spinner")
        self.advance_time_and_run(.5)
        # Score should be increased by 100 pts
        self.assertEqual(353400, self.machine.game.player.score)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        self.hit_and_release_switch("s_left_outlane")
        self.advance_time_and_run(.5)
        # Should have 11 bonus pts
        self.assertEqual(11, self.machine.game.player.bonus)
        # Score should be increased by 10,000 pts
        self.assertEqual(363400, self.machine.game.player.score)
        self.hit_and_release_switch("s_spinner")
        self.advance_time_and_run(.5)
        # Score should be increased by 1000 pts not 100 pts
        self.assertEqual(364400, self.machine.game.player.score)
 
        # ball 2 drains Shoot again over
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        self.advance_time_and_run(10)
        self.assertEqual(0, self.machine.playfield.balls)
        self.assertEqual(3, self.machine.game.player.ball)
        self.advance_time_and_run(5)

        self.hit_and_release_switch("s_lane1")
        self.advance_time_and_run(.5)
        self.assertEqual(1, self.machine.playfield.balls)
 
        # ball 3 drains. game should end
        self.machine.default_platform.add_ball_to_device(self.machine.ball_devices.trough)
        self.advance_time_and_run(5)
        self.mock_event('text_input_high_score_complete')

        # enter high score
        self.assertSlideOnTop("high_score_enter_initials")
        self.hit_and_release_switch("s_flipper_right")
        self.hit_and_release_switch("s_flipper_right")
        self.hit_and_release_switch("s_start")  # C
        self.advance_time_and_run()
        self.assertTextOnTopSlide("C")
        self.hit_and_release_switch("s_flipper_right")
        self.hit_and_release_switch("s_start")  # CD
        self.advance_time_and_run()
        self.assertTextOnTopSlide("CD")
        self.hit_and_release_switch("s_flipper_right")
        self.hit_and_release_switch("s_start")  # CDE
        self.advance_time_and_run()
        self.assertTextOnTopSlide("CDE")
        self.hit_and_release_switch("s_start")
        self.advance_time_and_run()

        self.assertEventCalled('text_input_high_score_complete')
        self.advance_time_and_run(10)
        self.assertIsNone(self.machine.game)
