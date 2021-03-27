# Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.
# In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. For more information, see: Absolute path vs relative path in Linux/Unix
# Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.
# Example 1:
 
# Input: "/home/"
# Output: "/home"
# Explanation: Note that there is no trailing slash after the last directory
# name.
# Example 2:
 
# Input: "/../"
# Output: "/"
# Explanation: Going one level up from the root directory is a no-op, as the
# root level is the highest level you can go.
# Example 3:
 
# Input: "/home//foo/"
# Output: "/home/foo"
# Explanation: In the canonical path, multiple consecutive slashes are replaced
# by a single one.
# Example 4:
 
# Input: "/a/./b/../../c/"
# Output: "/c"
# Example 5:
 
# Input: "/a/../../b/../c//.//"
# Output: "/c"
# Example 6:
# 题目大意
# 给出一个 Unix 的文件路径，要求简化这个路径。这道题也是考察栈的题目。 解题思路
# 这道题笔者提交了好多次才通过，并不是题目难，而是边界条件很多，没考虑全一种情况就会出错。有 哪些边界情况就看笔者的 test 文件吧。