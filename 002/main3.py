#day 2
current_age_years = int(input("Enter your age in years: "))

#calculate what remain to live
remain_years = 90 - current_age_years
remain_days = remain_years * 365
remain_weeks = remain_years * 52
remain_months = remain_years * 12

#Print resut
print(f"You can live more {remain_days} days, or {remain_weeks} weeks, or {remain_months} months")
