# 使い方

* Pythonファイル単体では、co2濃度(ppm)の数値を出力します。

```python3 read.py```

* csvファイルに出力する

```chmod +x script.sh```
で実行権限を与える。

```./script.sh```
で、csvファイルが生成される。

* 1分ごとにco2濃度をcsvファイルに追記する

`crontab -e`にて、

```
* * * * * PATH/script.sh
```
を追記する。