def read_lines(filename):
    MODE_READ = 'r'
    lines = []
    with open(filename, MODE_READ) as input_file:
        for line in input_file:
            line = line.rstrip()
            lines.append(line)
    # FILL IN
    return lines

def enqueue(waitlist, customer): 
    waitlist.append(customer)

def dequeue(waitlist):
    del waitlist [0]

def display_waitlist(waitlist):
    status = 'Customers waiting: '
    print(status, end = '')
    print(*waitlist, sep = ', ')

def main():
    NEXT = 'NEXT'
    filename = 'customer_queue.txt'
    lines = read_lines(filename)
    waitlist = []
    for customer in lines:
        if customer == NEXT:
            dequeue(waitlist)
            display_waitlist(waitlist)
        else:
            enqueue(waitlist,customer)
            display_waitlist(waitlist)
    # FILL IN

    print('Done!')
main()
