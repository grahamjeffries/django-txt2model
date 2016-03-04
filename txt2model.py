import sys
import csv
import logging
import argparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def parse_field(field):
    """
    Parse a field dictionary and return a properly formatted string

    Args:
        field (dict): A dictionary of model field arguements

    Returns:
        str: A formatted string of the model field
    """
    field_name = field.pop('field_name', None)
    field_type = field.pop('field_type', None)

    field_clean = {}

    for f in field:
        if field[f] != '':
            field_clean[f] = field[f]

    kwargs = ', '.join(['%s=%s' % (f, field_clean[f]) for f in field_clean])
    entry = '    %s = models.%s(%s)\n' % (field_name,
                                          field_type,
                                          kwargs)
    return entry


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
        model_name = row.pop('model_name', None)
        try:
            row_dict[model_name].append(row)
        except KeyError:
            row_dict[model_name] = [row]
    infile.close()

    with open(output_file, 'w') as f:
        f.write('from django.db import models\n')
        for model_name in row_dict.keys():
            f.write('\n\nclass %s(models.Model):\n' % model_name)
            for field in row_dict[model_name]:
                f.write(parse_field(field))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="""Generate models.py content
                                                    from a text file.""")
    parser.add_argument('input', type=str, help='the input text file')
    parser.add_argument('--output', type=str, default='./models.py',
                        help='the output model content file')

    args = parser.parse_args()
    main(args.input, args.output)
