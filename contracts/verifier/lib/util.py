import pyteal as pt
from typing import get_args


# Checks literals to make sure the size matches what we expect
def check_size(t: type, ks: int):
    size = get_args(get_args(t)[0])[0]
    assert size == ks, f"Type {t} expected {ks} but got {size}"


def encode(tuple_field: pt.abi.Field) -> pt.Expr:
    return pt.Seq(
        tuple_field.store_into(tmp := tuple_field.produced_type_spec().new_instance()),
        tmp.encode(),
    )
