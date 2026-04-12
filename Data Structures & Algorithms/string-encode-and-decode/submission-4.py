class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs):
            return '||'.join(strs)
        else:
            return 'empty'

    def decode(self, s: str) -> List[str]:
        if s == 'empty':
            return list()
        else:
            return s.split('||')
        
