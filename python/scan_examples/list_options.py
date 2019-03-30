#!/usr/bin/env python3

# source ./activate_test_env.sh
# subprojects/libinsane-gobject/examples/list_options.py

import os

import gi
gi.require_version('Libinsane', '1.0')
from gi.repository import GObject  # noqa: E402

from gi.repository import Libinsane  # noqa: E402


class ExampleLogger(GObject.GObject, Libinsane.Logger):
    def do_log(self, lvl, msg):
        if lvl <= Libinsane.LogLevel.DEBUG:
            return
        print("{}: {}".format(lvl.value_nick, msg))


def main():
    if True:
        os.environ['LIBINSANE_NORMALIZER_ALL_OPTS_ON_ALL_SOURCES'] = "0"
        os.environ['LIBINSANE_NORMALIZER_BMP2RAW'] = "0"
        os.environ['LIBINSANE_NORMALIZER_CLEAN_DEV_DESCS'] = "0"
        os.environ['LIBINSANE_NORMALIZER_MIN_ONE_SOURCE'] = "0"
        os.environ['LIBINSANE_NORMALIZER_OPT_ALIASES'] = "0"
        os.environ['LIBINSANE_NORMALIZER_RAW24'] = "0"
        os.environ['LIBINSANE_NORMALIZER_RESOLUTION'] = "0"
        os.environ['LIBINSANE_NORMALIZER_SAFE_DEFAULTS'] = "0"
        os.environ['LIBINSANE_NORMALIZER_SOURCE_NAMES'] = "0"
        os.environ['LIBINSANE_NORMALIZER_SOURCE_NODES'] = "0"
        os.environ['LIBINSANE_NORMALIZER_SOURCE_TYPES'] = "0"
        os.environ['LIBINSANE_WORKAROUND_CACHE'] = "0"
        os.environ['LIBINSANE_WORKAROUND_CHECK_CAPABILITIES'] = "0"
        os.environ['LIBINSANE_WORKAROUND_DEDICATED_THREAD'] = "0"
        os.environ['LIBINSANE_WORKAROUND_ONE_PAGE_FLATBED'] = "0"
        os.environ['LIBINSANE_WORKAROUND_OPT_NAMES'] = "0"
        os.environ['LIBINSANE_WORKAROUND_OPT_VALUES'] = "0"

    Libinsane.register_logger(ExampleLogger())
    api = Libinsane.Api.new_safebet()

    devs = api.list_devices(Libinsane.DeviceLocations.ANY)
    print("Found {} devices".format(len(devs)))
    for dev in devs:
        print("")
        print("")
        print(dev.to_string())

        dev = api.get_device(dev.get_dev_id())
        children = dev.get_children()
        print("|-- Found {} sources".format(len(children)))

        for item in [dev] + children:
            print("|")
            print("|-- {} ({})".format(
                item.get_name(),
                "device" if item == dev else "source"
            ))
            opts = item.get_options()
            for opt in opts:
                print("|   |-- {}".format(opt.get_name()))
                print("|   |   |-- Title: {}".format(opt.get_title()))
                print("|   |   |-- Description: {}".format(opt.get_desc()))
                print("|   |   |-- Capabilities: {}".format(
                    opt.get_capabilities())
                )
                print("|   |   |-- Unit: {}".format(opt.get_value_unit()))
                print("|   |   |-- Constraint type: {}".format(
                      opt.get_constraint_type()))
                print("|   |   |-- Constraint: {}".format(
                    opt.get_constraint())
                )
                if opt.is_readable():
                    try:
                        print("|   |   |-- Value: {}".format(opt.get_value()))
                    except Exception as exc:
                        print("|   |   |-- Value: [{}]".format(str(exc)))
                else:
                    print("|   |   |-- Value: (unavailable)")
        print("")
        dev.close()


if __name__ == "__main__":
    main()
