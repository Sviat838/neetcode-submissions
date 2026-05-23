class Solution:

    # def encode(self, strs: List[str]) -> str:
    #     if strs:
    #         encoded_str = '/|\\'.join(strs)
    #     else:
    #         encoded_str = 'EMPTY'

    #     return encoded_str

    # def decode(self, s: str) -> List[str]:
    #     if s=='EMPTY':
    #         decoded_str = []
    #     elif s != '':
    #         decoded_str = s.split('/|\\')
    #     else:
    #         decoded_str = ['']

    #     return decoded_str

    def encode(self, strs: List[str]) -> str:


        if not strs:
            return ''

        words = strs[0]
        encoded_str = str(len(strs.pop(0)))

        for s in strs:
            encoded_str += ',' + str(len(s))
            words += s

        encoded_str += '#' + words

        return encoded_str


    def decode(self, s: str) -> List[str]:

        if not s:
            return []

        decoded_str = []

        lengths = s.split('#', 1)[0].split(',')

        words = s.split('#', 1)[1]

        while lengths:
            cur_length = int(lengths.pop(0))

            if cur_length == 0:
                decoded_str.append('')
            else:
                decoded_str.append(words[:cur_length])

            words = words[cur_length:]



        return decoded_str



    