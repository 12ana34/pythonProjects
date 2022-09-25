h=input('Enter hours: ')
r=input('Enter rate per hour: ')
try:
    fh=float(h)
    fr=float(r)
except:
    print('Error, please enter numeric input!')
    quit()
def computepay(fh,fr):
    if fh>40:
        return((40*fr)+((fh-40)*(fr*1.5)))
    else:
        return(fh*fr)
p=computepay(fh,fr)
print('Gross pay: ', p)