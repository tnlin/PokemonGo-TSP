# PokemonGo-TSP
最近被滑鐵盧大學分享的一篇PokemonGo最佳路徑規劃文章 [[1]](http://www.math.uwaterloo.ca/tsp/poke/index.html) 而啟發

剛好最近又很瘋PokemonGo，決定試著動手用模擬退火來解決PokemonGo的TSP問題

## What is TSP?
TSP全名Travelling salesman problem，中文翻譯做「旅行商問題」[[2]](https://en.wikipedia.org/wiki/Travelling_salesman_problem)

給定一系列城市和每對城市之間的距離，求解訪問每一座城市一次並回到起始城市的最短迴路

在計算複雜度(Computing Complexity)上 屬於NP-Complete的難題

 ![image](https://upload.wikimedia.org/wikipedia/commons/3/3c/Branchbound.gif)

## What is SA?
SA全名Simulated Annealing，中文翻譯做「模擬退火」[[3]](https://en.wikipedia.org/wiki/Simulated_annealing) [[4]](http://blog.csdn.net/lalor/article/details/7688329)

一種基於熱力學原理的隨機搜尋演算法，用來在固定時間內在一個大的搜尋空間內找最優解

 ![image](https://upload.wikimedia.org/wikipedia/commons/d/d5/Hill_Climbing_with_Simulated_Annealing.gif)


## Usage
### Requirement

Linux ( Debian / Ubuntu ):
```
apt-get install python-matplotlib
pip install -r requirements.txt
```

Linux ( Fedora / Redhat ):
```
yum install python-matplotlib
pip install -r requirements.txt
```

Mac OSX:
```
pip install matplotlib
pip install -r requirements.txt
```


### Annealing parameters

```
markov_step = 10 * num_location	# 內循環次數
T = 100					        # 初始溫度
T = 1					        # 最低溫度
```

因為是隨機搜尋演算法，不一定能保證每次都得到最佳解答

如果想要得到更好的解，增加markov_step是個好辦法

```
markov_step = 100 * num_location # 內循環次數
```

### Cooling Schedules
冷卻計畫[[7]](http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/)是模擬退火中用來降溫的函數，不同的降溫方式會影響演算法計算結果的速度以及結果的優劣（離最優解多近）

### Execute
直接執行`python tsp.py`, 預設會讀取`data/nctu.csv`

跑出結果後會畫出cost function和route, 結果如下

![image](http://i.imgur.com/GoZRbzt.png")

最後再把結果存入`data/tsp.db`內，方便未來分析

推薦下載 [Sqlite Browser](http://sqlitebrowser.org/) GUI管理工具來開啟資料庫

個人都是跑N次 `python tsp.py & ` 放到背景去執行，然後去做自己的事情

等跑完後最後再去sqlite看數據即可

### Execution Options

目前提供了一些命令列參數供大家在執行時比較彈性，可以依據自己的喜好來設定

一般來說想要取得比較優化的結果會比較耗時，而比較省時的運行結果就不會那麼優

目前預設的參數數值皆是經過實驗對比後相較平衡的，不會非常耗時，結果也不錯

`-h, --help 可看命令列參數的幫助解說`

`-d, --data 用來設定數據來源（預設值：nctu）`

`-f, --file 使用自己的數據檔案來作計算`

`-m, --markov-coefficient 用來設定內循環次數的係數（預設值：10）`

`--halt 用來設定當結果多穩定時程式就可以停止運算（預設值：150）`

`-t, --init-temperature 用來設定初始溫度（預設值：100）`

*附註：如果`-f`和`-d`一起使用，系統將會忽略`-d`*

### Google Map Visualization
執行完`tsp.py`之後，會根據DB內最短路徑產生路徑檔`path.json`，接著開啟index.html就會看到render到Google Map的結果，如下

交大

![NCTU](http://i.imgur.com/alsiSTZ.gif)

東海

![image](http://imgur.com/SbLBsmD.gif)

PS.
- 地圖會自動置中，但若要換一個地點跑數據，記得先清DB
- 參考[Google Map API 申請教學](https://pgm.readthedocs.io/en/develop/basic-install/google-maps.html)替換掉`index.html` 中 `{YOUR API KEY}`
- 執行`python -m SimpleHTTPServer` 或者 `python -m http.server`，用瀏覽器開啟`127.0.0.1:8000`，即可看到結果

## TODO
- [x] 將最佳路徑Link到Google Map上
- [x] Cooling schedule
- [ ] Road TSP (結合Google Map根據實際地理距離來計算)
- [ ] 考慮雷達半徑(50m)和5分鐘重置的條件，計算出最佳路線
- [ ] Benchmark with other algorithms
- [ ] Parallelization
- [ ] Reannealing

目前只實現了Geometric TSP，Road TSP [[5]](http://www.math.uwaterloo.ca/tsp/college/index.html) 還在克服中

用Google Map API 來計算實際地理距離目前還有點雷，像是操場/壘球場這種地方會繞一大圈而不是直接穿越

希望有經驗的大大能夠提出建議！ 謝謝

歡迎PR!!

## Reference
[1] [Pokemon Go Traveling Salesman Problem](http://www.math.uwaterloo.ca/tsp/poke/index.html) - 國外的Pokemon Go TSP

[2] [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) - TSP背景知識

[3] [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) - 模擬退火背景知識

[4] [模拟退火算法求解旅行商问题](http://blog.csdn.net/lalor/article/details/7688329) - 詳盡的模擬退火解說 ＋ Java實現，提到了三種產生新狀態的方式

[5] [Queen of College Tours](http://www.math.uwaterloo.ca/tsp/college/index.html) - 從Geometric TSP 到 Road TSP

[6] [PokemonGo-Map](https://github.com/PokemonGoMap/PokemonGo-Map) - 地圖掃描工具，開啟後放置一段時間，再把`pogom.db`拿出來，即可取得道館/補給站座標

[7] [A Comparison of Cooling Schedules for Simulated Annealing](http://what-when-how.com/artificial-intelligence/a-comparison-of-cooling-schedules-for-simulated-annealing-artificial-intelligence/) - 不同冷卻計畫的比較
