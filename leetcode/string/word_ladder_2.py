# 题目
# Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
# 1. Only one letter can be changed at a time
# 2. Each transformed word must exist in the word list. Note that beginWord is not a transformed
# word. Note:
# Return an empty list if there is no such transformation sequence. All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same. Example 1:
        
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: [
#   ["hit","hot","dot","dog","cog"],
#   ["hit","hot","lot","log","cog"]
# ]
# Example 2:
 
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: []
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#  题目大意
# 给定两个单词(beginWord 和 endWord)和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则:
# 1. 每次转换只能改变一个字母。
# 2. 转换过程中的中间单词必须是字典中的单词。
# 说明:
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。 解题思路
# 这一题是第 127 题的加强版，除了找到路径的⻓度，还进一步要求输出所有路径。解题思路同第 127 题一样，也是用 BFS 遍历。
# 当前做法不是最优解，是否可以考虑双端 BFS 优化，或者迪杰斯塔拉算法?
# 代码
# 如果不存在这样的转换序列，返回一个空列表。
# 所有单词具有相同的⻓度。
# 所有单词只由小写字母组成。
# 字典中不存在重复的单词。
#          package leetcode
# func findLadders(beginWord string, endWord string, wordList []string) []
# []string {
#   result, wordMap := make([][]string, 0), make(map[string]bool)
#   for _, w := range wordList {
#     wordMap[w] = true
#   }
#   if !wordMap[endWord] {
#     return result
# }
#   // create a queue, track the path
#   queue := make([][]string, 0)
#   queue = append(queue, []string{beginWord})
#   // queueLen is used to track how many slices in queue are in the same level
#   // if found a result, I still need to finish checking current level cause I
# need to return all possible paths
#   queueLen := 1
#   // use to track strings that this level has visited
#   // when queueLen == 0, remove levelMap keys in wordMap
#   levelMap := make(map[string]bool)
#   for len(queue) > 0 {
# path := queue[0]

#       queue = queue[1:]
#     lastWord := path[len(path)-1]
#     for i := 0; i < len(lastWord); i++ {
#       for c := 'a'; c <= 'z'; c++ {
#         nextWord := lastWord[:i] + string(c) + lastWord[i+1:]
#         if nextWord == endWord {
#           path = append(path, endWord)
#           result = append(result, path)
#           continue
#         }
#         if wordMap[nextWord] {
#           // different from word ladder, don't remove the word from wordMap
# immediately
#           // same level could reuse the key.
#           // delete from wordMap only when currently level is done.
#           levelMap[nextWord] = true
#           newPath := make([]string, len(path))
#           copy(newPath, path)
#           newPath = append(newPath, nextWord)
#           queue = append(queue, newPath)
# } }
# }
# queueLen--
#     // if queueLen is 0, means finish traversing current level. if result is
# not empty, return result
#     if queueLen == 0 {
#       if len(result) > 0 {
#         return result
#       }
#       for k := range levelMap {
#         delete(wordMap, k)
# }
#       // clear levelMap
#       levelMap = make(map[string]bool)
#       queueLen = len(queue)
#     }
# }
#   return result
# }
# 127. Word Ladder
# 题目
# Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
 
#  1. Only one letter can be changed at a time.
# 2. Each transformed word must exist in the word list. Note that beginWord is not a transformed
# word. Note:
# Return 0 if there is no such transformation sequence. All words have the same length.
# All words contain only lowercase alphabetic characters. You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same. Example 1:
#        Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
# Output: 5
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
# Example 2:
#   Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
# Output: 0
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
# 题目大意
# 给定两个单词(beginWord 和 endWord)和一个字典，找到从 beginWord 到 endWord 的最短转换 序列的⻓度。转换需遵循如下规则:
# 1. 每次转换只能改变一个字母。
# 2. 转换过程中的中间单词必须是字典中的单词。
# 说明:
# 如果不存在这样的转换序列，返回 0。 所有单词具有相同的⻓度。 所有单词只由小写字母组成。
   
# 字典中不存在重复的单词。
# 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
# 解题思路
# 这一题要求输出从 beginWord 变换到 endWord 最短变换次数。可以用 BFS，从 beginWord 开 始变换，把该单词的每个字母都用 'a'~'z' 变换一次，生成的数组到 wordList 中查找，这里
# 用 Map 来记录查找。找得到就入队列，找不到就输出 0 。入队以后按照 BFS 的算法依次遍历完， 当所有单词都 len(queue)<=0 出队以后，整个程序结束。
#   这一题题目中虽然说了要求找到一条最短的路径，但是实际上最短的路径的寻找方法已经告诉你
#   了:
# 1. 每次只变换一个字母
# 2. 每次变换都必须在 wordList 中
#      所以不需要单独考虑何种方式是最短的。