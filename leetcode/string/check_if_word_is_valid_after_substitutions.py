# We are given that the string "abc" is valid.
# From any valid string V, we may split V into two pieces X and Y such that X + Y (X concatenated withY)isequaltoV. (XorYmaybeempty.) Then,X+"abc"+Yisalsovalid.
# If for example S = "abc", then examples of valid strings are: "abc", "aabcbc", "abcabc", "abcabcababcc". Examples of invalid strings are: "abccba", "ab", "cababc", "bac".
# Return true if and only if the given string S is valid.