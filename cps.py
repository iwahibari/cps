# File check_gpu.py
# Author: Toshiaki Ueda
# Description: 標準入力からssh 
# Version: 5.3

import json 
import os
import sys

# jsonファイルのpathを取得して読み込みする
pyfile_path = __file__
jsonfile_path = os.path.dirname(__file__) + "/pc_ip.json"
jf = open(jsonfile_path, 'r')
json_dict = json.load(jf)

expfile_path = os.path.dirname(__file__) + "/tempfile/tmp_expect_cmd.exp"
os.system("rm -f " + expfile_path)

try:
    pc_name = sys.argv[1]
except:
    print("[ERROR] PC名が入力されていません。PC名をコマンドに続けて入力してください。")
    sys.exit()

pc_info = next((item for item in json_dict["pc"] if item["name"] == pc_name), None)

print(pc_info["ip"])
print(pc_info["pass"])
print(pc_info["username"])



pc_user = pc_info["username"]
pc_ip = pc_info["ip"]
pc_pass = pc_info["pass"]

expcmd_host = "set RemoteHost \"" + pc_user + "@" + pc_ip  + "\"\n"
expcmd_pass = "set PW \""  + pc_pass + "\"\n"

expcmd = r"""
set timeout 5

spawn env LANG=C /usr/bin/ssh -Y ${RemoteHost}
expect {
    -glob "yes/no" {
    send "yes\n"
    exp_continue
    }
    -glob "password:" {
    send "${PW}\n"
    }
}
    interact
"""


# 上書き
with open(expfile_path, mode="w") as wf:
    wf.write(expcmd_host)

# 追記
with open(expfile_path, mode="a") as af:
    af.write(expcmd_pass)
    af.write(expcmd)

os.system("expect " + expfile_path)
os.system("rm -f " + expfile_path)
