from smolagents.tools.base import BaseTool
import io
import contextlib


class PythonExecutionTool(BaseTool):
    name = "python_executor"
    description = "Executes multi line Python code for data processing and/or plotting"

    def call(self, code: str) -> str:
        local_vars = {}
        output = io.StringIO()
        try:
            with contextlib.redirect_stdout(output):
                exec(code, {}, local_vars)
            return output.getvalue() or "Code executed sucessfully."
        except Exception as e:
            return f"Execution error: {e}"
            