import os
import requests

def main():
    my_input = os.environ["INPUT_SERVER"]
    
    user = os.environ["INPUT_USER"]
    key = os.environ["INPUT_PASS"]
    host = os.environ["INPUT_SERVER"]
    port = os.environ["INPUT_PORT"]

    my_output = f"Hello {host} at port {port}"

    print(f"::set-output name=myOutput::{my_output}")
    
    
    # subprocess.call(["rsync", "-Ccavz", "--delete","DJStatic", "username@website"])
    
    keyfile = "~/.ssh/id_rsa"
    os.makedirs(os.path.dirname(keyfile), exist_ok=True)
    with open(keyfile, "w") as text_file:
        text_file.write("%s" % key)


if __name__ == "__main__":
    main()
