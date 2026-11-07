"""Builds profile/streak.svg from the GitHub contribution calendar.

Replaces the public streak-stats service, which often fails with
"Failed to retrieve contributions". Runs in Actions with GITHUB_TOKEN.
usage: python .github/scripts/streak.py <username> <out.svg>
"""
import datetime as dt
import json
import os
import sys
import urllib.request

USER, OUT = sys.argv[1], sys.argv[2]
TOKEN = os.environ["GITHUB_TOKEN"]


def gql(query, **variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "User-Agent": "profile-streak"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if "errors" in body:
        raise SystemExit(body["errors"])
    return body["data"]


created = gql("query($u:String!){user(login:$u){createdAt}}", u=USER)["user"]["createdAt"]
today = dt.datetime.now(dt.timezone.utc).date()
days = {}
for year in range(int(created[:4]), today.year + 1):
    start = max(dt.date(year, 1, 1), dt.date.fromisoformat(created[:10]))
    end = min(dt.date(year, 12, 31), today)
    cal = gql(
        """query($u:String!,$f:DateTime!,$t:DateTime!){user(login:$u){
             contributionsCollection(from:$f,to:$t){contributionCalendar{
               weeks{contributionDays{date contributionCount}}}}}}""",
        u=USER, f=f"{start}T00:00:00Z", t=f"{end}T23:59:59Z",
    )["user"]["contributionsCollection"]["contributionCalendar"]
    for w in cal["weeks"]:
        for d in w["contributionDays"]:
            days[dt.date.fromisoformat(d["date"])] = d["contributionCount"]

dates = sorted(d for d in days if d <= today)
total = sum(days[d] for d in dates)
first = next((d for d in dates if days[d] > 0), today)

# longest streak
best, best_span, run, run_start = 0, (None, None), 0, None
for d in dates:
    if days[d] > 0:
        run_start = d if run == 0 else run_start
        run += 1
        if run > best:
            best, best_span = run, (run_start, d)
    else:
        run = 0

# current streak (today may still be empty)
cur, d = 0, today if days.get(today, 0) > 0 else today - dt.timedelta(days=1)
cur_end = d
while days.get(d, 0) > 0:
    cur += 1
    d -= dt.timedelta(days=1)
cur_start = d + dt.timedelta(days=1)


def fmt(x):
    return x.strftime("%b %-d, %Y") if x.year != today.year else x.strftime("%b %-d")


cur_label = f"{fmt(cur_start)} – {fmt(cur_end)}" if cur else "start one today"
best_label = f"{fmt(best_span[0])} – {fmt(best_span[1])}" if best else "—"
total_label = f"{fmt(first)} – Present"

ring = 2 * 3.14159 * 40
frac = min(1.0, cur / best) if best else 0.0
svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="495" height="195" viewBox="0 0 495 195" role="img" aria-label="{USER} contribution streak">
<style>
 .n{{font:700 28px 'Segoe UI',Ubuntu,'Helvetica Neue',sans-serif;fill:#C9D1D9}}
 .l{{font:600 14px 'Segoe UI',Ubuntu,sans-serif;fill:#C9D1D9}}
 .a{{fill:#58A6FF}}
 .d{{font:400 11px 'Segoe UI',Ubuntu,sans-serif;fill:#8B949E}}
</style>
<rect width="495" height="195" rx="6" fill="#0D1117"/>
<line x1="165" y1="28" x2="165" y2="170" stroke="#30363D"/>
<line x1="330" y1="28" x2="330" y2="170" stroke="#30363D"/>
<text class="n" x="82.5" y="88" text-anchor="middle">{total:,}</text>
<text class="l" x="82.5" y="122" text-anchor="middle">Total Contributions</text>
<text class="d" x="82.5" y="146" text-anchor="middle">{total_label}</text>
<circle cx="247.5" cy="72" r="40" fill="none" stroke="#30363D" stroke-width="5"/>
<circle cx="247.5" cy="72" r="40" fill="none" stroke="#58A6FF" stroke-width="5" stroke-linecap="round"
  stroke-dasharray="{ring * max(frac, 0.02):.1f} {ring:.1f}" transform="rotate(-90 247.5 72)"/>
<text class="n" x="247.5" y="82" text-anchor="middle">{cur}</text>
<text class="l a" x="247.5" y="136" text-anchor="middle">Current Streak</text>
<text class="d" x="247.5" y="158" text-anchor="middle">{cur_label}</text>
<text class="n" x="412.5" y="88" text-anchor="middle">{best}</text>
<text class="l" x="412.5" y="122" text-anchor="middle">Longest Streak</text>
<text class="d" x="412.5" y="146" text-anchor="middle">{best_label}</text>
</svg>
"""
os.makedirs(os.path.dirname(OUT) or ".", exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(svg)
print(f"total={total} current={cur} longest={best}")
