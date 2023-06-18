1. With feature name and scenario name
    - Rules: generate feature folder and scenario file
        - e.g.
            ```Python
            Feature(feature_name="Google search")
            Scenario(scenario_name="Voice search", feature_name="Google search")
            ```
        - directory structure should be:
            ```
            google_search
            └───voice_search.py
            ```

    - Feature or scenario name duplicate
        - will show warning and should not generate duplicate feature directory or scenario file
        - e.g.
            ```Python
            Feature(feature_name="Google search")
            Feature(feature_name="Google search")
            Scenario(scenario_name="Voice search", feature_name="Google search")
            Scenario(scenario_name="Voice search", feature_name="Google search")
            ```
        - warning:
            ```
            [WARNING] Feature: Google search has already existed
            [WARNING] Scenario: Voice search is already in Feature: Google search
            ```
        - directory structure should be:
            ```
            google_search
            └───voice_search.py
            ```
