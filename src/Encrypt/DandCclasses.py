from testencrypt import fileEncryption
import huffman
import util

'''
-------------------
-------------------
'''
class DandC():
    def __init__(self,file):
        self.file=file
        self.compressedfile=file+'.huf'

    def compressor(self):
        with open(self.file, 'rb') as original:
            freqs=huffman.make_freq_table(original)
            tree=huffman.make_tree(freqs)
            original.seek(0)
            with open(self.compressedfile , 'wb') as smaller:
                util.compress(tree, original, smaller)
        return -1

    def decompressor(self):
        with open(self.compressedfile , 'rb') as comped:
            with open(self.file+'decomp','wb') as decomped:
                util.decompress(comped,decomped)
        return -1
if __name__=='__main__':
    x=DandC('Test.txt')
    x.compressor()
    x.decompressor()





