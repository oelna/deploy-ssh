import os
import requests

def main():
    my_input = os.environ["INPUT_USERNAME"]

    my_output = f"Hello {my_input}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
