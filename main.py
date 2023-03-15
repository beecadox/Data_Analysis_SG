import argparse
from parts import part1, part2, part3
from data_preprocessing import preprocess 

OPTIONS = {
    1: part1,
    2: part2,
    3: part3,
}

if __name__ =="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--preprocess', 
                        action=argparse.BooleanOptionalAction,
                        default=False,
                        help='Choose already preprocessed data or raw data')
    parser.add_argument('--part', 
                        type=int, 
                        default=1, 
                        choices=[1, 2, 3],
                        help='Choose which Assignment Part to run')
    args = parser.parse_args()
    if args.preprocess:
        data = preprocess()
    else:
        print("raw data")  
    print(args.part)