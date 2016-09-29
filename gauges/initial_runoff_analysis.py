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
from pandas import DataFrame, concat, Series, date_range
from numpy import loadtxt, array
from datetime import datetime
import matplotlib.pyplot as plt


def compare_ppt_discharge(combo_path, etrm_tabulated):
    """ compare PRISM precipitation, USGS gauge data, and ETRM results.

    :param etrm_tabulated:
    :param combo_path:
    :param etrm_results_path:
    :return:
    """

    etrm_results_list = os.listdir(etrm_tabulated)

    for table in etrm_results_list:

        etrm_name = os.path.basename(table)  # .replace('.csv', '')
        print 'etrm table {}'.format(etrm_name)

        name_list = []
        combo_files = os.listdir(combo_path)
        # combo_files = [comb.replace('.csv', '') for comb in combo_files]
        print 'combo files: {}'.format(combo_files)
        data_dict = {}

        if etrm_name in combo_files:
            print 'found matching table {} and {}'.format(etrm_name, combo_files[combo_files.index(etrm_name)])
            gauge_key = etrm_name[:8]
            start_yr_str, end_yr_str = etrm_name[-13:-4].split('_')
            start, end = datetime(int(start_yr_str), 1, 1), datetime(int(end_yr_str), 1, 1)
            gauge_name = etrm_name.strip('{}_'.format(str(gauge_key))).strip(
                '{}_{}.csv'.format(start_yr_str, end_yr_str))
            # csv in format: [YYY/MM/DD, q[cfs], ppt[m**3] #
            # no headers in them #
            cols = ['q_obs_cbm', 'precip_cbm']
            csv = loadtxt(os.path.join(combo_path, etrm_name), dtype=str, delimiter=',')
            ind = date_range(csv[0, 0], csv[-1, 0])
            data = csv[:, 1:]
            data = array(data, dtype=float)
            df = DataFrame(data, index=ind, columns=cols)
            print 'pre-conversion obs dg: {}'.format(df)
            # convert mean daily cfs to cubic meters per day
            df['q_obs_cbm'] *= 86400 / 35.3147  # sec/day cbm/cft
            print 'gauge ppt obs df: \n{}'.format(df)

            etrm_csv = loadtxt(os.path.join(etrm_tabulated, etrm_name), dtype=str, delimiter=',', skiprows=0,
                               usecols=[0, 2, 4, 6, 8, 10, 12, 14])  # load only odd rows (cubic meters)
            etrm_ind = date_range(etrm_csv[3, 0], etrm_csv[-1, 0])
            etrm_data = etrm_csv[3:, 1:]
            etrm_data = array(etrm_data, dtype=float)
            etrm_cols = etrm_csv[0, 1:]
            etrm_df = DataFrame(etrm_data, index=etrm_ind, columns=etrm_cols)
            print 'etrm df:\n{}'.format(etrm_df)

            start, end = etrm_df.index[0], etrm_df.index[-1]

            df = concat([df, etrm_df], axis=1)
            df = df.loc[start:end]
            cum_q = Series(df['q_obs_cbm'].cumsum(), name='cum_q_cbm')
            cum_ppt = Series(df['precip_cbm'].cumsum(), name='cum_precip_cbm')
            cum_ro = Series(df['ro'].cumsum(), name='cum_ro')

            df = concat([df, cum_q, cum_ppt, cum_ro], axis=1)

            print 'new df with cumulative terms: \n{}'.format(df)
            data_dict[gauge_key] = {'Name': gauge_name, 'Start_End': (start, end), 'Data': df}
            name_list.append(data_dict[gauge_key]['Name'])

        # for item in etrm_results_path:
        #     gauge_key = item[:8]
        #     csv = loadtxt(item, dtype=float, delimiter=',',)
        #
        #     # put plots here #
        #     data_dict[gauge_key] = {'Name': gauge_name, 'Start_End': (start, end), 'Data': df}
        #     print data_dict

        # need to find out the name of the variables
        # for key, series in data_dict.iteritems():
        #     df = series['Data']
        #     df.plot(kind='line', subplots=2, title=series['Name'])
        #     plt.show()
            # plt.subplot(df[:, 0], df[:. 1])
            # fig = ax.get_figure()
            # how to call the name here
            # fig.savefig()

            # plot time series of discharge and precip #
            # put in two subplots, one of cumulative discharge, the other of cumulative precipitation #
            pass


if __name__ == '__main__':
    home = os.path.expanduser('~')
    print 'home: {}'.format(home)
    gauges = os.path.join(home, 'Documents', 'Recharge', 'Gauges')
    q_ppt_data_path = os.path.join(gauges, 'BasinPPT_GaugeQ_NM')
    q_path = os.path.join(gauges, 'GaugeQ')
    etrm_results_tables = os.path.join(gauges, 'basin_etrm_out')
    compare_ppt_discharge(q_ppt_data_path, etrm_results_tables)

# ============= EOF ============================================= #
