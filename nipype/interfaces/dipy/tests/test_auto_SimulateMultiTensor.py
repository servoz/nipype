# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.dipy.simulate import SimulateMultiTensor

def test_SimulateMultiTensor_inputs():
    input_map = dict(baseline=dict(mandatory=True,
    ),
    bvalues=dict(usedefault=True,
    ),
    diff_iso=dict(usedefault=True,
    ),
    diff_sf=dict(usedefault=True,
    ),
    gradients=dict(),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_bval=dict(),
    in_bvec=dict(),
    in_dirs=dict(mandatory=True,
    ),
    in_frac=dict(mandatory=True,
    ),
    in_mask=dict(),
    in_vfms=dict(mandatory=True,
    ),
    n_proc=dict(usedefault=True,
    ),
    num_dirs=dict(usedefault=True,
    ),
    out_bval=dict(usedefault=True,
    ),
    out_bvec=dict(usedefault=True,
    ),
    out_file=dict(usedefault=True,
    ),
    out_mask=dict(usedefault=True,
    ),
    snr=dict(usedefault=True,
    ),
    )
    inputs = SimulateMultiTensor.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_SimulateMultiTensor_outputs():
    output_map = dict(out_bval=dict(),
    out_bvec=dict(),
    out_file=dict(),
    out_mask=dict(),
    )
    outputs = SimulateMultiTensor.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

