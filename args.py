import argparse

def parse_args():
    arg_parser = argparse.ArgumentParser()

    # Help messages for each option
    helps = {}
    helps['data'] = 'Data to calculate TSP. [Default: nctu]'
    helps['file'] = 'Full path of data file.'
    helps['markov'] = 'Coefficient to multiply the number of locations. [Default: 10]'
    helps['halt'] = 'Optimization threshold: stability of solution as program halts. [Default: 150]'
    helps['init_temperature'] = 'Initial temperature. [Default: 100]'

    arg_parser.add_argument(
        '-d', '--data', 
        choices=['nctu', 'nthu', 'thu'],
        default='nctu',
        help=helps['data']
    ) 

    arg_parser.add_argument(
        '-f', '--file',
        help=helps['file'],
        metavar='FULL_FILE_PATH'
    )

    arg_parser.add_argument(
        '-m', '--markov-coefficient', 
        type=int,
        default=10,
        help=helps['markov']
    )

    arg_parser.add_argument(
        '--halt', 
        help=helps['halt'],
        type=int,
        default=150,
        metavar='THRESHOLD'
    )

    arg_parser.add_argument(
        '-t', '--init-temperature',
        help=helps['init_temperature'],
        type=int,
        default=100,
        metavar='INITIAL_TEMPERATURE'
    )

    return arg_parser.parse_args()
