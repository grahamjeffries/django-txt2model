import sys
import csv
import logging
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main(input_file, output_file):
    """
    Parse the input file and write Django models.py content

    Args:
        input_file (str): The input text file to read
        output_file (str): The output file to write generated models contents
    """

    if sys.version_info[0] < 3:
        infile = open(input_file, 'rU')
    else:
        infile = open(input_file, 'r', newline='', encoding='utf8')

    row_dict = {}
    input_reader = csv.DictReader(infile, delimiter='\t')
    for row in input_reader:
        model_name = row.pop('model_name')
        try:
            row_dict[model_name].append(row)
        except KeyError:
            row_dict[model_name] = [row]
    infile.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Generate models.py content
                                                    from a text file.""")
    parser.add_argument('input', type=str, help='the input text file')
    parser.add_argument('--output', type=str, default='./models.py',
                        help='the output model content file')

    args = parser.parse_args()
    main(args.input, args.output)
