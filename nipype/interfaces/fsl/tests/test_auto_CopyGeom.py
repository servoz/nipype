# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import CopyGeom


def test_CopyGeom_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        dest_file=dict(
            argstr="%s",
            copyfile=True,
            extensions=None,
            mandatory=True,
            name_source="dest_file",
            name_template="%s",
            output_name="out_file",
            position=1,
        ),
        environ=dict(nohash=True, usedefault=True,),
        ignore_dims=dict(argstr="-d", position="-1",),
        in_file=dict(argstr="%s", extensions=None, mandatory=True, position=0,),
        output_type=dict(),
    )
    inputs = CopyGeom.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_CopyGeom_outputs():
    output_map = dict(out_file=dict(extensions=None,),)
    outputs = CopyGeom.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
