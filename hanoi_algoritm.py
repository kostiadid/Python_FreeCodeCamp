def hanoi_solver(n):
    source = list(range(n, 0, -1))
    middle = []
    end = []

    lines = []
    lines.append(f"{source} {middle} {end}")
    #Start column -> Central
    # Start  to  Target
    #Central to target 
    def move(k, src, central,  target):
        if k == 0:
            return
        #from scr to central
        move(k-1, src,  target, central)
        # scr  to  Target
        target.append(src.pop())
        lines.append(f"{source} {middle} {end}")
        #  from central to   target   
        move(k-1, central, src,  target)

    move(n, source, middle, end)
    return "\n".join(lines)
