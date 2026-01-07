from llama_index.core.tools.tool_spec.base import BaseToolSpec

class RefundAndDiscountSpec(BaseToolSpec):

    spec_functions = ["refund_and_discount"]

    def refund_and_discount(self):
        "A tool for refund and discount "
        refund = "For discount and refund queries please contact the hotel staff. contact info: e-mail: support@grandhotel.com, telephone: +385 (0)11 111 111"
        return refund
