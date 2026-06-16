def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here

    return_chunks = []

    for i in range(0,len(tokens),chunk_size-overlap):
        return_chunks.append(tokens[i:i+chunk_size])
        if i+chunk_size >=len(tokens):
            break

    return return_chunks