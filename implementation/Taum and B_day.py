
def taumBday(b, w, bc, wc, z):
    # Write your code here
    if wc+z < bc:
        result = ((wc+z)*b)+(wc*w)
    elif bc+z < wc:
        result = ((bc+z)*w)+(bc*b)
    else:
        result = (bc*b)+(wc*w)
    return result