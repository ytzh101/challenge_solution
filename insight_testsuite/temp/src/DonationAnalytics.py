import csv, sys, time, math, os

class Donor(object):

    def __init__(self, cmte, name, zip_code, date, amount, other):
        self.cmte = cmte
        self.name = name
        self.zip_code = zip_code
        self.year = date.tm_year
        self.month = date.tm_mon
        self.day = date.tm_mday
        self.amount = amount
        self.other = other

    @staticmethod
    def builder(csv_buffer):
        # TODO corner cases:
        # tans_date is empty or malformed
        # zip_code is empty or fewer than five digits
        # name is empty or malformed
        # cmte_id is empty
        # trans_amt is empty
        try:
            cmte = csv_buffer[0]
            name = csv_buffer[7]
            zip_code = csv_buffer[10]
            date = time.strptime(csv_buffer[13], '%m%d%Y') # parse time from mmddyyyy format into 3 fields
            amount = float(csv_buffer[14])
            other = csv_buffer[15]
        except (IndexError, ValueError):
            print("skip this donor record as challenge description")
            return None

        if (len(zip_code) < 5) or (other) or (not name) or (not cmte):
            print("skip this donor record as challenge description")
            return None

        return Donor(cmte, name, zip_code[:5], date, int(amount+0.5), other)


if __name__ == "__main__":
    # default path argv
    input_itcont_file = 'input/itcont.txt'
    input_percentile_file = 'input/percentile.txt'
    output_file = 'output/repeat_donors.txt'

    try:
        input_itcont_file = sys.argv[1]
    except IndexError:
        pass
    try:
        input_percentile_file = sys.argv[2]
    except IndexError:
        pass
    try:
        output_file = sys.argv[3]
    except IndexError:
        pass

    # path guard
    output_dir = os.path.dirname(output_file)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    # data processing starts here
    dataReader = csv.reader(open(input_itcont_file, newline=''), delimiter='|')
    donors = [] # keep donors record if backtrack is needed in the future
    registered_signatures = [] # HashMap to register unique donors
    repeated_donors = []
    repeated_donation_sum = 0
    repeated_donors_cnt = 0

    with open(input_percentile_file, 'r') as fp:
        percentile = int(next(fp))
        # TODO: corner case percentile < 0 or > 100
        if percentile < 0 or percentile > 100:
            print("percentile is not valid in range of [0, 100]")
            sys.exit(-1)

    fid = open(output_file,'a+')
    for row in dataReader:
        this_donor = Donor.builder(row)
        if this_donor:
            donors.append(this_donor)
            signature_pairs = (this_donor.name, this_donor.zip_code)

            if signature_pairs not in registered_signatures:
                # Unique entry at this moment
                registered_signatures.append(signature_pairs)
            else:
                # Repeated Entry
                repeated_donors.append(this_donor)
                repeated_donors_cnt += 1
                repeated_donors = sorted(repeated_donors, key=lambda x : x.amount, reverse=False)
                target_index = math.ceil((percentile/100)*len(repeated_donors))-1
                target_percentile = repeated_donors[target_index].amount
                repeated_donation_sum += this_donor.amount

                output_string = "|".join([this_donor.cmte, this_donor.zip_code,
                    "{:d}".format(this_donor.year),
                    "{:d}".format(target_percentile),
                    "{:d}".format(repeated_donation_sum),
                    "{:d}".format(repeated_donors_cnt)
                ])

                print(output_string)
                fid.write(output_string + '\n')

    fid.close()
