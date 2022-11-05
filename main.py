import os
import requests

def main():
    my_input = os.environ["INPUT_SERVER"]
    
    user = os.environ["INPUT_USER"]
    key = os.environ["INPUT_PASS"]
    host = os.environ["INPUT_SERVER"]
    port = os.environ["INPUT_PORT"]
    
    source = os.environ["INPUT_SOURCE"]
    target = os.environ["INPUT_TARGET"]

    my_output = f"Hello {host} at port {port}"

    print(f"::set-output name=myOutput::{my_output}")
    
    
    
    
    keyfile = "~/.ssh/id_rsa"
    os.makedirs(os.path.dirname(keyfile), exist_ok=True)
    with open(keyfile, "w") as text_file:
        text_file.write("%s" % key)
        
    server_string = "%s@%s:%s" % (user, host, target)
        
    subprocess.call(["rsync", "-rltgoDzvO", "--dry-run", "./", server_string])
    # rsync -Pav -e "ssh -i $HOME/.ssh/somekey" username@hostname:/from/dir/ /to/dir/

if __name__ == "__main__":
    main()
