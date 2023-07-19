[cmdletBinding()]
param(
    [Parameter(Mandatory=$True, Position=0)]
    [string]
    $CmdSize,
    [Parameter(Mandatory=$True, Position=1)]
    [string]
    $CmdTable
)


$table = (New-Object 'int[,]' $CmdSize, $CmdSize)

function CreateIntMatrixFromStrInput {
    param (
        [Parameter(Mandatory)]
        [int]$Size,
        [Parameter(Mandatory)]
        [string]$TableElements
    )
    $TableElementsArray = $TableElements.Split("x")
    $i=0
    $j=0
    $counter = 0
    foreach ($elem in $TableElementsArray){
        if($i -ge $Size){
            break
        }
        $counter = $counter + 1
        $table[$i,$j] = ([int][string]$elem)

        if($counter%$Size -eq 0){
            $i=$i+1
        }
        if(($j+1)%$Size -eq 0 -and $j -ne 0){
            $j=0
        }
        else{
            $j=$j+1
        }
    }
}


function PrintMatrix {
    param (
        [Parameter(Mandatory)]
        [int[,]]$Matrix,
        [Parameter(Mandatory)]
        [int]$Width,
        [Parameter(Mandatory)]
        [int]$Height
    )

    for ($i=0; $i -lt $Width; $i++) {
        for ($j=0; $j -lt $Height; $j++) {
            Write-Host -NoNewline $Matrix[$i,$j] "  "
        }
        Write-Host
    }

}


function FindEmpty {
    param (
        [Parameter(Mandatory)]
        [int[,]]$Matrix,
        [Parameter(Mandatory)]
        [int]$Width,
        [Parameter(Mandatory)]
        [int]$Height
    )

    for ($i=0; $i -lt $Width; $i++) {
        for ($j=0; $j -lt $Height; $j++) {
           if ($Matrix[$i,$j] -eq 0){
                $emptyCoords = @($i,$j)
                return $emptyCoords
           }
        }
    }
    return $null
}


function Check {
    param (
        [Parameter(Mandatory)]
        [int[,]]$Matrix,
        [Parameter(Mandatory)]
        [int]$Width,
        [Parameter(Mandatory)]
        [int]$Height,
        [Parameter(Mandatory)]
        [int]$Number,
        [Parameter(Mandatory)]
        [int]$Xcoord,
        [Parameter(Mandatory)]
        [int]$Ycoord
    )
    # row
    for ($i=0; $i -lt $Width; $i++) {
        if ($Matrix[$Xcoord,$i] -eq $Number -and $Ycoord -ne $i){
            # not good row
            Write-Host Working..
            return $false
        }
    }

    # column
    for ($j=0; $j -lt $Height; $j++) {
        if ($Matrix[$j,$Ycoord] -eq $Number -and $Xcoord -ne $j){
            # not good column
            Write-Host Working..
            return $false
        }
    }

    $sqrtSize = [math]::Sqrt($Width)
    $X = [math]::Truncate($Ycoord/$sqrtSize)
    $Y = [math]::Truncate($Xcoord/$sqrtSize)

    for ($i = $Y*$sqrtSize; $i -lt $Y*$sqrtSize+$sqrtSize; $i++) {
        for ($j = $X*$sqrtSize; $j -lt $X*$sqrtSize+$sqrtSize; $j++) {
           if($Matrix[$i,$j] -eq $Number -and $i -ne $Xcoord -and $j -ne $Ycoord){
            return $false
           }
        }
    }
    return $true
}


function Solve {

    param (
        [Parameter(Mandatory)]
        [int[,]]$Matrix,
        [Parameter(Mandatory)]
        [int]$Width,
        [Parameter(Mandatory)]
        [int]$Height
    )

    $row, $col = FindEmpty -Matrix $Matrix -Width $Width -Height $Height

    if ($null -eq $row -or $null -eq $col){
        return $true
    }
    else{
        Write-Host Found empty: $row $col
    }

    for ($i = 1; $i -lt $Width+1; $i++){
        if(Check -Matrix $Matrix -Width $Width -Height $Height -Number $i -Xcoord $row -Ycoord $col){
            $Matrix[$row, $col] = $i
            # tried number is $i
            if(Solve -Matrix $Matrix -Width $Width -Height $Height){
                return $true
            }

            $Matrix[$row, $col] = 0

        }
    }
    return $false
}


CreateIntMatrixFromStrInput -Size $CmdSize -TableElements $CmdTable
PrintMatrix -Matrix $table -Width $CmdSize -Height $CmdSize
Solve -Matrix $table -Width $CmdSize -Height $CmdSize
PrintMatrix -Matrix $table -Width $CmdSize -Height $CmdSize
