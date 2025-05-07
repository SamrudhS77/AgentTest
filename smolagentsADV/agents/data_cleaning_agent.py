from smolagents import ManagedAgent

class DataCleaningAgent(ManagedAgent):
    description = "Analyzes and cleans data by handling nulls, fixing types, handling outliers and removing duplicates."

    def run(self, context: str) -> str:
        instructions = """
        1. Load the dataset and inspect missing values.
        2. Drop columns or rows with high null percentage.
        3. Convert numeric columns from string where needed.
        4. Remove exact duplicates.
        5. Deal with outliers as seen fit.
        6. Return a summary of what was cleaned.
        """
        return f"Begin data cleaning:\n{instructions}\n\nContext:\n{context}"
