#!/usr/bin/env python

from mixcoatl.admin.billing_code import BillingCode
from prettytable import PrettyTable
import argparse
import sys

if __name__ == '__main__':
    """ Returns a list of billingcode codes. """
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', help='Produce verbose output', action="store_true")
    cmd_args = parser.parse_args()

    all_billingcodes = BillingCode.all()

    if cmd_args.verbose:
        for billingcode in all_billingcodes:
            billingcode.pprint()
    else:
        billingcode_table = PrettyTable(["ID", "Name", "Budget Code", "Soft Quota", "Hard Quota",
                                         "Current Usage", "Projected Usage", "Status"])
        for billingcode in all_billingcodes:
            if hasattr(billingcode, 'soft_quota'):
                soft_quota = billingcode.soft_quota
            else:
                soft_quota = {'currency': '', 'value': 0}
            if hasattr(billingcode, 'hard_quota'):
                hard_quota = billingcode.hard_quota
            else:
                hard_quota = {'currency': '', 'value': 0}
            if hasattr(billingcode, 'current_usage'):
                current_usage = billingcode.current_usage
            else:
                current_usage = {'currency': '', 'value': 0}
            billingcode_table.add_row([billingcode.billing_code_id, billingcode.name, billingcode.finance_code,
                                       "%s %.2f" % (soft_quota['currency'], soft_quota['value']),
                                       "%s %.2f" % (hard_quota['currency'], hard_quota['value']),
                                       "%s %.2f" % (current_usage['currency'], current_usage['value']),
                                       "%s %.2f" % (billingcode.projected_usage['currency'],
                                       billingcode.projected_usage['value']), billingcode.status])

        print(billingcode_table)
