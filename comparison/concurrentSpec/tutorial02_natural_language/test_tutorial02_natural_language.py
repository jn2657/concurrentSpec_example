import unittest
from concurrentSpec.src.feature import Feature
from concurrentSpec.src.scenario import Scenario

class TestTutorial02NaturalLanguage(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Feature("Tutorial02 Natural Language", """

        In order to increase the ninja survival rate,
        As a ninja commander
        I want my ninjas to decide whether to take on an opponent
        based on their skill levels.
        
        """)

    def test_weaker_opponent(self):
        Scenario("Weaker opponent")\
        .Given("the ninja has a third level black-belt")\
        .When("attacked by a samurai")\
        .Then("the ninja should engage the opponent")\
        .execute()

    def test_stronger_opponent(self):
        Scenario("Stronger opponent")\
        .Given("the ninja has a third level black-belt")\
        .When("attacked by a Chuck Norris")\
        .Then("the ninja should run for his life")\
        .execute()