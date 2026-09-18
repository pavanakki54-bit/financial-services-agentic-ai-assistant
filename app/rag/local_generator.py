class LocalGroundedGenerator:
    def generate(self, prompt: str) -> str:
        prompt_lower = prompt.lower()

        if "60 days" in prompt_lower and "dispute" in prompt_lower:
            return (
                "Eligible transaction disputes should be reported "
                "within 60 days of the transaction appearing on the statement."
            )

        if "fee waiver" in prompt_lower or "fee_policy.md" in prompt_lower:
            return (
                "Fee waiver eligibility depends on the applicable policy "
                "and account circumstances. Approval is not guaranteed."
            )

        return (
            "The available policy information does not provide enough "
            "information to answer this question."
        )
