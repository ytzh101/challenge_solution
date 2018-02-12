## Description 
This is the solution response to the [Insight Data Engineering](http://insightdataengineering.com) Coding Challege. The objective is to identify areas with donation statistics that could be resources of repeat campaign contributions for political donation recipients. This program streamingly processes input donation records from a Federal Election Commission data file, internally identify repeat donors based on (name, zip code), and explicitly output donation statistics for a recipient from an area (zip code) in a calendar year in terms of a given percentile (from input) and totol amount in a sorted order. More details about the challenge problem is in the Github repo [InsightDataScience/donation-analytics](https://github.com/InsightDataScience/donation-analytics)

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

## Additional comments
This program can be enriched to perform more selection functionalities for one or multiple specific recipient, in a given area, and in a given year. This becomes a powerful tool to provide consultanting services to the customers. 

## Contact: 
'ytzhang.bu@gmail.com'

## Disclaimer: 
For any question about the Insight Data Engineering Fellowship and the Coding Challenge, plase email `cc@insightdataengineering.com` 

