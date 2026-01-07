from llama_index.core.tools.tool_spec.base import BaseToolSpec

class FallbackToHumanSpec(BaseToolSpec):

    spec_functions = ["fallback_to_human"]

    def fallback_to_human(self):
        "A tool when user is asking to speak with a human agent. Always call this tool when user wants to speak to a human."
        contact = "fallback_to_human tool"
        return {
            "result": contact,
            "instructions": "NEVER SAY THAT YOU HAVE CONNECTED THE USER TO THE AGENT. Instruct the user to contact us via website."
        }
