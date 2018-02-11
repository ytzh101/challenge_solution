
This is the solution response to the Insight Data Science challege. 

## System requirements 
The solution src runs and is tested against Python 3.6.4 with default packages on OSX.
No 3rd party ptyhon packages are required. 

## Repo directory structure

    ├── README.md
    ├── input
    │   ├── README.md
    │   ├── itcont.txt
    │   └── percentile.txt
    ├── insight_testsuite
    │   ├── results.txt
    │   ├── run_tests.sh
    │   ├── temp
    │   │   ├── input
    │   │   │   ├── itcont.txt
    │   │   │   └── percentile.txt
    │   │   ├── output
    │   │   │   └── repeat_donors.txt
    │   │   ├── run.sh
    │   │   └── src
    │   │       ├── DonationAnalytics.py
    │   │       └── README.md
    │   └── tests
    │       └── test_1
    │           ├── README.md
    │           ├── input
    │           │   ├── itcont.txt
    │           │   └── percentile.txt
    │           └── output
    │               └── repeat_donors.txt
    ├── output
    │   ├── README.md
    │   └── repeat_donors.txt
    ├── run.sh
    └── src
        ├── DonationAnalytics.py
        └── README.md

## Test Results 
Run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 
    
On success:

    [PASS]: test_1
    [Sun Feb 11 12:00:45 EST 2018] 1 of 1 tests passed

Contact: 'ytzhang.bu@gmail.com'
Disclaimer: for any question about the challenge description, plase email `cc@insightdataengineering.com` 

