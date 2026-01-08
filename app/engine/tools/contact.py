from pathlib import Path

from llama_index.core.tools.tool_spec.base import BaseToolSpec


class ContactSpec(BaseToolSpec):
    spec_functions = ["contact"]

    def contact(self):
        "A tool for getting contact information"
        base_dir = Path(__file__).resolve().parent  # folder gdje je ovaj .py
        path = (base_dir / "../../../data/contact/contact.txt").resolve()

        return path.read_text(encoding="utf-8")
