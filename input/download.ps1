# Get "session" cookie from logged in browser at https://adventofcode.com/2022
#    F12 -> Network (reload page) -> 2022 -> Headers -> Request Headers -> cookie
# it stays valid until you [Log Out]
$session_cookie="53616c7465645f5fe07def8c91eeb588f0a6ad1b683aa2f51111fb170dc62b4cd99e1a11b6b7ea6ef7898513ceb18b3720e4cc52d0678355b2516c69f33e00d9"

$day = $(Get-Date).day
$wc = New-Object System.Net.WebClient
$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "session=$session_cookie")

# download input files for days 1-25 unless they already exist or aren't available yet
for ($i=1; $i -le 25; $i++) {
	$pth = "c:/git/aoc22/input/$i.txt"
  	if (!(Test-Path $pth)) {
  		try {
	  		$wc.DownloadFile("https://adventofcode.com/2022/day/$i/input", $pth)
	  		echo $pth
	  	} catch {}
}}

# open todays problem in a web browser
start https://adventofcode.com/2022/day/$day

# create solution from template if it doesn't exist yet
if (!(Test-Path "c:/git/aoc22/day$day.py")) {
  cp c:/git/aoc22/dayx.py c:/git/aoc22/day$day.py}
