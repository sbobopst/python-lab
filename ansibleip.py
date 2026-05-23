import subprocess 

inv_path = "~/ansible-infra-lab/inventories/lab/hosts.yml"
def ansibleping():

    command = ['ansible', '-i', inv_path, 'all', '-m', 'ping']

    return subprocess.call(command) == 0

