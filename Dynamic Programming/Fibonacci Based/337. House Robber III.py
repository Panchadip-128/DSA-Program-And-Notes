# time: O(n)

# logic: will start returning from leaf node.(so postorder traversal).
# logic: everything will depend on whether we include root or not for each subtree.

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        # return pair: [withRoot, withoutRoot]
        def dfs(root):
            if not root:
                return [0, 0]    
            leftPair=  dfs(root.left)
            rightPair= dfs(root.right)
            # now find the ans when we will include the root and when we don't include the root.
            withRoot=  root.val + leftPair[1] + rightPair[1]  # when have to take 'withoutRoot' of it's child.
            withoutRoot= max(leftPair) + max(rightPair)    # we can take max(withRoot,withoutRoot) of  both it's child.
            return [withRoot, withoutRoot]
        
        return max(dfs(root))   # return max([withRoot, withoutRoot])
