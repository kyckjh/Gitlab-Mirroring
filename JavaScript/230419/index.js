
for (let j = 0; j < 5; j++) {
  let str = ""
  for (let k = 0; k < 5-j; k++)
  {
    str += " "
  }
  for (let k = 5-j; k < 5+j+1; k++)
  {
    str += "*"
  }
  for (let k = 5+j+1; k < 9; k++)
  {
    str += " "
  }
  console.log(str)
}