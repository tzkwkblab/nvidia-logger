from xml.etree import ElementTree
import subprocess
import json
import sys


if __name__ == '__main__':
    document = ElementTree.parse(sys.argv[1])

    mems = document.findall('.//fb_memory_usage')
    utils = document.findall('.//utilization')
    procs = document.findall('.//process_info')

    ret = {}

    for mem in mems:
        for mem_ in mem:
            ret[mem_.tag] = mem_.text

    for util in utils:
        for util_ in util:
            ret[util_.tag] = util_.text

    ret['procs'] = []
    for proc in procs:

        mini_dic = {}
        for proc_ in proc:
            if proc_.tag == 'pid':
                cmd = 'ps aux| grep {}'.format(proc_.text)
                ps = subprocess.Popen(cmd, shell=True,
                                      stdout=subprocess.PIPE,
                                      stderr=subprocess.STDOUT)

                for line in ps.communicate()[0].decode().split('\n'):
                    if proc_.text in line:
                        elements = line.split()
                        pid = elements[1]
                        time = elements[9]

                        if proc_.text == pid:
                            mini_dic['time'] = time

            if proc_.tag == 'used_memory':
                mini_dic[proc_.tag] = proc_.text

        ret['procs'].append(mini_dic)

    with open(sys.argv[1].replace('xml', 'json'), 'a+') as log_file:
        log_file.seek(len(log_file.readline()) + 1)
        log_file.write(json.dumps(ret))
        log_file.write('\n')
