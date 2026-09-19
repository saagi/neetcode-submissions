class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict_map={}
        for num in nums:
            dict_map[num] = dict_map.get(num,0)+1
        listpairs = []
        for number,freq in dict_map.items():
            listpairs.append([freq,number])
        # sorted_freq = sorted([item for listpairs[item][0] in range(len(listpairs))])
        listpairs.sort(key=lambda x: x[0])
        output=[]
        for i in range(k):
            output.append(listpairs[-1-i][1])

        return output
        
        



        