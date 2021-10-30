import subprocess

comando = ("powershell -ExecutionPolicy ByPass -File EscanerPuertos.ps1")
procesoPowerShell = subprocess.check_output(comando)
print(procesoPowerShell.decode())
