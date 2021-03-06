# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..utils import Tkregister2


def test_Tkregister2_inputs():
    input_map = dict(
        args=dict(
            argstr="%s",
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        fsl_in_matrix=dict(
            argstr="--fsl %s",
            extensions=None,
        ),
        fsl_out=dict(
            argstr="--fslregout %s",
        ),
        fstal=dict(
            argstr="--fstal",
            xor=["target_image", "moving_image", "reg_file"],
        ),
        fstarg=dict(
            argstr="--fstarg",
            xor=["target_image"],
        ),
        invert_lta_in=dict(
            requires=["lta_in"],
        ),
        invert_lta_out=dict(
            argstr="--ltaout-inv",
            requires=["lta_in"],
        ),
        lta_in=dict(
            argstr="--lta %s",
            extensions=None,
        ),
        lta_out=dict(
            argstr="--ltaout %s",
        ),
        moving_image=dict(
            argstr="--mov %s",
            extensions=None,
            mandatory=True,
        ),
        movscale=dict(
            argstr="--movscale %f",
        ),
        noedit=dict(
            argstr="--noedit",
            usedefault=True,
        ),
        reg_file=dict(
            argstr="--reg %s",
            extensions=None,
            mandatory=True,
            usedefault=True,
        ),
        reg_header=dict(
            argstr="--regheader",
        ),
        subject_id=dict(
            argstr="--s %s",
        ),
        subjects_dir=dict(),
        target_image=dict(
            argstr="--targ %s",
            extensions=None,
            xor=["fstarg"],
        ),
        xfm=dict(
            argstr="--xfm %s",
            extensions=None,
        ),
    )
    inputs = Tkregister2.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_Tkregister2_outputs():
    output_map = dict(
        fsl_file=dict(
            extensions=None,
        ),
        lta_file=dict(
            extensions=None,
        ),
        reg_file=dict(
            extensions=None,
        ),
    )
    outputs = Tkregister2.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
