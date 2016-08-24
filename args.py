import argparse

def parse_args():
    arg_parser = argparse.ArgumentParser()

    # Help messages for each option
    helps = {}
    helps['data'] = 'Data to calculate TSP'
    helps['markov'] = 'Coefficient to multiply the number of locations'
    helps['halt'] = 'Optimization threshold: stability of solution as program halts'

    arg_parser.add_argument(
        '-d', '--data', 
        choices=['nctu', 'nthu', 'thu'],
        default='nctu',
        help=helps['data']
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

    return arg_parser.parse_args()
