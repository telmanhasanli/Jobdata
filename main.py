#!/usr/bin/env python3

import sys  # Used to get command-line arguments
import csv

# Constants
EXPERIENCE = [
    'Less than 1 year',
    '1 year to less than 3 years',
    '3 years to less than 5 years',
    '5 years to less than 8 years',
    '8 years or more'
]

PROVINCE_NAMES = [
    'ontario', 'alberta', 'british columbia',
    'manitoba', 'new brunswick', 'newfoundland and labrador',
    'nova scotia', 'prince edward island', 'quebec',
    'saskatchewan',
    'northwest territories', 'nunavut', 'yukon', 'canada'
]

def main(argv):
    # Parse command-line arguments
    experience = argv[1]
    statistics = argv[2]
    province = argv[3]

    # Validate experience input
    if experience not in ['1', '2', '3', '4', '5']:
        print("Invalid input, only accepts arguments of 1, 2, 3, 4, 5", file=sys.stdout)
        sys.exit(-1)
    else:
        experience_to_search = EXPERIENCE[int(experience) - 1]

    # Validate statistics input
    if statistics not in ['vacancies', 'wage']:
        print("Invalid input, only accepts 'vacancies' or 'wage'", file=sys.stdout)
        sys.exit(-1)

    # Map statistics to search terms
    if statistics == 'vacancies':
        statistics_search = 'Job vacancies'
        header = 'Date,Count'
    else:
        statistics_search = 'Average offered hourly wage'
        header = 'Date,Wage'

    # Validate province input
    if province not in PROVINCE_NAMES:
        print(f"Invalid input for province name - {province}", file=sys.stdout)
        sys.exit(-1)

    # Open input dataset
    with open('q4dataset.csv', 'r', encoding='utf-8-sig') as f:
        fh = csv.reader(f)
        next(fh)  # Skip header row

        # Open output file
        with open(f'q4_processed_{statistics}_{province}.csv', 'w', encoding='utf-8-sig') as ff:
            ff.write(header + '\n')  # Write header to output file

            # Process each row in the dataset
            for row in fh:
                if len(row) < 13:  # Skip rows with insufficient columns
                    continue

                # Extract relevant columns
                date = row[0]
                geo_col = row[1].lower()
                occuptation_col = row[3]
                job_vac_col = row[4]
                stats_col = row[5]
                value = row[12]

                # Filter based on criteria
                if (
                    geo_col == province and
                    stats_col == statistics_search and
                    occuptation_col == 'Software engineers and designers [2173]' and
                    job_vac_col == "Bachelor's degree" and
                    value != '' and
                    EXPERIENCE.index(experience_to_search) < len(EXPERIENCE)
                ):
                    value_date = f"{date},{value}"
                    ff.write(value_date + '\n')

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: main.py <1/2/3/4/5> <vacancies/wage> <province>", file=sys.stdout)
        sys.exit(-1)
    main(sys.argv)
