from functions import give_codontruth
from functions import give_simplemodel

def SMAC():
    print '-' * 72
    print '|' + ' ' * 11 + 'SMAC (Simple Model Aminoacid Checker) version 1' + ' ' * 11 + '|'
    print '-' * 72
    print '| X := Atom | (~X) | (X&X) | (XvX) | (X>X) | (dX) | (bX)' + ' ' * 15 + '|'
    print '| Atoms: A, R, N, D, C, Q, E, G, H, I, L, K, M, F, P, S, T, W, Y, V, *' + ' ' + '|'
    print '| Examples: E, (~W), (~(E&(~E))), (d((bD)>(d((dE)v(~K)))))' + ' ' * 13 + '|'
    print '-' * 72
    simplemodel = give_simplemodel()
    print 'Verbose(Y/N)'
    answer = raw_input()
    if answer == 'Y':
        verbose = 1
    else:
        verbose = 0
    while True:
        print 'Specifiy codon:'
        codon = raw_input()
        print 'Specifiy formula:'
        formula = raw_input()
        give_codontruth(simplemodel, codon, formula, verbose)
        print 'Again? (Y/N)'
        answer = raw_input()
        if answer != 'Y':
            raise SystemExit(0)

SMAC()

#Copyright 2016 Maximilian Huber

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

#http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
