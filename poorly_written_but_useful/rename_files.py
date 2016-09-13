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

import os

from gauges import initial_runoff_analysis


def rename_list_of_files(renamed_path, destination_names_path):

    dst_names = os.listdir(destination_names_path)
    print 'dst_names: {}'.format(dst_names)

    src_names = os.listdir(renamed_path)
    src_names.sort()
    print 'renames: {}'.format(src_names)

    for scr_name in src_names:
        for dst_name in dst_names:
            i, j = scr_name.split('.')
            if i in dst_name.lower():
                src = os.path.join(renamed_path, scr_name)
                dst = os.path.join(renamed_path, '{}.{}'.format(dst_name.replace('.csv', ''), j))
                print 'src: {}'.format(src)
                print 'dst: {}'.format(dst)
                # os.rename(src, dst)


if __name__ == '__main__':
    home = os.path.expanduser('~')
    print 'home: {}'.format(home)
    gauges = os.path.join(home, 'Documents', 'Recharge', 'Gauges')
    q_ppt_data_path = os.path.join(gauges, 'BasinPPT_GaugeQ_NM')
    to_rename = os.path.join('F:\\', 'ETRM_Inputs', 'NM_Geo_Shapes', 'Selected_Basin_Polygons')
    rename_list_of_files(to_rename, q_ppt_data_path)

# ==================== EOF =========================
