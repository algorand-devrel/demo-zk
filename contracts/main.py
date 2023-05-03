import beaker

import verifier.application as app  # type: ignore

from zokrates import get_proof_and_inputs, get_vk  # type: ignore


def demo(app_id: int = 0):
    acct = beaker.sandbox.get_accounts().pop()
    algod_client = beaker.sandbox.get_algod_client()

    ac = beaker.client.ApplicationClient(
        algod_client, app.app, app_id=app_id, signer=acct.signer
    )

    if app_id == 0:
        app_id, _, _ = ac.create()
        print(f"Created app: {app_id}")
        ac.fund(1000 * beaker.consts.algo)
    else:
        ac.update()

    boxes = [(0, app.VK_BOX_NAME.encode())]

    # Bootstrap with vk
    ac.call(app.bootstrap, vk=get_vk(), boxes=boxes)

    # Pass proof && inputs to be verified
    proof, inputs = get_proof_and_inputs()
    result = ac.call(app.verify, inputs=inputs, proof=proof, boxes=boxes)
    print(f"Contract verified? {result.return_value}")


if __name__ == "__main__":
    app_spec = app.app.build(beaker.sandbox.get_algod_client())
    app_spec.export("artifacts")

    demo()
