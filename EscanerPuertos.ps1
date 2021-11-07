# Parametro para la direccion ip a escanear
#
param([Parameter(Mandatory)] [string]$direccion_ip)
#
# Definimos un array con puertos a escanear
# Establecemos una variable para Waittime
#
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139)
$waittime = 100
#
# Generamos bucle foreach para evaluar cada puerto
#
foreach ($p in $portstoscan)
{
    $TpcObject = New-Object System.Net.Sockets.TcpClient
        try{ $resultado = $TpcObject.ConnectAsync($direccion_ip,$p).Wait($waittime)}catch{}
        if ($resultado -eq "True")
        {
            Write-Host "Puerto abierto:"$p
        }
}