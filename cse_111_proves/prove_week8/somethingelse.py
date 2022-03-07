"""
    "Ac", "Actinium", 227
    "Ag", "Silver", 107.8682
    "Al", "Aluminum", 26.9815386    
    "Ar","Argon",	39.948
    "As","Arsenic",	74.9216                   
    "At","Astatine",	210
    "Au","Gold",	196.966569
    "B","Boron",	10.811
    "Ba","Barium",	137.327
    "Be","Beryllium",	9.012182
    "Bi","Bismuth",	208.9804
    "Br","Bromine",	79.904
    "C","Carbon",	12.0107
    "Ca","Calcium",	40.078
    "Cd","Cadmium",	112.411
    "Ce","Cerium",	140.116
    "Cl","Chlorine",	35.453
    "Co","Cobalt",	58.933195
    "Cr","Chromium",	51.9961
    "Cs","Cesium",	132.9054519
    "Cu","Copper",	63.546
    "Dy","Dysprosium",	162.5
    "Er","Erbium",	167.259
    "Eu","Europium",	151.964
    "F","Fluorine",	18.9984032
    "Fe","Iron",	55.845
    "Fr","Francium",	223
    "Ga","Gallium",	69.723
    "Gd","Gadolinium",	157.25
    "Ge","Germanium",	72.64
    "H","Hydrogen",	1.00794
    "He","Helium",	4.002602
    "Hf","Hafnium",	178.49
    "Hg","Mercury",	200.59
    "Ho","Holmium",	164.93032
    "I","Iodine",	126.90447
    "In","Indium",	114.818
    "Ir","Iridium",	192.217
    "K","Potassium",	39.0983
    "Kr","Krypton",	83.798
    "La","Lanthanum",	138.90547
    "Li","Lithium",	6.941
    "Lu","Lutetium",	174.9668
    "Mg","Magnesium",	24.305
    "Mn","Manganese",	54.938045
    "Mo","Molybdenum",	95.96
    "N","Nitrogen",	14.0067
    "Na","Sodium",	22.98976928
    "Nb","Niobium",	92.90638
    "Nd","Neodymium",	144.242
    "Ne","Neon",	20.1797
    "Ni","Nickel",	58.6934
    "Np","Neptunium",	237
    "O","Oxygen",	15.9994
    "Os","Osmium",	190.23
    "P","Phosphorus",	30.973762
    "Pa","Protactinium",	231.03588
    "Pb","Lead",	207.2
    "Pd","Palladium",	106.42
    "Pm","Promethium",	145
    "Po","Polonium",	209
    "Pr","Praseodymium",	140.90765
    "Pt","Platinum",	195.084
    "Pu","Plutonium",	244
    "Ra","Radium",	226
    "Rb","Rubidium",	85.4678
    "Re","Rhenium",	186.207
    "Rh","Rhodium",	102.9055
    "Rn","Radon",	222
    "Ru","Ruthenium",	101.07
    "S","Sulfur",	32.065
    "Sb","Antimony",	121.76
    "Sc","Scandium",	44.955912
    "Se","Selenium",	78.96
    "Si","Silicon",	28.0855
    "Sm","Samarium",	150.36
    "Sn","Tin",	118.71
    "Sr","Strontium",	87.62
    "Ta","Tantalum",	180.94788
    "Tb","Terbium",	158.92535
    "Tc","Technetium",	98
    "Te","Tellurium",	127.6
    "Th","Thorium",	232.03806
    "Ti","Titanium",	47.867
    "Tl","Thallium",	204.3833
    "Tm","Thulium",	168.93421
    "U","Uranium",	238.02891
    "V","Vanadium",	50.9415
    "W","Tungsten",	183.84
    "Xe","Xenon",	131.293
    "Y","Yttrium",	88.90585
    "Yb","Ytterbium",	173.054
    "Zn","Zinc",	65.38
    "Zr","Zirconium",	91.224

"""

