# Get "session" cookie from logged in browser at https://adventofcode.com/2022
#    F12 -> Network (reload page) -> 2022 -> Headers -> Request Headers -> cookie
# it stays valid until you [Log Out]
$session_cookie="53616c7465645f5fe07def8c91eeb588f0a6ad1b683aa2f51111fb170dc62b4cd99e1a11b6b7ea6ef7898513ceb18b3720e4cc52d0678355b2516c69f33e00d9"

$d = $(Get-Date).day
$yyyy = $(Get-Date).year
$yy = $yyyy - 2000
$wc = New-Object System.Net.WebClient
$wc.Headers.Add([System.Net.HttpRequestHeader]::Cookie, "session=$session_cookie")
$srcdir = "C:/git/aoc$yy"

# download input files for days 1-25 unless they already exist or aren't available yet
for ($i=1; $i -le 25; $i++) {
	$pth = "$srcdir/input/$i.txt"
  	if (!(Test-Path $pth)) {
  		try {
	  		$wc.DownloadFile("https://adventofcode.com/$yyyy/day/$i/input", $pth)
	  		echo $pth
	  	} catch {}
}}

# open todays problem in a web browser
start https://adventofcode.com/$yyyy/day/$d

# create solution from template if it doesn't exist yet
if (!(Test-Path "$srcdir/day$d.py")) {
    cp "$srcdir/dayx.py" "$srcdir/day$d.py"}

# open files we want to edit or look at
& 'C:\Program Files\Sublime Text\subl.exe' `
    "$srcdir/example/example$d.txt" `
    "$srcdir/day$d.py" `
    "$srcdir/input/$d.txt"
