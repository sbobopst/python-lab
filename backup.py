import datetime
import shutil
import os

mypath = os.path.expanduser("~/python-lab")

def backup():
    data = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M').replace(" ","_").replace(":", "-"))

    try:
        shutil.copytree(src=os.path.join(mypath,'testfolder'), dst=f'./backup_{data}')
    except:
        print(f'Backup directory {data} was not created because one already exists.')

    onlyfiles = [f for f in os.listdir(mypath) if "backup_" in f]

    format = '%Y-%m-%d_%H-%M'

    for f in onlyfiles:
        if (datetime.datetime.now() - datetime.datetime.strptime(f.replace("backup_", ""), format) > datetime.timedelta(minutes=5)):
            shutil.rmtree(os.path.join(mypath,f))
            print("Deleted dir", f, 'REASON: More than 5 minutes have passed')

def main():
    backup()

if __name__ == '__main__':
    main()