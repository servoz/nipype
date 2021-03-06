# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..registration import Rigid


def test_Rigid_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fixed_file=dict(
            argstr="%s",
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=0,
        ),
        ftol=dict(
            argstr="%g",
            mandatory=True,
            position=4,
            usedefault=True,
        ),
        initialize_xfm=dict(
            argstr="%s",
            copyfile=True,
            extensions=None,
            position=5,
        ),
        moving_file=dict(
            argstr="%s",
            copyfile=False,
            extensions=None,
            mandatory=True,
            position=1,
        ),
        sampling_xyz=dict(
            argstr="%g %g %g",
            mandatory=True,
            position=3,
            usedefault=True,
        ),
        similarity_metric=dict(
            argstr="%s",
            mandatory=True,
            position=2,
            usedefault=True,
        ),
    )
    inputs = Rigid.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Rigid_outputs():
    output_map = dict(
        out_file=dict(
            extensions=None,
        ),
        out_file_xfm=dict(
            extensions=None,
        ),
    )
    outputs = Rigid.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
