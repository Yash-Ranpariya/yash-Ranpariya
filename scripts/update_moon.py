import datetime
import urllib.request
import os

def get_moon_phase(date):
    year, month, day = date.year, date.month, date.day
    if month < 3:
        year -= 1
        month += 12
    month += 1
    c = 365.25 * year
    e = 30.6 * month
    jd = c + e + day - 694039.09
    jd /= 29.5305882
    jd = jd - int(jd)
    b = round(jd * 8)
    if b >= 8: b = 0
    return b

phases = [
    "1f311.svg", "1f312.svg", "1f313.svg", "1f314.svg",
    "1f315.svg", "1f316.svg", "1f317.svg", "1f318.svg"
]

def update_moon():
    today = datetime.datetime.utcnow()
    phase = get_moon_phase(today)
    
    url = "https://raw.githubusercontent.com/twitter/twemoji/master/assets/svg/" + phases[phase]
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as res:
        svg_content = res.read()
        
    with open("moon.svg", "wb") as f:
        f.write(svg_content)
    
    print(f"Updated moon to phase: {phase} ({phases[phase]})")

if __name__ == "__main__":
    update_moon()
