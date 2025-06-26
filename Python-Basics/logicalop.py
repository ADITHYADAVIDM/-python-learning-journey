has_high_income = True
has_good_credit = False
has_criminal_record = False

if has_high_income or has_good_credit:
    print("Eligible for loan")

if has_criminal_record and not(has_good_credit):
    print("Not eligible for loan")