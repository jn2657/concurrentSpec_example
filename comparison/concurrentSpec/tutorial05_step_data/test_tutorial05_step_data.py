import unittest
from concurrentSpec.src.feature import Feature
from concurrentSpec.src.scenario import Scenario

class TestTutorial05StepData(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Feature("Tutorial05 Step Data")

    def test_some_scenario(self):
        Scenario("Some scenario")\
        .Given("a sample text loaded into the frobulator:", """
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua.
        """)\
        .When("we activate the frobulator")\
        .Then("we will find it similar to English")\
        .execute()

# Scenario: Some scenario
#      Given a sample text loaded into the frobulator:
#         """
#         Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
#         eiusmod tempor incididunt ut labore et dolore magna aliqua.
#         """
#     When we activate the frobulator
#     Then we will find it similar to English