from eth import constants
from eth.db.atomic import AtomicDB
from eth.db.chain import ChainDB
from eth.rlp.headers import BlockHeader
from eth.vm.base import VM


def get_vm(vm_class: VM):
    header = BlockHeader(
        difficulty=1,
        gas_limit=8000000,
        gas_used=0,
        bloom=0,
        mix_hash=constants.ZERO_HASH32,
        nonce=constants.GENESIS_NONCE,
        block_number=0,
        parent_hash=constants.ZERO_HASH32,
        receipt_root=constants.BLANK_ROOT_HASH,
        uncles_hash=constants.EMPTY_UNCLE_HASH,
        timestamp=0,
        transaction_root=constants.BLANK_ROOT_HASH,
    )
    vm = vm_class(header, ChainDB(AtomicDB()))
    return vm
