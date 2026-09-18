def check_fee_waiver_eligibility(
    account_status: str,
    previous_adjustments: int,
    reason_provided: bool,
) -> dict:
    if account_status.lower() != "good_standing":
        return {
            "eligible": False,
            "reason": "Account must be in good standing.",
            "requires_review": True,
        }

    if previous_adjustments > 0:
        return {
            "eligible": False,
            "reason": "Previous fee adjustments require additional review.",
            "requires_review": True,
        }

    if not reason_provided:
        return {
            "eligible": False,
            "reason": "A reason for the fee waiver request is required.",
            "requires_review": True,
        }

    return {
        "eligible": True,
        "reason": "The request meets the preliminary eligibility criteria.",
        "requires_review": True,
    }
