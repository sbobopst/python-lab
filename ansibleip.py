import subprocess 
import shutil

inv_path = "~/ansible-infra-lab/inventories/lab/hosts.yml"
def ansibleping():
	if(shutil.which('ansible')!=None):
		command = ['ansible', '-i', inv_path, 'all', '-m', 'ping']
		return subprocess.call(command) == 0
	else:
		print("Ansible not found")
		return False
