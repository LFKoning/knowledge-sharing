import sys
import pandas

import os



def main(file_path):
    """Main program routine."""
    if not os.path.exists(file_path):
        print(f"Cannot find file: {flie_path}!")
        sys.exit()

    df = pd.read_csv(file_path)



if __name__ == "__main__":
    file_path = sys.argv[1]
    main(file_path)

