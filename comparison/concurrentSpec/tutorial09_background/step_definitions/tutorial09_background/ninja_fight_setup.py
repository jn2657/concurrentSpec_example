class NinjaFightSetup:

    def set_up(self):
        pass

    def given_the_ninja_encounters_another_opponent(self):
        # -- SETUP/TEARDOWN:
        if hasattr(self, "ninja_fight"):
            # -- VERIFY: Double-call does not occur.
            assert self.ninja_fight != None
        self.ninja_fight = None

