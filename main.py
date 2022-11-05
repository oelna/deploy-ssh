import os
import requests

def main():
    my_input = os.environ["INPUT_HOST"]
    
    user = os.environ["INPUT_USER"]
    key = os.environ["INPUT_PASS"]
    host = os.environ["INPUT_SERVER"]
    port = os.environ["INPUT_PORT"]

    my_output = f"Hello {host} at port {port}"

    print(f"::set-output name=myOutput::{my_output}")


if __name__ == "__main__":
    main()
