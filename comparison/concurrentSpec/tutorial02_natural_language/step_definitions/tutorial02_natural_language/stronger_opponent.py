from ninja_fight import NinjaFight
from hamcrest import assert_that, equal_to

class StrongerOpponent:

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def given_the_ninja_has_a_third_level_black_belt(self):
        self.ninja_fight = NinjaFight("third level black-belt")

    def when_attacked_by_a_chuck_norris(self):
        self.ninja_fight.opponent = "Chuck Norris"

    def then_the_ninja_should_run_for_his_life(self):
        assert_that("run for his life", equal_to(self.ninja_fight.decision()))
        # assert "run for his life" == self.ninja_fight.decision()

