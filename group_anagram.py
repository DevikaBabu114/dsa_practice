#Given an array of strings strs, group the anagrams together. You can return the answer in any order.(leetcode-49)

def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_groups={}
        for str in strs:
            sorted_str="".join(sorted(str))
            if sorted_str in anagram_groups:
                anagram_groups[sorted_str].append(str)
            else:
                anagram_groups[sorted_str]=[str]
        result=[]
        for  group in  anagram_groups.values():
            result.append(group)
        return result

    
n=int(input("no of string:"))
string_list=list(input("strings:").split())
print(groupAnagrams(n,string_list))