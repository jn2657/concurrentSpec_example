from frobulator import Frobulator

class SomeScenario:

    def set_up(self):
        pass

    def tear_down(self):
        pass

    def given_a_sample_text_loaded_into_the_frobulator_(self):
        frobulator = getattr(self, "frobulator", None)
        if not frobulator:
            self.frobulator = Frobulator()
        self.frobulator.text = self.get_text()  #< STEP-DATA from self.text

    def when_we_activate_the_frobulator(self):
        self.frobulator.activate()

    def then_we_will_find_it_similar_to_english(self):
        assert "English" == self.frobulator.seems_like_language()

