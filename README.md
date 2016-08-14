# PokemonGo-TSP
最近被滑鐵盧大學分享的一篇PokemonGo最佳路徑規劃文章 [[1]](#Reference) 而啟發

剛好最近又很瘋PokemonGo，決定試著動手用模擬退火來解決PokemonGo的TSP問題


## Quick Start
### Requirement
`pip install sqlite3 numpy`

`pip freeze | grep numpy`

numpy==1.11.1, python2/3的環境下皆可運行


### Annealing parameters

    markov_step = 10 * num	# 內循環次數
    T = 100					# 初始溫度
    T = 1					# 最低溫度
    T_ALPHA = 0.99			# 退溫常數
如果想要得到更好的解，增加markov_step是個好辦法

	markov_step = 100 * num # 內循環次數
	
### Execute
直接執行`python tsp.py`, 預設會讀取`data/pokestops.csv`

跑出結果後會畫出cost function和route, 結果如下

![image](http://i.imgur.com/GoZRbzt.png")

最後再把結果存入`data/tsp.sqlite`內，方便未來分析

推薦下載 [Sqlite Browser](http://sqlitebrowser.org/) GUI管理工具來開啟資料庫

個人都是下四次 `python tsp.py & ` 放到背景去執行，然後去做自己的事情

等跑完後最後再去sqlite看數據即可



### Google Map Visualization

附上一張交大校內[Pokemon Stop的最佳路規劃](https://www.google.com/maps/d/edit?mid=1lLYI5pnaxiFfFOcAQ45-Foeg-Jg)

目前是人工手拉的地圖，希望未來能夠自動整合到地圖上QQ


 ![image](http://i.imgur.com/GqmAOl3.png)




## What is TSP?
TSP全名Travelling salesman problem，中文翻譯做「旅行商問題」[2](#Reference)

給定一系列城市和每對城市之間的距離，求解訪問每一座城市一次並回到起始城市的最短迴路

在 Computer Science 內屬於NP Hard的難題

![image](https://upload.wikimedia.org/wikipedia/commons/2/2b/Bruteforce.gif)
 
## What is SA?
SA全名Simulated Annealing，中文翻譯做「模擬退火」[[3]](#Reference) [[4]](#Reference)

一種基於熱力學原理的隨機搜尋演算法，用來在固定時間內在一個大的搜尋空間內找最優解

 ![image](https://upload.wikimedia.org/wikipedia/commons/d/d5/Hill_Climbing_with_Simulated_Annealing.gif)


## TODO
- [ ] Road TSP(結合Google Map根據實際地理距離來計算)
- [ ] Link to result to Google Map
- [ ] Parallelization 
- [ ] Reannealing
- [ ] Cooling schedule

目前只實現了Geometric TSP，Road TSP 還在克服中

用Google Map API 來計算實際地理距離目前還有點雷

像是操場/壘球場這種地方會繞一大圈而不是直接穿越

希望有經驗的大大能夠提出建議！ 謝謝


## Reference
[1] [Pokemon Go Traveling Salesman Problem](http://www.math.uwaterloo.ca/tsp/poke/index.html) - 國外的Pokemon Go TSP

[2] [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem) - TSP背景知識

[3] [Simulated annealing](https://en.wikipedia.org/wiki/Simulated_annealing) - 模擬退火背景知識

[4] [模拟退火算法求解旅行商问题](http://blog.csdn.net/lalor/article/details/7688329) - 詳盡的模擬退火解說 ＋ Java實現，提到了三種產生新狀態的方式

[5] [Queen of College Tours](http://www.math.uwaterloo.ca/tsp/college/index.html) - 從Geometric TSP 到 Road TSP

[6] [PokemonGo-Map](https://github.com/PokemonGoMap/PokemonGo-Map) - 地圖掃描工具，開啟後放置一段時間，再把pogom.db拿出來，即可取得道館/補給站座標
