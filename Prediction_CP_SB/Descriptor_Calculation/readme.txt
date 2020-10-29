A workflow for the Descriptor calculation.

Installation and dependencies
1)	KNIME (https://www.knime.com/) >= 3.7.0
Usage
1)	Download the workflow and load it into your knime installation.
2)	Double click on the ‘SDF Reader’: ‘Molecule_file’ node and add path for the .sdf file for which the descriptors are to be calculated. This will calculate following 26 physicochemical properties: SlogP, SMR, LabuteASA, TPSA, AMW, ExactMW, NumLipinskiHBA, NumLipinskiHBD, NumRotatableBonds, NumHBD, NumHBA, NumAmideBonds, NumHeteroAtoms, NumHeavyAtoms, NumAtoms, NumRings, NumAromaticRings, NumSaturatedRings, NumAliphaticRings, NumAromaticHeterocycles, NumSaturatedHeterocycles, NumAliphaticHeterocycles, NumAromaticCarbocycles, NumSaturatedCarbocycles, NumAliphaticCarbocycles, FractionCSP3.
3)	Double click on the ‘CSV Writer’: ‘write descriptor file’ node and add the path and name of the output file that would containing calculated descriptor.
