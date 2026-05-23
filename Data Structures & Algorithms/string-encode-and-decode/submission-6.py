class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            encoded_str = '/|\\'.join(strs)
        else:
            encoded_str = 'EMPTY'
        print('encoded_str = ' + encoded_str)
        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s=='EMPTY':
            decoded_str = []
        elif s != '':
            decoded_str = s.split('/|\\')
        else:
            decoded_str = ['']

        return decoded_str


    