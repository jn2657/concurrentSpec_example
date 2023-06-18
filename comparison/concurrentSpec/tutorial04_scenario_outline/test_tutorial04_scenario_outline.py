import unittest
from concurrentSpec.src.feature import Feature
from concurrentSpec.src.scenario_outline import ScenarioOutline

class TestTutorial04ScenarioOutline(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        Feature("Tutorial04 Scenario Outline")

    def test_using_blender(self):
        ScenarioOutline("Use Blender with <thing>")\
        .Given("I put '<thing>' in a blender")\
        .When("I switch the blender on")\
        .Then("it should transform into '<other thing>'")\
        .WithExamples("""
            | thing         | other thing |
            | Red Tree Frog | mush        |
            | apples        | apple juice |
            | iPhone        | toxic waste |
            | Galaxy Nexus  | toxic waste |
        """)\
        .execute()
