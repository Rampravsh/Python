// let name ='rampravesh kumar'
// let percentage=92
// console.log('my name is:',name,percentage)
// console.log(name+percentage)

// var singleNumber = function (nums) {
//   let set = new Set();
//   for (let i = 0; i < nums.length; i++) {
//     if (set.has(nums[i])) {
//       set.delete(nums[i]);
//     } else {
//       set.add(nums[i]);
//     }
//   }
//   return set[0]
// };
// let nums = [2, 2, 1];
// console.log(singleNumber(nums));
let n = 10;
for (let i = 0; i < n; i++) {
  let row = "";
  for (let j = 1; j <=n; j++) {
    row += j;
  }
  console.log(row);
}
