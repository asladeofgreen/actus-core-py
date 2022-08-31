# **********************************
# N.B. Auto-generated using actus-mp
# **********************************
import enum


class ContractType(enum.Enum):
    """CT :: Contract Type.

    The ContractType is the most important information. It defines the cash flow generating pattern of a contract. The ContractType information in combination with a given state of the risk factors will produce a deterministic sequence of cash flows which are the basis of any financial analysis.

    """
    # Principal at Maturity :: Lending agreements with full amortization at maturity.
    PAM = 0

    # Annuity :: Lending agreements with fixed periodic payments consisting of an interest and principal portion. The periodic payments are adjusted for variable rate instruments such that maturity remains fixed.
    ANN = 1

    # Negative Amortizer :: Lending agreements with fixed periodic payments consisting of an interest and principal portion. Maturity changes for variable rate instruments.
    NAM = 2

    # Linear Amortizer :: Lending agreements with fixed principal repayment amounts and variable interest payments.
    LAM = 3

    # Exotic Linear Amortizer :: Lending agreements with exotic repayment schedules.
    LAX = 4

    # Call Money :: Lonas that are rolled over as long as they are not called. Once called it has to be paid back after the stipulated notice period.
    CLM = 5

    # Undefined Maturity Profile :: Interest paying cash accounts (current / savings / etc.).
    UMP = 6

    # Cash :: Represents cash holdings.
    CSH = 7

    # Stock :: Represents stocks/shares/equity.
    STK = 8

    # Commodity :: Represents commodities.
    COM = 9

    # Swap :: An agreement of swapping two legs such as fixed against variable or currency 1 against currency 2 etc.
    SWAPS = 10

    # Plain Vanilla Swap :: Plain vanilla interest rate swaps.
    SWPPV = 11

    # Foreign Exchange Outright :: An agreement of swapping two cash flows in different currencies at a future point in time.
    FXOUT = 12

    # Cap and Floor :: An agreement of paying the differential (cap or floor) of a reference rate versus a fixed rate.
    CAPFL = 13

    # Future :: An agreement of exchanging an underlying instrument against a fixed price in the future.
    FUTUR = 14

    # Option :: Different types of options on buying an underlying instrument at a fixed price in the future.
    OPTNS = 15

    # Credit Enhancement Guarantee :: A guarantee / letter of credit by a third party on the scheduled payment obligations of an underlying instrument
    CEG = 16

    # Credit Enhancement Collateral :: A collateral securing the scheduled payment obligations of an underlying instrument
    CEC = 17

    # Exotic Annuity :: Exotic version of ANN However step ups with respect to (i) Principal, (ii) Interest rates are possible. Highly flexible to match totally irregular principal payments. Principal can also be paid out in steps.
    ANX = -1

    # Convertible Note :: Bonds with a call or put option. If option is exercised, underlying bond ceases to exist.
    BNDCP = -2

    # Warrant :: Bonds with a warrant. If option is exercised, underlying bond continues to exist.
    BNDWR = -3

    # Credit Default Swap :: A payment is triggered if one or more of the ndelying counterparties defaults.
    CDSWP = -4

    # Credit Linked Note :: A credit linked note is a security with an embedded CDSWP
    CLNTE = -5

    # Margining :: A Margining contract traces the value changes and the different margin categories like inital and variation margin.
    MAR = -6

    # Exotic Negative Amortizer :: Exotic version of NAM However step ups with respect to (i) Principal, (ii) Interest rates are possible. Highly flexible to match totally irregular principal payments. Principal can also be paid out in steps.
    NAX = -7

    # Perpetual Bonds :: Bonds without any maturity date. Interest is paid into eternity if is not terminated.
    PBN = -8

    # Repurchase Agreement :: A Repo contract controls and manages the sale and repurchase of assets on the books.
    REP = -9

    # Securitization Credit Risk :: Securitiazion contracts where contracs are ranked according to credit default. The lower ranked tranches are hit by the first defaults. Only when the lowest tranches are wiped out, the next higher tranch is hit.
    SCRCR = -10

    # Securitization Market Risk :: Securitiazion contracts where all underlying contracts are treated equal. The buyer of a tranche gets a part of the cash-flows.
    SCRMR = -11

    # Total Return Swap :: A total return swap is a swap agreement in which one party makes payments based on a set rate, either fixed or variable, while the other party makes payments based on the return of an underlying asset, which includes both the income it generates and any capital gains.
    TRSWP = -12

