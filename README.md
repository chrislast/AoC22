# AoC22
Advent of Code 2022 solutions

fetch *my* inputs from Powershell:
```powershell
# Get "session" cookie from logged in browser at https://adventofcode.com/2022
#    F12 -> Network (reload page) -> 2022 -> Headers -> Request Headers -> cookie

$session_cookie="53616c7465645f5fed8855a42edc1ab3adf7e7bf465e1c7f36cd1b0499d72d4d6f3d528b33d8081a8350c447237279bc35da5967f2fa59310e652f2c40a3bbff"
$wc = New-Object System.Net.WebClient
$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "session=$session_cookie")
for ($i=1; $i -le 25; $i++) {
	$pth = "c:/git/aoc22/input/$i.txt"
  	if (!(Test-Path $pth)) {
  		$wc.DownloadFile("https://adventofcode.com/2022/day/$i/input", $pth)
}}
```
