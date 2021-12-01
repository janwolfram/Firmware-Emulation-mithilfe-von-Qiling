import re
import json
import sys

enc = 'iso-8859-15'
file = open("questionmark/101-108_questionmark.txt", "r", encoding=enc)

text = file.read()
file.close()

devices = text.split("+++")

counter = 0
devices_splitted = []
index = 0
name = ""
emulation = ""

for item in devices[1:]:
    if "Number" in item:
        index += 1
    if "*" not in item:
        name = item
    else:    
        emulation = item
        devices_splitted.append({"device": name, "content": emulation})
whitelist_folder = ["bin", "sbin", "usr/bin", "usr/sbin"]


whitelist_help = ["Usage", "usage"]
whitelist_failed = ["not implemented", 
"'NoneType' object has no attribute 'cur_thread'", 
"QlErrorStructConversion",
"QlErrorFileNotFound",
"QlErrorFileType",
"QlErrorOsType",
"QlErrorOutput",
"QlErrorArch",
"QlErrorRuntype",
"QlErrorJsonDecode",
"QlErrorNotImplemented",
"QlErrorELFFormat",
"QlErrorMACHOFormat",
"QlErrorModuleFunctionNotFound",
"QlErrorModuleNotFound",
"QlErrorExecutionStop",
"QlErrorSyscallError",
"QlErrorSyscallNotFound",
"QlErrorCoreHook",
"QlOutOfMemory",
"QlMemoryMappedError",
"QlGDTError",
"Unknown error code",
"OK (UC_ERR_OK)",
"No memory available or memory not present (UC_ERR_NOMEM)",
"Invalid/unsupported architecture (UC_ERR_ARCH)",
"Invalid handle (UC_ERR_HANDLE)",
"Invalid mode (UC_ERR_MODE)",
"Different API version between core & binding (UC_ERR_VERSION)",
"Invalid memory read (UC_ERR_READ_UNMAPPED)",
"Invalid memory write (UC_ERR_WRITE_UNMAPPED)",
"Invalid memory fetch (UC_ERR_FETCH_UNMAPPED)",
"Invalid hook type (UC_ERR_HOOK)",
"Invalid instruction (UC_ERR_INSN_INVALID)",
"Invalid memory mapping (UC_ERR_MAP)",
"Write to write-protected memory (UC_ERR_WRITE_PROT)",
"Read from non-readable memory (UC_ERR_READ_PROT)",
"Fetch from non-executable memory (UC_ERR_FETCH_PROT)",
"Invalid argument (UC_ERR_ARG)",
"Read from unaligned memory (UC_ERR_READ_UNALIGNED)",
"Write to unaligned memory (UC_ERR_WRITE_UNALIGNED)",
"Fetch from unaligned memory (UC_ERR_FETCH_UNALIGNED)",
"Insufficient resource (UC_ERR_RESOURCE)",
"Unhandled CPU exception (UC_ERR_EXCEPTION)"]

for element in devices_splitted:
    device_version = ""
    device = {'name' : "", 'versions': []}
    for key, value in element.items():
        if "device" in key:
            #print(value)
            device["name"] = value
        if "content" in key:
            versions = value.split("***")
            version_no = ""
                
            for version in versions:
                total = 0
                succeded = 0
                failed = 0
                help = 0
                find_version = 0
                no_binary = 0
                succeded_return_zero = 0
                help_not_zero = 0
                help_and_succeded = 0
                version_and_succeded = 0
                
                count_bugs = [0] * 44
                binaries_detail = []

                if version_no:
                    folders = version.split("///")
                    foldername = ""
                    for folder in folders:
                        # print(folder)
                        if foldername:
                            binaries = folder.split("---")
                            binary_name = ""
                            for binary in binaries[1:]:
                                # print(binary)
                                if binary_name:
                                    # to debug
                                    #if "7581" in device["name"]:
                                        #print(binary_name)    
                                    detail = {"name": "", "isBinary": False, "help": False, "version": False, "succeded": False, "error": "none"}
                                    detail["name"] = binary_name
                                    return_code = binary.partition("return code:")[2].strip()

                                    total += 1
                                    if "unsupported operand type" in binary:
                                        no_binary += 1
                                    else:
                                        detail["isBinary"] = True
                                        help_flag = False
                                        failed_flag = False
                                        version_flag = False
                                        if re.search("(?<![\d\/])[0-9]+\.[0-9]+(?![\/\d])", binary) is not None:
                                            find_version += 1
                                            detail["version"] = True
                                            version_flag = True
                                        for word in whitelist_help:
                                            if word in binary:
                                                if not help_flag:
                                                    detail["help"] = True
                                                    help += 1
                                                    if return_code != "0":
                                                        help_not_zero +=1
                                                    help_flag = True
                                        for index, word in enumerate(whitelist_failed, start = 0):
                                            if word in binary:
                                                if not failed_flag: 
                                                    detail["error"] = word
                                                    count_bugs[index] += 1           
                                                    failed_flag = True
                                                    failed += 1 
                                        if not failed_flag:
                                            detail["succeded"] = True
                                            if help_flag:
                                                help_and_succeded += 1
                                            if version_flag:
                                                version_and_succeded += 1
                                            succeded += 1
                                            if return_code == "0":
                                                succeded_return_zero += 1
                                    binary_name = ""
                                    binaries_detail.append(detail)       
                                else :
                                    if len(binary.strip()) < 40 and len(binary.strip()) > 0:
                                        binary_name = binary.strip()        
                            foldername = ""

                        if folder in whitelist_folder:
                            foldername = folder

                    test_dict = {}
                    for i, e in enumerate(whitelist_failed, start = 0):
                        test_dict[e] = count_bugs[i]

                    if len(sys.argv) > 1 and  sys.argv[1] == "-b":
                        device["versions"].append({'version': device_version, 'total': total, 'help': help, 'version_no': find_version, 'failed': failed, 'succeded' : succeded, 'succeded&return_zero': succeded_return_zero, 'help&succeded': help_and_succeded, 'version&succeded': version_and_succeded, 'no_binary': no_binary, "binaries": binaries_detail , 'errors' : test_dict})   
                    else:
                        device["versions"].append({'version': device_version, 'total': total, 'help': help, 'version_no': find_version, 'failed': failed, 'succeded' : succeded, 'succeded&return_zero': succeded_return_zero, 'help&succeded': help_and_succeded, 'version&succeded': version_and_succeded, 'no_binary': no_binary , 'errors' : test_dict})
                    version_no = "" 
                if re.search("^[0-9]", version) is not None:
                    device_version = version
                    version_no = version       
    # print(device)   
    print(json.dumps(device, indent=1))          
