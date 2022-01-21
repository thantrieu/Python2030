import argparse

paser = argparse.ArgumentParser()
paser.add_argument('a', help='First integer number.', type=int)
paser.add_argument('b', help='Second integer number.', type=int)
paser.add_argument('-o', '--option',
                   help='Option: 1-Add. 2-Substract. 3-Multiple. 4-Divide.',
                   type=int, default=1)
args = paser.parse_args()
print(f'a = {args.a}')
print(f'b = {args.b}')
match args.option:
    case 1:
        print(f'{args.a} + {args.b} = {args.a + args.b}')
    case 2:
        print(f'{args.a} - {args.b} = {args.a - args.b}')
    case 3:
        print(f'{args.a} * {args.b} = {args.a * args.b}')
    case 4:
        print(f'{args.a} / {args.b} = {args.a / args.b}')
    case _:
        print('==> Wrong option. Please try again!')
