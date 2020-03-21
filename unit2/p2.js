// Unit2.5 find the second largest
// answer
let arr = [5, 8, 6]
let max = -Infinity
let max2 = -Infinity
for (let i=0; i<arr.length; i++) {
  if (arr[i] > max) {
    max2 = max
    max = arr[i]
  } else if (arr[i] > max2) {
    max2 = arr[i]
  }
}
console.log(max, max2)

// Unit2.6 Upper the string
let str = "You better run now! az"
// solution 1
console.log(str.toUpperCase())
// solution 2
let ans1 = ""
for (let i=0; i<str.length; i++) {
  let code = str.charCodeAt(i)
  // console.log(code)
  if (code >= 97 && code <= 122) {
    ans1 += String.fromCharCode(code - 32)
  } else {
    ans1 += str[i]
  }
}
console.log(ans1)
// solution 3
let str3 = "Hi az"
let ans3 = ''
for(let i=0; i<str3.length; i++) {
  if (str3[i] >= 'a' && str3[i] <= 'z') {
    ans3 += String.fromCharCode(
      str3.charCodeAt(i) - 32
    )
  } else {
    ans3 += str3[i]
  }
}
console.log(ans3)

// Unit2.7 Delete specifit letter in a string
let origin = "Jumpy"
let letter = "y"
let ans = ""
for (let i=0; i<origin.length; i++) {
  if (origin[i] != letter)  {
    ans = ans + origin[i]
  }
}
console.log(ans)

// Unit2.8 Project 2
// 1. Find the second smallest
// 2. lower case to upper case and vise versa
// 3. Print the factor numbers
