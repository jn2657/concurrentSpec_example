import unittest
from concurrentSpec.src.feature import Feature
from concurrentSpec.src.scenario import Scenario
from concurrentSpec.src.background import Background

class TestTutorial09Background(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Feature("Tutorial09 Background")
        Background("Ninja fight setup")\
        .Given("the ninja encounters another opponent")

    def test_weaker_opponent(self):
        Scenario("Weaker opponent")\
        .Given("the ninja has a third level black-belt")\
        .When("attacked by a samurai")\
        .Then("the ninja should engage the opponent")\
        .execute()

    def test_stronger_opponent(self):
        Scenario("Stronger opponent")\
        .Given("the ninja has a second level black-belt")\
        .When("attacked by a Chuck Norris")\
        .Then("the ninja should run for his life")\
        .execute()