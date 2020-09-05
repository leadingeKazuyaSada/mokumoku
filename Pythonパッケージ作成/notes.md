# パッケージの作成

参考
- [python の pip でインストールできる自作モジュールを作ってみる / 桃缶食べたい。](https://blog.chocolapod.net/momokan/entry/117)

## 自作モジュールのパッケージ化

### 最低限のフォルダ構成

```
pyplaysc
    │  setup.py
    └─pyplaysc
            __init__.py
            play_sc.py
```

### \_\_init\_\_.py の中での import 

参考
- [Pythonの相対インポートで上位ディレクトリ・サブディレクトリを指定 | note.nkmk.me](https://note.nkmk.me/python-relative-import/)

例: 同じパッケージの同じフォルダにあるモジュールからクラスをインポート
```
from .play_sc import PlaySc, PlayScElement
```

## pipenv install の仕方

参考
- [バージョン管理システムについての但し書き](https://pipenv-ja.readthedocs.io/ja/translate-ja/basics.html#a-note-about-vcs-dependencies)

```
> pipenv install -e git+file:///Dev/Python/my_pckg/pyplaysc#egg=pyplaysc
```

-e は、editable mode (依存性解決をするモード)。

以下のエラーでインストール失敗
```
PS F:\Dev\Python\my_pckg\呼び出し側サンプル> pipenv install -e git+file:///Dev/Python/my_pckg/pyplaysc#egg=pyplaysc
Installing -e git+file:///Dev/Python/my_pckg/pyplaysc#egg=pyplaysc…
Adding pyplaysc to Pipfile's [packages]…
Installation Succeeded
Pipfile.lock (ef5eb5) out of date, updating to (db4242)…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
Success!
Updated Pipfile.lock (ef5eb5)!
Installing dependencies from Pipfile.lock (ef5eb5)…
An error occurred while installing -e git+file:///F:/Dev/Python/my_pckg/pyplaysc#egg=pyplaysc! Will try again.
  ================================ 1/1 - 00:00:00
Installing initially failed dependencies…
[pipenv.exceptions.InstallError]:   File "c:\users\sata\appdata\local\programs\python\python38\lib\site-packages\pipenv\core.py", line 1983, in do_install
[pipenv.exceptions.InstallError]:       do_init(
[pipenv.exceptions.InstallError]:   File "c:\users\sata\appdata\local\programs\python\python38\lib\site-packages\pipenv\core.py", line 1246, in do_init
[pipenv.exceptions.InstallError]:       do_install_dependencies(
[pipenv.exceptions.InstallError]:   File "c:\users\sata\appdata\local\programs\python\python38\lib\site-packages\pipenv\core.py", line 858, in do_install_dependencies
[pipenv.exceptions.InstallError]:       batch_install(
[pipenv.exceptions.InstallError]:   File "c:\users\sata\appdata\local\programs\python\python38\lib\site-packages\pipenv\core.py", line 763, in batch_install
[pipenv.exceptions.InstallError]:       _cleanup_procs(procs, not blocking, failed_deps_queue, retry=retry)
[pipenv.exceptions.InstallError]:   File "c:\users\sata\appdata\local\programs\python\python38\lib\site-packages\pipenv\core.py", line 681, in _cleanup_procs
[pipenv.exceptions.InstallError]:       raise exceptions.InstallError(c.dep.name, extra=err_lines)
[pipenv.exceptions.InstallError]: ['Obtaining pyplaysc from git+file:/F:/Dev/Python/my_pckg/pyplaysc#egg=pyplaysc', '  Updating f:\\dev\\python\\my_pckg\\呼び出し側サンプル\\.venv\\src\\pyplaysc clone']
[pipenv.exceptions.InstallError]: ['ERROR: Command errored out with exit status 1: git reset --hard -q 88a07d804957fde3248552ea785f41a5bfd04d30 Check the logs for full command output.']
ERROR: ERROR: Package installation failed...
     ================================ 0/1 - 00:00:00
```

## requirements.txt の書き方

## Pipfile の書き方