elementList = [
    {"symbol" = "Ac", "name" = "Actinium", 227   }
    {"symbol" = "Ag", "name" = "Silver", 107.8682}
    {"symbol" = "Al", "name" = "Aluminum",26.9815386    }
    {"symbol" = "Ar", "name" = "Argon", 39.948}
    {"symbol" = "As", "name" = "Arsenic",	74.9216            }       
    {"symbol" = "At", "name" = "Astatine",	210}
    {"symbol" = "Au", "name" = "Gold",	196.966569}
    {"symbol" = "B"," "name" = Boron",	10.811}
    {"symbol" = "Ba", "name" = "Barium",	137.327}
    {"symbol" = "Be", "name" = "Beryllium",	9.012182}
    {"symbol" = "Bi", "name" = "Bismuth",	208.9804}
    {"symbol" = "Br", "name" = "Bromine",	79.904}
    {"symbol" = "C"," "name" = Carbon",	12.0107}
    {"symbol" = "Ca", "name" = "Calcium",	40.078}
    {"symbol" = "Cd", "name" = "Cadmium",	112.411}
    {"symbol" = "Ce", "name" = "Cerium",	140.116}
    {"symbol" = "Cl", "name" = "Chlorine",	35.453}
    {"symbol" = "Co", "name" = "Cobalt",	58.933195}
    {"symbol" = "Cr", "name" = "Chromium",	51.9961}
    {"symbol" = "Cs", "name" = "Cesium",	132.9054519}
    {"symbol" = "Cu", "name" = "Copper",	63.546}
    {"symbol" = "Dy", "name" = "Dysprosium",	162.5}
    {"symbol" = "Er", "name" = "Erbium",	167.259}
    {"symbol" = "Eu", "name" = "Europium",	151.964}
    {"symbol" = "F"," "name" = Fluorine",	18.9984032}
    {"symbol" = "Fe", "name" = "Iron",	55.845}
    {"symbol" = "Fr", "name" = "Francium",	223}
    {"symbol" = "Ga", "name" = "Gallium",	69.723}
    {"symbol" = "Gd", "name" = "Gadolinium",	157.25}
    {"symbol" = "Ge", "name" = "Germanium",	72.64}
    {"symbol" = "H"," "name" = Hydrogen",	1.00794}
    {"symbol" = "He", "name" = "Helium",	4.002602}
    {"symbol" = "Hf", "name" = "Hafnium",	178.49}
    {"symbol" = "Hg", "name" = "Mercury",	200.59}
    {"symbol" = "Ho", "name" = "Holmium",	164.93032}
    {"symbol" = "I"," "name" = Iodine",	126.90447}
    {"symbol" = "In", "name" = "Indium",	114.818}
    {"symbol" = "Ir", "name" = "Iridium",	192.217}
    {"symbol" = "K"," "name" = Potassium",	39.0983}
    {"symbol" = "Kr", "name" = "Krypton",	83.798}
    {"symbol" = "La", "name" = "Lanthanum",	138.90547}
    {"symbol" = "Li", "name" = "Lithium",	6.941}
    {"symbol" = "Lu", "name" = "Lutetium",	174.9668}
    {"symbol" = "Mg", "name" = "Magnesium",	24.305}
    {"symbol" = "Mn", "name" = "Manganese",	54.938045}
    {"symbol" = "Mo", "name" = "Molybdenum",	95.96}
    {"symbol" = "N"," "name" = Nitrogen",	14.0067}
    {"symbol" = "Na", "name" = "Sodium",	22.98976928}
    {"symbol" = "Nb", "name" = "Niobium",	92.90638}
    {"symbol" = "Nd", "name" = "Neodymium",	144.242}
    {"symbol" = "Ne", "name" = "Neon",	20.1797}
    {"symbol" = "Ni", "name" = "Nickel",	58.6934}
    {"symbol" = "Np", "name" = "Neptunium",	237}
    {"symbol" = "O"," "name" = Oxygen",	15.9994}
    {"symbol" = "Os", "name" = "Osmium",	190.23}
    {"symbol" = "P"," "name" = Phosphorus",	30.973762}
    {"symbol" = "Pa", "name" = "Protactinium",	231.03588}
    {"symbol" = "Pb", "name" = "Lead",	207.2}
    {"symbol" = "Pd", "name" = "Palladium",	106.42}
    {"symbol" = "Pm", "name" = "Promethium",	145}
    {"symbol" = "Po", "name" = "Polonium",	209}
    {"symbol" = "Pr", "name" = "Praseodymium",	140.90765}
    {"symbol" = "Pt", "name" = "Platinum",	195.084}
    {"symbol" = "Pu", "name" = "Plutonium",	244}
    {"symbol" = "Ra", "name" = "Radium",	226}
    {"symbol" = "Rb", "name" = "Rubidium",	85.4678}
    {"symbol" = "Re", "name" = "Rhenium",	186.207}
    {"symbol" = "Rh", "name" = "Rhodium",	102.9055}
    {"symbol" = "Rn", "name" = "Radon",	222}
    {"symbol" = "Ru", "name" = "Ruthenium",	101.07}
    {"symbol" = "S"," "name" = Sulfur",	32.065}
    {"symbol" = "Sb", "name" = "Antimony",	121.76}
    {"symbol" = "Sc", "name" = "Scandium",	44.955912}
    {"symbol" = "Se", "name" = "Selenium",	78.96}
    {"symbol" = "Si", "name" = "Silicon",	28.0855}
    {"symbol" = "Sm", "name" = "Samarium",	150.36}
    {"symbol" = "Sn", "name" = "Tin",	118.71}
    {"symbol" = "Sr", "name" = "Strontium",	87.62}
    {"symbol" = "Ta", "name" = "Tantalum",	180.94788}
    {"symbol" = "Tb", "name" = "Terbium",	158.92535}
    {"symbol" = "Tc", "name" = "Technetium",	98}
    {"symbol" = "Te", "name" = "Tellurium",	127.6}
    {"symbol" = "Th", "name" = "Thorium",	232.03806}
    {"symbol" = "Ti", "name" = "Titanium",	47.867}
    {"symbol" = "Tl", "name" = "Thallium",	204.3833}
    {"symbol" = "Tm", "name" = "Thulium",	168.93421}
    {"symbol" = "U"," "name" = Uranium",	238.02891}
    {"symbol" = "V"," "name" = Vanadium",	50.9415}
    {"symbol" = "W"," "name" = Tungsten",	183.84}
    {"symbol" = "Xe", "name" = "Xenon",	131.293}
    {"symbol" = "Y"," "name" = Yttrium",	88.90585}
    {"symbol" = "Yb", "name" = "Ytterbium",	173.054}
    {"symbol" = "}Zn", "name" = "Zinc",	65.38
    {"symbol" = "Zr", "name" = "Zirconi'symbol = um",	91.224}
]              