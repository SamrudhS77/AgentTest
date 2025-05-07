from smolagents import ManagedAgent

class DataExplorationAgent(ManagedAgent):
    description = "Explores dataset to extract summary stats, distributions, and correlations."

    def run(self, context: str) -> str:
        instructions = """
        1. Describe numeric and categorical columns.
        2. Identify highly correlated features.
        3. Suggest possible target variables or features to remove.
        4. Recommend visualizations like histograms or box plots.
        """
        return f"Begin data exploration:\n{instructions}\n\nContext:\n{context}"
