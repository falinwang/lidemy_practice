
# ALG101 先別急著寫 Leetcode
- Course link: [ALG101 先別急著寫 Leetcode by Lidemy](https://lidemy.com/courses/enrolled/793973)
- Lecturer: 胡立
  - [Blog](https://blog.huli.tw/)
  - [Medium](https://medium.com/@hulitw)
- Start Date: 2020/3/20

### Current status: 21% COMPLETE
------
# Notes
## Day 1

### 課程進行方式：
1. 觀看課程影片學習
2. 觀看課程影片實戰內容
3. 寫作業（Project）練習
4. 觀看課程檢討影片
5. 複習作業

### How to use Lidemy OJ
測試方式
1. 直接在Terminal輸入 然後按ctrl + D
2. 在 editor 打 solve ()
3. 開一個 txt
Terminal
`cat input.txt | node code.js`

### How to use Python on OJ
[使用python在OJ上读取输入流 | Welcome to Luson’s home](https://luxuantao.github.io/2017/08/13/%E4%BD%BF%E7%94%A8python%E5%9C%A8OJ%E4%B8%8A%E8%AF%BB%E5%8F%96%E8%BE%93%E5%85%A5%E6%B5%81/)
[MyMarkDown/如何优雅的使用Python做OJ题.md at master · DIYer22/MyMarkDown · GitHub](https://github.com/DIYer22/MyMarkDown/blob/master/%E5%A6%82%E4%BD%95%E4%BC%98%E9%9B%85%E7%9A%84%E4%BD%BF%E7%94%A8Python%E5%81%9AOJ%E9%A2%98.md)





### Status
- Finished Unit 1 all
- [Unit1.1：What the funk，都說了先不要 | Lidemy 鋰學院](https://lidemy.com/courses/793973/lectures/14419350)
- [OnlineJudge](https://oj.lidemy.com/problem/1003)

---
## Day 2

### How to use debugger
- Refer to unit2 > debugger.html
- Type in debugger in the first row and open the file with browser
``` html
<script>
  debugger
  let arr = [2, 7, 5]
  let max = arr[0]
  for (let i=0; i<arr.length; i++) {
    if (arr[i] > max) {
      max = arr[i]
    }
  }
  console.log(max)
</script>
```
- Use Step (F9) to check the variable step by step
- Hover on the variable can get the current value

## Capitalize - ASCII
* ASCII: https://zh-yue.wikipedia.org/wiki/ASCII
* A = 65, Z = 90, a = 97, z = 122
* lower case - 32 = capital
* Convert in Python 3
	* ASCII to int: `ord('a') = 97`
	* int to string `str(chr(97)) = ‘a’`
* Convert in JavaScript
	* ASCII code - 32
	* `String.fromCharCode(‘a’.charCodeAt(0)-32)`
		* `String.fromCharCode(65)` = ‘A’
		* `’a’.charCodeAt(0)` = 97
		*  `’abc’.charCodeAt(0)` = 97
		*  `’abc’.charCodeAt(2)` = 99
	* Tell if it is low case
		* `c >= ‘a’ && c <= ‘z’`
	* function:
		* `s.toUpperCase()`
