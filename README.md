# cps 複数PCへのsshを簡単に扱う

## cpsとは
- LinuxやWSLで長いコマンド、パスワードを用いずにssh接続をする。
- 登録済みの全PCにssh接続をして、指定コマンドを実行する。
- ipアドレスやパスワードを記述したjsonファイルを用いるため、共有PCでは使わない。

## cpsを使う

**0. cpsを実行するには`expect`コマンドとpythonが必要です。インストールされていない場合、以下のコマンドを実行してインストールしてください。**
```sh
sudo apt install python3
sudo apt install expect
```

**1. 本リポジトリをクローン**
```sh
git clone https://github.com/iwahibari/cps.git
```

**2. `~/.bashrc`にaliasを記載**
```sh
alias cps="python pathToDirectry/cps/cps.py"
```

**3. `source ~/.bashrc`を実行**

**4. `pc_ip.json`にssh接続先PCの情報を登録**
    cpsでは`pc_ip.json`に登録された情報をもとにssh接続を実行します。  
    下の例をもとにssh接続先pcの情報を登録してください。  
    コマンド実行時に指定するPC名を`name`に、ユーザーネームを`username`に、ipアドレスを`ip`に、パスワードを`pass`にそれぞれ登録します。  
```json
{
	"pc": [
		{
			"name": "test1",
			"username": "username1",
			"ip": "192.168.0.111",
			"pass": "password"
		},
		{
			"name": "test2",
			"username": "username2",
			"ip": "192.168.0.222",
			"pass": "password"
		},
		{
			"name": "test3",
			"username": "username3",
			"ip": "192.168.0.333",
			"pass": "password"
		}
	]
}
```

**5. 準備は以上です。**

## 使い方

以下のコマンドを実行することで、IPアドレス、ユーザー名、パスワードの入力を省略してSSH接続をすることができます
```sh
cps 接続先PC名前
```


## リリースノート

ver.5.3

