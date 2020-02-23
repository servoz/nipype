# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from ..brains import JointHistogram


def test_JointHistogram_inputs():
    input_map = dict(
        args=dict(argstr="%s",),
        environ=dict(nohash=True, usedefault=True,),
        inputMaskVolumeInXAxis=dict(
            argstr="--inputMaskVolumeInXAxis %s", extensions=None,
        ),
        inputMaskVolumeInYAxis=dict(
            argstr="--inputMaskVolumeInYAxis %s", extensions=None,
        ),
        inputVolumeInXAxis=dict(argstr="--inputVolumeInXAxis %s", extensions=None,),
        inputVolumeInYAxis=dict(argstr="--inputVolumeInYAxis %s", extensions=None,),
        outputJointHistogramImage=dict(argstr="--outputJointHistogramImage %s",),
        verbose=dict(argstr="--verbose ",),
    )
    inputs = JointHistogram.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value


def test_JointHistogram_outputs():
    output_map = dict()
    outputs = JointHistogram.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
