human_years = 10
human_years = 1
human_years = 2
CAT_ONE_YEAR = 15
CAT_TWO_YEARS = 9
CAT_MORE_YEARS = 4

DOG_ONE_YEAR = 15
DOG_TWO_YEARS = 9
DOG_MORE_YEARS = 5

if human_years == 1:
    cat_years = CAT_ONE_YEAR
    dog_years = DOG_ONE_YEAR
elif human_years == 2:
    cat_years = CAT_ONE_YEAR + CAT_TWO_YEARS
    dog_years = DOG_ONE_YEAR + DOG_TWO_YEARS
elif human_years > 2:
    
    cat_years = CAT_ONE_YEAR + CAT_TWO_YEARS + (human_years - 2) * CAT_MORE_YEARS
    dog_years = DOG_ONE_YEAR + DOG_TWO_YEARS + (human_years - 2)* DOG_MORE_YEARS

print(human_years, cat_years, dog_years)