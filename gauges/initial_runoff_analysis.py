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
from pandas import DataFrame, to_numeric
from numpy import loadtxt, array
from datetime import datetime
import matplotlib.pyplot as plt


def compare_ppt_discharge(combo_path):

    os.chdir(combo_path)
    combo_files = os.listdir(combo_path)
    data_dict = {}
    for item in combo_files:
        gauge_key = item[:8]
        start_yr_str, end_yr_str = item[-13:-4].split('_')
        start, end = datetime(int(start_yr_str), 1, 1), datetime(int(end_yr_str), 1, 1)
        gauge_name = item.strip('{}_'.format(str(gauge_key))).strip('{}_{}.csv'.format(start_yr_str, end_yr_str))
        # csv in format: [YYY/MM/DD, q[cfs], ppt[m**3] #
        # no headers in them #
        cols = ['Discharge_[cfs]', 'Precipitation_[m^3]']
        csv = loadtxt(item, dtype=str, delimiter=',')
        ind = csv[:, 0]
        data = csv[:, 1:]
        data = array(data, dtype=float)
        df = DataFrame(data, index=ind, columns=cols)
        data_dict[gauge_key] = {'Name': gauge_name, 'Start_End': (start, end), 'Data': df}
        print data_dict



    '''need to find out the name of the variables'''
    for key, series in data_dict.iteritems():
        df = series['Data']
        ax = df.plot(kind='line',subplots=2, title = series['Name'])
        plt.show()
        # plt.subplot(df[:, 0], df[:. 1])
        fig = ax.get_figure()
        #how to call the name here
        fig.savefig()

        # plot time series of discharge and precip #
        # put in two subplots, one of cumulative discharge, the other of cumulative precipitation #
        pass

if __name__ == '__main__':
    #home line
    q_ppt_data_path = os.path.join("e:\\Rinf\\BasinPPT\\")
    compare_ppt_discharge(q_ppt_data_path)
# ============= EOF =============================================




