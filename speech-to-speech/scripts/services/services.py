import os
import subprocess

def run_start_sh_recursive(path , break_dir) : 

    parts = path.split(os.sep)

    if parts[-1] == break_dir : run_start_sh(path) ; return

    for i in range(len(parts) -1 , -1 , -1) : 

        current_path = os.sep.join(parts[: i + 1])

        if os.path.isdir(current_path) : 

            if parts[i] == break_dir: run_start_sh(current_path) ; break
            else : run_start_sh(current_path)

def run_start_sh(directory) : 

    script_path = os.path.join(directory , 'start.sh')
    
    try :         
        
        os.chmod(script_path , 0o755)
        subprocess.run(['./start.sh'] , cwd = directory , check = True)

    except FileNotFoundError : print(f'start.sh not found in {directory}')
    except subprocess.CalledProcessError as e : print(f'Error running start.sh in {directory}: Return code {e.returncode}')
    except Exception as e : print(f'An unexpected error occurred in {directory}: {e}')