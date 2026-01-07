from llama_index.core.tools.tool_spec.base import BaseToolSpec

class ContactSpec(BaseToolSpec):

    spec_functions = ["contact"]

    def contact(self):
        "A tool for getting contact information"
        contact = "contact tool"
        return contact
