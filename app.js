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
// let n = 10;
// for (let i = 0; i < n; i++) {
//   let row = "";
//   for (let j = 1; j <=n; j++) {
//     row += j;
//   }
//   console.log(row);
// }


// var containsNearbyDuplicate = function(nums, k) {
//     let map=new Map()
//     for (let i=0;i<nums.length;i++){
//         if(map.has(nums[i])){
//             if(Math.abs(map.get(nums[i])-i)<=k){
//                 return true
//             }else{
//                 map.set(nums[i],i)
//             }
//         }else{
//             map.set(nums[i],i)
//         }
//     }
//     return false
// };