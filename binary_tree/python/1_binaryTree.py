#!/mnt/lustre02/jiangsu/aispeech/home/xmw01/tools/anaconda3/bin/python
# -*- coding: UTF-8 -*-

from collections import deque
from typing import List



class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Display(object):
    #binary tree levelOrder traversal print
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
    #def levelOrder(self, root : TreeNode):
        results =[]
        if(root == None): 
            return results
        
        que = deque([root])  #must be iterable

        while que:
            size = len(que)
            result = []
            for i in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if(cur.left):
                    que.append(cur.left)
                if(cur.right):
                    que.append(cur.right)
            results.append(result)

        return results



def constructBinaryTree(nums):
    Treelist = [None for _ in range(len(nums))]

    for i in range(len(nums)):
        if nums[i] != None:
            node = TreeNode(nums[i])
            Treelist[i] = node
        if i == 0: root = node

    i = 0
    #注意结束的规则如下
    while i * 2 + 2 < len(nums):
        if Treelist[i] != None:
            # 和c++ 构建一样，这个是关键逻辑
            Treelist[i].left = Treelist[2 * i + 1]
            Treelist[i].right = Treelist[2 * i + 2]
            i += 1
    #返回根节点
    return root

if __name__ == '__main__':

    nums = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
    root = constructBinaryTree(nums)
    display = Display()
    listBinaryTree = display.levelOrder(root)
    for i in listBinaryTree:
        for j in i:
            print(j)
    print(root)
