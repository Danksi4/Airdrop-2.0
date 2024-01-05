import bitio
import huffman
import pickle


def read_tree(tree_stream):
    '''Read a description of a Huffman tree from the given compressed
    tree stream, and use the pickle module to construct the tree object.
    Then, return the root node of the tree itself.

    Args:
      tree_stream: The compressed stream to read the tree from.

    Returns:
      A Huffman tree root constructed according to the given description.
    '''
    tree=pickle.load(tree_stream)
    root=huffman.make_encoding_table(tree)
    return root


def decode_byte(tree, bitreader):
    """
    Reads bits from the bit reader and traverses the tree from
    the root to a leaf. Once a leaf is reached, bits are no longer read
    and the value of that leaf is returned.

    Args:
      bitreader: An instance of bitio.BitReader to read the tree from.
      tree: A Huffman tree.

    Returns:
      Next byte of the compressed bit stream.
    """
    path=()
    invmaptree=dict((v,k) for k, v in tree.items()) #Inverts the tree so the path is assigned as the keys, this allows us to 
    #find the value of what is stored in the tree using the path
    while path not in invmaptree: #loops this proccess until it encounters an existing path, so the value end up being the desired leaf.
      bit=bitreader.readbit()
      if bit == 0:
        path=path+(False,)
      if bit == 1:
        path=path+(True,)
    value=invmaptree[path] #Uses the path as the key to produce the value associated with the path in the tree
    return(value)


def decompress(compressed, uncompressed):
    '''First, read a Huffman tree from the 'compressed' stream using your
    read_tree function. Then use that tree to decode the rest of the
    stream and write the resulting symbols to the 'uncompressed'
    stream.

    Args:
      compressed: A file stream from which compressed input is read.
      uncompressed: A writable file stream to which the uncompressed
          output is written.
    '''
    tree=read_tree(compressed)
    bitreader=bitio.BitReader(compressed) #initializes bitreader object
    bitwriter=bitio.BitWriter(uncompressed) #initializes bitwriter object
    byte=0
    while True:
       byte=decode_byte(tree,bitreader)
       if byte == None:
          break
       else:
          bitwriter.writebits(byte,8) #writes 8 bits to the output stream
    


def write_tree(tree, tree_stream):
    '''Write the specified Huffman tree to the given tree_stream
    using pickle.

    Hint:  Use pickle.dump()
    **Requirement:**  pickle.dump(..., protocol=4)

    Args:
      tree: A Huffman tree.
      tree_stream: The binary file to write the tree to.
    '''
    pickle.dump(tree,tree_stream,protocol=4)
    


def compress(tree, uncompressed, compressed):
    '''First write the given tree to the stream 'compressed' using the
    write_tree function. Then use the same tree to encode the data
    from the input stream 'uncompressed' and write it to 'compressed'.
    If there are any partially-written bytes remaining at the end,
    write 0 bits to form a complete byte.

    Flush the bitwriter after writing the entire compressed file.

    Args:
      tree: A Huffman tree.
      uncompressed: A file stream from which you can read the input.
      compressed: A file stream that will receive the tree description
          and the coded input data.
    '''
    write_tree(tree,compressed)
    root=huffman.make_encoding_table(tree)
    bitreader=bitio.BitReader(uncompressed)
    bitwriter=bitio.BitWriter(compressed)
    byte=0
    while byte!= None:
        try:
          byte=bitreader.readbits(8)
          for bit in root[byte]:
            bitwriter.writebit(bit)
        except EOFError:
          byte=None
          for bit in root[None]:
            bitwriter.writebit(bit)
          

    

    

   