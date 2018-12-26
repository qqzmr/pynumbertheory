import difflib

def readfile(filename):
    try:
        file=open(filename,"rb")
        text=file.read().splitlines()
        file.close()
        return text
    except IOError as e:
        print(e)

textfile1="nsswitch1.conf"
textfile2="nsswitch2.conf"
t1_lines=readfile(textfile1)
t2_lines=readfile(textfile2)
diff=difflib.HtmlDiff()
file=open("diffconf.html","w")
file.write(diff.make_file(t1_lines, t2_lines))  # python2可用,python3有问题
file.close()

