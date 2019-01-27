import os

from lark import Lark, Transformer, v_args

dir_ = os.path.dirname(os.path.realpath(__file__))


class Container(list):
    def __init__(self, *args):
        super(Container, self).__init__(args)


class PCADTransformer(Transformer):
    array = list

    def start(self, tokens):
        return tokens

    # v_args means s is supplied individually and not within a list
    @v_args(inline=True)
    def string(self, s):
        v = s[1:-1].replace('\\"', '"')
        return v

    @v_args(inline=True)
    def name(self, s):
        v = s[0:]
        return v


if __name__ == "__main__":
    f_in = os.path.join(dir_, "..\\test\\data\\pcad_short.NET")
    f_tree = os.path.join(dir_, "..\\test\\data\\pcad_short_tree.txt")

    with open(f_in, 'r') as f:
        text = f.read()

    kwargs = dict(rel_to=__file__)
    pcad_parser = Lark.open('pcad.lark', parser='lalr', **kwargs)
    tree = pcad_parser.parse(text)

    with open(f_tree, 'w') as f:
        f.write(tree.pretty())

    # print(tree.pretty())
    objs = PCADTransformer().transform(tree)
    print(objs)
