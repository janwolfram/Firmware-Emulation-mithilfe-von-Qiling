import os

def execute_command(cmd):
    print("return code:", os.system(cmd))


def getDevicesList(path):
    paths = []
    for root, categories, files in os.walk(path):
        for category in categories:
            for _, devices, _ in os.walk(path+"/"+category):
                for device in devices:
                    paths.append({"name": device, "path": path + "/" +
                                 category + "/" + device, "category": category})
                break
        break
    return paths


PATH = '/home/janw/Videos/testfolder_emulations/unpacked_avm_firmwares_final'

# find all Devices
my_devices = getDevicesList(PATH)
# beliebige Anzahl an Geräten in das Array einfügen
devices = [my_devices[0]]
index = 1
for device in devices:
    print("Number: ", index)
    for key, value in device.items():
        if key == "name":
            print("+++" + value + "+++")
        if key == "path":
            for _, versions, _ in os.walk(value):
                for version in versions:
                    print("***" + version + "***")
                    if os.path.exists(value + "/" + version + "/original"):
                        filesystem = value + "/" + version + "/original" + "/filesystem"
                        # bin folder
                        print("///bin///")
                        for root, dirs, files in os.walk(filesystem + "/bin"):
                            for file in files:
                                print("---" + file + "---")
                                qltool = "python3 ../../Videos/qiling/qltool run -f {} --rootfs {} --verbose off --timeout 20000000 --args --help".format(
                                    filesystem + "/bin/" + file, filesystem)
                                execute_command(qltool)
                                print("---")
                        print("///")
                        # sbin folder
                        print("///sbin///")
                        for root, dirs, files in os.walk(filesystem + "/sbin"):
                            for file in files:
                                print("---" + file + "---")
                                qltool = "python3 ../../Videos/qiling/qltool run -f {} --rootfs {} --verbose off --timeout 20000000 --args --help".format(
                                    filesystem + "/sbin/" + file, filesystem)
                                execute_command(qltool)
                                print("---")
                        print("///")

                        # usr/bin folder
                        print("///usr/bin///")
                        for root, dirs, files in os.walk(filesystem + "/usr/bin"):
                            for file in files:
                                print("---" + file + "---")
                                qltool = "python3 ../../Videos/qiling/qltool run -f {} --rootfs {} --verbose off --timeout 20000000 --args --help".format(
                                    filesystem + "/usr/bin/" + file, filesystem)
                                execute_command(qltool)
                                print("---")
                        print("///")

                        # usr/sbin folder
                        print("///usr/sbin///")
                        for root, dirs, files in os.walk(filesystem + "/usr/sbin"):
                            for file in files:
                                print("---" + file + "---")
                                qltool = "python3 ../../Videos/qiling/qltool run -f {} --rootfs {} --verbose off --timeout 20000000 --args --help".format(
                                    filesystem + "/usr/sbin/" + file, filesystem)
                                execute_command(qltool)
                                print("---")
                        print("///")
                    print("***")

                break
    print("+++")
    index += 1

