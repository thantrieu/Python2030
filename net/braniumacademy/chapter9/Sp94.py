import sys
import argparse
paser = argparse.ArgumentParser()
paser.add_argument('fname', help='Your name')
paser.add_argument('age', help='Your age', type=int)
paser.add_argument('gpa', help='Your gpa', type=float)
paser.add_argument('-a', '--act', help='Action: 1-add.\n2-substract\n3-exponent.', type=int, default=0)
args = paser.parse_args()
print(f'Full name: {args.fname}')
print(f'Age: {args.age}')
print(f'GPA: {args.gpa:0.2f}')
if args.act == 1:
    print('Add')
elif args.act == 2:
    print('Substract')
elif args.act == 3:
    print('Exponent')
else:
    print('Nothing selected.')