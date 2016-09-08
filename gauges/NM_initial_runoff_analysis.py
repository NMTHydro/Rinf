# ===============================================================================
# Copyright 2016 dgketchum
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

"""
The purpose of this module is to plot guage discharge,  precip, and (eventually) ETRM runoff from selected NM basins.



dgketchum 24 JUL 2016
"""

import os
from pandas import DataFrame
from numpy import loadtxt
from datetime import datetime
import matplotlib.pyplot as plt


def compare_ppt_discharge(combo_path):

    os.chdir(combo_path)
    combo_files = os.listdir(combo_path)
    data_dict = {}
    for item in combo_files:
        gauge_key = item[:8]
        start_yr_str, end_yr_str = item[-13:-4].split('_')
        start, end = datetime(start_yr_str, 0, 0), datetime(end_yr_str, 0, 0)
        # csv in format: [YYY/MM/DD, q[cfs], ppt[m**3] #
        # no headers in them #
        arr_cols = ['Date', 'Discharge_[cfs]', 'Precipitation_[m^3]']
        col_check = loadtxt(item, dtype=str, skiprows=0, delimiter=',', usecols=arr_cols)
        print 'headers being read: \n {}'.format(col_check[:1, :])
        csv = loadtxt(item, dtype=str, skiprows=3, delimiter=',', usecols=arr_cols)
        amf_data = append(amf_data, csv, axis=0)

        df = DataFrame(amf_data, index=new_ind, columns=columns)


if __name__ == '__main__':
    home = os.path.expanduser('~')
    print 'home: {}'.format(home)
    gauges = os.path.join(home, 'Documents', 'Recharge', 'Gauges')
    q_ppt_data_path = os.path.join(gauges, 'BasinPPT_GaugeQ_NM')
    q_path = os.path.join(gauges, 'GaugeQ')
    compare_ppt_discharge(q_ppt_data_path)

# ============= EOF =============================================
    



