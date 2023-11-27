const mod = 1e9+7;
const f = (n,i,j,ans) =>{
  if(n==0) return 1;
  if(ans[n][i][j]!==mod) return ans[n][i][j];
  let val1 = 0 , val2 = 0 , val3 = 0;
  if(i>0) val1 = f(n-1,i-1,2,ans) % mod;
  if(j>0) val2 = f(n-1,i,j-1,ans) % mod;
  val3 = f(n-1,i,2,ans) % mod; 
  return ans[n][i][j] = ((val1%mod + val2%mod)%mod + val3%mod) % mod ;
}
var checkRecord = function(n) {
    let i = 1 , j = 2 , ans = [];
    for(let i = 0; i<=n ;i++){
      let arr = [] ; 
      for(let i=0;i<=1;i++) arr.push(new Array(3).fill(mod));
      ans.push(arr); 
    }
    return f(n,i,j,ans) ; 
};