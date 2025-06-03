# File check_gpu.py
# Author: Toshiaki Ueda
# Description: 標準入力からssh -> gpu確認 nviida-smi
# Version: 3.2

import json 
import os
import sys

# jsonファイルのpathを取得して読み込み
pyfile_path = __file__
jsonfile_path = os.path.dirname(__file__) + "/pc_ip.json"
jf = open(jsonfile_path, 'r')
json_dict = json.load(jf)
json_length = (len(json_dict["pc"]))

expfile_path = os.path.dirname(__file__) + "/tempfile/tmp_expect_cmd.exp"
logfile_path = os.path.dirname(__file__) + "/tempfile/tmp_expect_log.out"
tmpoutfile_path = os.path.dirname(__file__) + "/tmp_out.out"

os.system("rm -f " + expfile_path + " "  + logfile_path)

i = 1

shell_cmd = sys.argv[1]

for key in json_dict["pc"]:
    print("[" + str(i) + "/" + str(json_length) +"]  checking " + key["name"])

    pc_name = key["name"]
    pc_username = key["username"]
    pc_ip = key["ip"]
    pc_pass = key["pass"]

    with open(logfile_path, mode= "a") as lf:
        lf.write("\n" + pc_name + "\n")

    expcmd_host = "set RemoteHost " + pc_username + "@" + pc_ip  + "\n"
    expcmd_pass = "set PW "  + pc_pass + "\n"
    explog_path = "set logfile " + logfile_path + "\n"
    expshell_cmd = "set shellcmd " + shell_cmd + "\n"

    expcmd = r"""
spawn ssh -Y ${RemoteHost}
expect "password"
send "${PW}\r"
expect "\\\$"
log_file ${logfile}
send "${shellcmd}\r"
expect "\\\$"
log_file
exit 0
"""

    # 上書き
    with open(expfile_path, mode="w") as wf:
        wf.write(expcmd_host)

    # 追記
    with open(expfile_path, mode="a") as af:
        af.write(expcmd_pass)
        af.write(explog_path)
        af.write(expshell_cmd)
        af.write(expcmd)



    os.system("expect -f " + expfile_path  + " > " + tmpoutfile_path)
    with open(logfile_path, mode="a") as lf:
        lf.write("\n")
    i += 1
    
os.system("cat " + logfile_path)
os.system("rm -f " + expfile_path + " " + logfile_path + " " + tmpoutfile_path)
