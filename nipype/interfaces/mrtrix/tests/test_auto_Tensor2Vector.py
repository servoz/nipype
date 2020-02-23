# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..preprocess import Tensor2Vector


def test_Tensor2Vector_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        debug=dict(argstr="-debug", position=1,),
        environ=dict(nohash=True, usedefault=True,),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=-2,),
        out_filename=dict(argstr="%s", extensions=None, genfile=True, position=-1,),
        quiet=dict(argstr="-quiet", position=1,),
    )
    inputs = Tensor2Vector.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Tensor2Vector_outputs():
    output_map = dict(vector=dict(extensions=None,),)
    outputs = Tensor2Vector.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
