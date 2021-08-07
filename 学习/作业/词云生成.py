import wordcloud
w = wordcloud.WordCloud()
w.generate("哈哈哈哈 哈哈啊哦 地方 地方")
w.to_file("da.jpg")