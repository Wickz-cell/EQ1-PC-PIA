# Definimos un array con puertos a escanear
#Establecemos una variable para Waittime
#
$portstoscan = @(20,21,22,23,25,50,51,53,80,110,119,135,136,137,138,139)
$waittime = 100

# Solicitamos la direccion ip a escanear
#
Write-Host "Direccion ip a escanear: " -NoNewline
$direccion = Read-Host

#Generamos bucle foreach para evaluar cada puerto
#
foreach ($p in $portstoscan)
{
    $TpcObject = New-Object System.Net.Sockets.TcpClient
        try{ $resultado = $TpcObject.ConnectAsync($direccion,$p).Wait($waittime)}catch{}
        if ($resultado -eq "True")
        {
            Write-Host "Puerto abierto: " -NoNewline; Write-Host $p -ForegroundColor Green
        }
}
