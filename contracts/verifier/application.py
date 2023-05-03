import pyteal as pt
import beaker as bkr

from .lib.bls12_381 import (
    Inputs,
    Proof,
    VerificationKey,
    G1,
    compute_linear_combination,
    valid_pairing,
)

_vk_box_name = "vk"
vk_box_name = pt.Bytes(_vk_box_name)
opup = pt.OpUp(pt.OpUpMode.OnCall)

app = bkr.Application("Verifier", build_options=bkr.BuildOptions(avm_version=10))


@app.update(authorize=bkr.Authorize.only(pt.Global.creator_address()))
def update():
    return pt.Approve()


@app.external(authorize=bkr.Authorize.only(pt.Global.creator_address()))
def bootstrap(vk: VerificationKey):
    # write the VK to box storage
    return pt.BoxPut(vk_box_name, vk.encode())


@app.external
def verify(inputs: Inputs, proof: Proof, *, output: pt.abi.Bool):
    return pt.Seq(
        # idk if this will need to change but its enough for now
        opup.ensure_budget(pt.Int(13500)),
        # Fetch the VK from box storage
        get_vk(output=(vk := VerificationKey())),  # type: ignore
        # Compute vk_x from sum of inputs
        (vk_x := pt.abi.make(G1)).decode(compute_linear_combination(vk, inputs)),
        # return result (normal programs should assert out if its invalid)
        output.set(valid_pairing(proof, vk, vk_x)),
    )


def get_vk(*, output: VerificationKey):
    # Read in the VK from our box
    return pt.Seq(
        vk_data := pt.BoxGet(vk_box_name),
        pt.Assert(vk_data.hasValue(), comment="Verification Key not set"),
        output.decode(vk_data.value()),
    )
