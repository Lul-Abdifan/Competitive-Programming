# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:

		i = 0
		req = 0
		def solve(level):
			nonlocal i,req
			val = ""
			req = 0
			while i<len(s) and s[i]!='-':
				val+=s[i]
				i+=1
			node = TreeNode(int(val))
			while i<len(s) and s[i]=='-':
				req+=1
				i+=1
			if req>level:
				node.left = solve(level+1)
				if i<len(s) and req>level:
					node.right = solve(level+1)
			return node     
		return solve(0)