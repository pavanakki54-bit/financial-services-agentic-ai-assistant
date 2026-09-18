from app.tools.eligibility_tool import check_fee_waiver_eligibility


def test_eligible_fee_waiver():
    result = check_fee_waiver_eligibility(
        account_status="good_standing",
        previous_adjustments=0,
        reason_provided=True,
    )

    assert result["eligible"] is True
    assert result["requires_review"] is True


def test_account_not_in_good_standing():
    result = check_fee_waiver_eligibility(
        account_status="past_due",
        previous_adjustments=0,
        reason_provided=True,
    )

    assert result["eligible"] is False
    assert "good standing" in result["reason"].lower()


def test_previous_adjustment_requires_review():
    result = check_fee_waiver_eligibility(
        account_status="good_standing",
        previous_adjustments=1,
        reason_provided=True,
    )

    assert result["eligible"] is False
    assert result["requires_review"] is True


def test_missing_reason_is_not_eligible():
    result = check_fee_waiver_eligibility(
        account_status="good_standing",
        previous_adjustments=0,
        reason_provided=False,
    )

    assert result["eligible"] is False
    assert "reason" in result["reason"].lower()
