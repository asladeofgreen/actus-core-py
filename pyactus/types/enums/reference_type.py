# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import enum


class ReferenceType(enum.Enum):
    """RTP :: Reference Type.

    The type of the referencing object

    """
    # Contract :: The reference represents an actual contract
    CNT = 0

    # Contract Identifier :: The reference represents an identifier of an actual contract
    CID = 1

    # Market Object Identifier :: The reference represents the identifier of a market object
    MOC = 2

    # Legal Entity Identifier :: The reference represents the identifier of a legal entity
    EID = 3

    # Contract Structure :: The reference represents a ContractStructure
    CST = 4

