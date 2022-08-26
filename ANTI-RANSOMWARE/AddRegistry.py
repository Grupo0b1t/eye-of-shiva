import winreg as reg
import ctypes, sys
import os            


def is_admin(): # request run as admin
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
        

def AddToRegistry(script =  os.path.realpath(__file__), key = reg.HKEY_LOCAL_MACHINE, **kwarg):
    """This function will add to windows registries to initialize current script along with OS

    Args:
        script (str, optional): Path of the script you want to add to the records. Defaults to os.path.realpath(__file__).
        key (module, optional): Location where the key will be made. Defaults to reg.HKEY_CURRENT_USER.
        **kwargs (str, required key 'name'): Registry Name.
    """
    if is_admin():
        path = "Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        open = reg.OpenKey(key, path, 0, reg.KEY_ALL_ACCESS)
        try:
            reg.SetValueEx(open, kwarg["name"],0,reg.REG_SZ, script) 
            reg.CloseKey(open)
        except KeyError:
            print("Set a name for your registry, ex: AddToRegisty(name='anyName')")
        except Exception as err:
            print(err)
    else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__=="__main__":
    path = ''
    AddToRegistry(script=path, name=" ") #change name and path