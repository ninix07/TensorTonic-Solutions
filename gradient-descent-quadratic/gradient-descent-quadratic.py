def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for _ in range(steps+1):
        del_f= 2*a*x0+ b
        x0=x0- lr* del_f

    return x0
        