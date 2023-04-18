// 1번
const nums = [1,2,3,4,5,6,7,8]

for (let i = 0; i < nums.length; i++) {
  console.log('nums[' + i + ']: ' + nums[i])
}

// for (const i = 0; i < nums.length; i++) {
//                                     ^

// TypeError: Assignment to constant variable.

// i는 const 형식으로 선언되었기 때문에 값을 바꿀 수 없다.
// i++에서 i 값을 1 증가시키려 했기 때문에 오류가 발생하였다.

// 2번
for (num of nums) {
  console.log(num, typeof num)
}
// in 을 이용하면 nums의 key를 가져오기 때문에 array인 nums의 index를 
// string으로 가져오게 됩니다. of 을 사용하여 nums의 value를 가져와야
// number 형식의 숫자를 가져오게 됩니다.
// 0 string
// 1 string
// 2 string
// 3 string
// 4 string
// 5 string
// 6 string
// 7 string
