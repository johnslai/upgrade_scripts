#!/usr/bin/env python
import argparse


def conf2json():
  pass

def parse_xml(string):
  import xmltodict
  return xmltodict.parse(string)["gdaq"]



def get_file():
  parser = argparse.ArgumentParser(description='Convert gdaq.conf to gdaq.json.')
  parser.add_argument('conf_file', nargs='?', default="gdaq.conf", help="gdaq.conf")
  args = parser.parse_args()
  conf_file = args.conf_file
  print(conf_file)
  return conf_file

def write_json(fn, gdaq_conf):
  import json
  with open(fn, "w") as fp:
    json.dump(gdaq_conf, fp, indent=2, sort_keys=True)


def fix_syntax(conf_file):
  import re
  sub1=(r"(<devices>)")
  repl1=(r"<gdaq>\n<devices>")
  sub2=(r"(</cloud>)")
  repl2=("</cloud>\n</gdaq>")
  sub3=(r"(std_ratio)")
  repl3=(r"stddev_ratio")
  subs = [ sub1, sub2, sub3 ]
  repls = [ repl1, repl2, repl3 ]
  string = "";
  #subs_repls = zip(subs, repls)
  with open(conf_file, 'r') as infile:
    for line in infile:
      for [sub, repl] in zip(subs, repls):
        line = re.sub(sub, repl, line)
      string = string + line

  return string

current_scale = {
    "20": 0.00089667390,
    "30": 0.0011991983,
    "75": 0.00299799575
    }

phase_map = {
    "0": "N",
    "1": "C",
    "2": "B",
    "3": "A"
    }

default_channel = {
    "scale": 0.0008966739,
    "phase_high": "C", 
    "phase_low": "N", 
    "breaker_size": 20, 
    "enabled": True, 
    "type": "current", 
    "id": 0
    }

def modify_dict(gdaq_conf):
  import json
  with open("gdaq_example.json", "r") as fp:
    new_conf = json.load(fp)

  # no need to merge device, waveparser, control, send
  # merge bud.serial and  channels
  new_conf["bud"]["serial"]=gdaq_conf["bud"]["serial"]
  old_channels = gdaq_conf["channels"]
  # voltage channels, no change
  # current channels, change breaker_size, 
  # scale, phase_high, phase_low, ct_size
  for i in range(4,46):
    new_channelx = default_channel.copy();
    old_channelx = old_channels.get("channel"+str(i), default_channel)
    new_channelx["scale"] = current_scale[str(int(float(old_channelx.get('ct_size', '20'))))]

    new_channelx["phase_high"] = phase_map[str(old_channelx.get('voltage_id', '1'))]
    new_channelx["phase_low"] = "N"
    new_channelx["breaker_size"] = float(old_channelx.get('breaker_size', '20'))
    new_channelx["enabled"] = (old_channelx.get('enabled', '1') == '1')
    new_conf["channels"]["channel"+str(i)] = new_channelx
  return new_conf

def main():
  conf_file = get_file()
  xml_string = fix_syntax(conf_file)
  gdaq_conf = parse_xml(xml_string)
  new_conf = modify_dict(gdaq_conf)
  write_json("gdaq.json", new_conf)
  

if __name__ == '__main__':
  main()
