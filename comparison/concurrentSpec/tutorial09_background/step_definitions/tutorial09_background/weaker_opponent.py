from ninja_fight import NinjaFight
from hamcrest import assert_that, equal_to

class WeakerOpponent:

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def given_the_ninja_has_a_third_level_black_belt(self):
        self.ninja_fight = NinjaFight("third level black-belt")

    def when_attacked_by_a_samurai(self):
        self.ninja_fight.opponent = "samurai"

    def then_the_ninja_should_engage_the_opponent(self):
        assert_that("engage the opponent", equal_to(self.ninja_fight.decision()))
        # assert "engage the opponent" == self.ninja_fight.decision()

