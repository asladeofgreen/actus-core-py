# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import enum


class ReferenceRole(enum.Enum):
    """RRL :: Reference Role.

    The role of the referencing object

    """
    # Underlying :: The reference represents a simple underlyer contract
    UDL = 0

    # First Leg :: The reference represents the first leg contract
    FIL = 1

    # Second Leg :: The reference represents the second leg contract
    SEL = 2

    # Covered Contract :: The reference represents a contract that is covered under the parent contract
    COVE = 3

    # Covering Contract :: The reference represents a contract that covers for covering contracts under the parent contract Contract
    COVI = 4

