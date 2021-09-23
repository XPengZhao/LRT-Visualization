var n = 4
var tree = {}
for(let i=0;i<n;i++){
    tree[i] = {
        'name':i,
        'num_child':0,
        'value':0,
        'sum':0,
        'child':[]
    }
}
var node_wight = [4,9,-7,-8]
for(let i=0;i<n;i++){
    tree[i].value = parseInt(node_wight[i])
    tree[i].sum = parseInt(node_wight[i])
}

function compSum(root){
    let mid = tree[root].value
    for(let i=0;i<tree[root].num_child;i++){
        let a = compSum(tree[root].child[i].name)
        mid += a
    }
    tree[root].sum = mid
    return mid
}
let input_arr = [[0,1], [0,3], [1,2]]
for(var i = 0;i < n-1; i++){
    let lines = input_arr[i]
    tree[lines[0]].child.push(tree[lines[1]])
    tree[lines[0]].num_child++
}
compSum(0)
console.log(tree)
var cha = 0
var sum = 0
var maxCha = 0
var res
for(let i=0;i<n;i++){
    cha = Math.abs(tree[i].sum*2-sum)
    console.log(cha)
    if(maxCha < cha){
        maxCha = cha
        res = i
    }
}
console.log(res)
