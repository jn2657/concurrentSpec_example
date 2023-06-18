from blender import Blender
from hamcrest import assert_that, equal_to

class UseBlenderWithThing:

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def given_i_put_thing_in_a_blender(self, thing):
        self.blender = Blender()
        self.blender.add(thing)

    def when_i_switch_the_blender_on(self):
        self.blender.switch_on()

    def then_it_should_transform_into_other_thing_(self, other_thing):
        assert_that(self.blender.result, equal_to(other_thing))
        # assert self.blender.result == other_thing

