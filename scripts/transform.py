import subprocess
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('--input', help="Directory of file to transform")
parser.add_argument('--output', help="Directory for transformed files")
args = vars(parser.parse_args())


def run_shell_cmd(cmd):
    try:
        p = subprocess.Popen(cmd.split(), stdout=subprocess.PIPE)
        last_stdout_bytes, last_stderr_bytes = p.communicate()
        if last_stdout_bytes:
            return last_stdout_bytes.decode('utf-8', 'replace')
        else:
            return last_stderr_bytes
    except Exception as e:
        print(e)

run_shell_cmd("gdalwarp -s_srs EPSG:4326 -t_srs EPSG:4326 -to SRC_METHOD=NO_GEOTRANSFORM -tr 0.5 0.5 -r near -te -180.0 -90.0 180.0 90.0 -te_srs EPSG:4326 -of GTiff " + args.get('input') + " " + args.get('output'))