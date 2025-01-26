#! /usr/bin/env python
#

import os
import sys

from lmtoy import runs

project="2024-S1-MX-34"

#        obsnums per source (make it negative if not added to the final combination)
on = {}
on['NGC4447'] = [110632, 110637, 
                 125295, 125297, 125301, 125303,      # 21-jan-2025
                 125362, 125364, 125366,
                 ]

#        common parameters per source on the first dryrun (run1a, run2a)
pars1 = {}
#pars1['NGC4447']   = "dv=100 dw=150 pix_list=0,2 b_order=3 map_coord_use=0 bank=0"
pars1['NGC4447']   = "dv=100 dw=150 pix_list=0,2 b_order=3 bank=0"

#        common parameters per source on subsequent runs (run1b, run2b)
pars2 = {}
pars2['NGC4447']   = "srdp=1 admit=0"

if __name__ == '__main__':    
    runs.mk_runs(project, on, pars1, pars2, None, sys.argv)
