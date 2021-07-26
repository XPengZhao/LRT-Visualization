function NodeProj(name,version){
    this.name = name
    this.version = version
}
function findNode(nodeKey,midList,child,childWord,childNode){
    if(nodeKey in midList){
        midList[nodeKey].reference = {}
        if (child in midList) {
            midList[nodeKey].reference[childWord] = midList[childWord]
        } else {
            midList[childWord] = childNode
            midList[nodeKey].reference[childWord] = childNode
        }
    }
}
function addChild(midList,father,childWord,child,fatherNode){
    let childNode = new NodeProj(child[0], child[1])
    if(father in midList){
        for(let key in midList) {
            if(key === father){
                midList[key].reference = {}
                if (child in midList) {
                    midList[key].reference[childWord] = midList[childWord]
                } else {
                    midList[childWord] = childNode
                    midList[key].reference[childWord] = childNode
                }
            }else {

            }

            for (let key1 in midList[key].reference){
                if (key1 === father) {
                    midList[key].referece[father].reference = {}
                    if (child in midList) {
                        midList[key].referece[father].reference[childWord] = midList[childWord]
                    } else {
                        midList[childWord] = childNode
                        midList[key].referece[father].reference[childWord] = childNode
                    }
                }
            }
        }
    }else {
        fatherNode.reference = {}
        fatherNode.reference[childWord] = childNode
        midList[father] = fatherNode
    }


    return midList
}
function buildTree(rootProj,reference){
    let res = {}
    let midList = {}
    let rootWord = rootProj.split(',')
    let rootNode = new NodeProj(rootWord[0],rootWord[1])
    midList[rootWord[0]+rootWord[1]] = rootNode
    for(let i=0; i<reference.length;i++){
        console.log(midList)
        let word = reference[i]
        let resWord = word.split('->')
        let father = resWord[0].split(',')
        let child = resWord[0].split(',')
        let fatherWord = father[0]+father[1]
        let childWord = child[0]+child[1]
        let fatherNode = new NodeProj(father[0],father[1])
        midList = addChild(midList,fatherWord,childWord,child,fatherNode)

    }
    console.log(midList[rootWord[0]+rootWord[1]].reference)
}
// 请按题目要求修改参数
function findVersion(checkProk,rootProj,reference) {
    // 在这⾥写代码
    buildTree(rootProj,reference)
}
findVersion('e ','a,1',['b,1->e,2','c,1->e,1','a,1->b,1','a,1->c,1','a,1->d,1'])
