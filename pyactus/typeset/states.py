# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import dataclasses
import datetime

from pyactus.typeset import enums


@dataclasses.dataclass
class StateSpace():
    """
    A data structure representing various states of a contract.  The states of a 
    contract contain important information used when evaluating payoff. Furthermore, 
    states themselves contain atomic analytical elements such as the nominal value 
    or accrued interest for a lending instrument. On the other hand, states are 
    updated throughout an instrument's lifetime through evaluation of state 
    transition function in the various contract events.
    
    """
    # IPAC :: Accrued Interest :: The current value of accrued interest    
    accrued_interest: float

    # IPAC2 :: Accrued Interest 2 :: The current value of accrued interest of the second leg    
    accrued_interest2: float

    # PRF :: Contract Performance :: Indicates the current Contract Performance status. Different states of the contract range from performing to default.    
    contract_performance: enums.ContractPerformance

    # XA :: Exercise Amount :: The amount fixed for a the contingent event/obligation exercised at Exercise Date    
    exercise_amount: float

    # XD :: Exercise Date :: The timestamp at which a contingent event/obligation is exercised    
    exercise_date: datetime.datetime

    # FEAC :: Fee Accrued :: The current value of accrued fees    
    fee_accrued: float

    # ICBA :: Interest Calculation Base Amount :: The basis at which interest is being accrued. Potentially different from NVL.    
    interest_calculation_base_amount: float

    # SCIP :: Interest Scaling Multiplier :: The multiplier being applied to interest cash flows    
    interest_scaling_multiplier: float

    # MD :: Maturity Date :: The timestamp as per which the contract matures according to the initial terms or as per unscheduled events    
    maturity_date: datetime.datetime

    # PRNXT :: Next Principal Redemption Payment :: The value at which principal is being repaid. This may be including or excluding of interest depending on the Contract Type    
    next_principal_redemption_payment: float

    # IPNR :: Nominal Interest Rate :: The applicable nominal rate    
    nominal_interest_rate: float

    # IPNR2 :: Nominal Interest Rate 2 :: The applicable nominal rate    
    nominal_interest_rate2: float

    # NPD :: Non Performing Date :: The date of the (uncovered) payment event responsible for the current value of the Contract Performance state variable.    
    non_performing_date: datetime.datetime

    # NT :: Notional Principal :: The outstanding nominal value    
    notional_principal: float

    # NT2 :: Notional Principal 2 :: The outstanding nominal value of the second leg    
    notional_principal2: float

    # SCNT :: Notional Scaling Multiplier :: The multiplier being applied to principal cash flows    
    notional_scaling_multiplier: float

    # SD :: Status Date :: The timestamp as per which the state is captured at any point in time    
    status_date: datetime.datetime

    # TD :: Termination Date :: The timestamp of unscheduled termination of a contract    
    termination_date: datetime.datetime

    
    def __str__(self):
        """Instance string representation.
        
        """
        return " | ".join(i for i in self.__dict__.values())