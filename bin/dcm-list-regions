#!/usr/bin/env python

from mixcoatl.geography.region import Region
from prettytable import PrettyTable
import argparse
import sys

if __name__ == '__main__':
    """ List regions. """
    parser = argparse.ArgumentParser()
    parser.add_argument('--verbose', '-v', help='Produce verbose output', action="store_true")

    cmd_args = parser.parse_args()

    regions = Region.all()

    if cmd_args.verbose:
        for region in regions:
            region.pprint()
    else:
        region_table = PrettyTable(["Region ID", "Provider ID", "Cloud", "Region Name", "Description", "Status"])
        for region in regions:
            region_table.add_row([region.region_id, region.provider_id, region.cloud['cloud_provider_name'],
                                  region.name, region.description, region.status])
        print(region_table)
