from smolagents.tools.base import BaseTool
import pandas as pd

class FileLoaderTool(BaseTool):
    name = "load_csv"
    description = "Loads a CSV file and returns column names and preview."

    def call(self, file_path: str) -> str:
        try:
            df = pd.read_csv(file_path)
            preview = df.head().to_string()
            column_summary = ", ".join(df.columns)
            return f"Loaded file with columns: {column_summary}\n\nPreview:\n{preview}"
        except Exception as e:
            return f"Error loading file: {e}"
