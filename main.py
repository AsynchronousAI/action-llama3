import argparse
from terminal import *
from gui import *

def main():
    parser = argparse.ArgumentParser(
                    prog='action-llama3',
                    description='A LLM that is locally hosted and can take commands to complete tasks.',
                    epilog='Unexex Labs - 2024')
    
    parser.add_argument('-g', '--gui', help='Should host a GUI?', action='store_true')
    parser.add_argument('-t', '--term', help='Should continue in terminal?', action='store_true')
    parser.add_argument('-a', '--temp', help='Temperature for the model.', default=0.7, type=float)

    args = parser.parse_args()

    if args.gui:
        gui(args)
    elif args.term:
        terminal(args)
    else:
        print("no args")

if __name__ == "__main__":
    main()
